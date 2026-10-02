#!/usr/bin/env python3
"""Portable checksum-verified installer for super-global-skill (standard library only)."""
from __future__ import annotations
import argparse, datetime, hashlib, json, os, shutil, sys, uuid
from pathlib import Path, PurePosixPath

NAME='super-global-skill'; VERSION='2.0.0'; PACKAGE=Path(__file__).resolve().parent
AGENTS=('codex','claude','opencode','antigravity','antigravity-cli','gemini','cursor','copilot','windsurf','cline','generic')
ALIASES={'claudecode':'claude','claude-code':'claude','antigravity-ide':'antigravity','gemini-cli':'gemini','agents':'generic'}

def digest(p:Path): return hashlib.sha256(p.read_bytes()).hexdigest()
def reject_links(p:Path):
    for x in (p,*p.parents):
        if x.is_symlink() or (hasattr(x,'is_junction') and x.is_junction()): raise ValueError('Symlink/junction requires an explicitly resolved destination: '+str(x))
def atomic_json(p:Path,v):
    p.parent.mkdir(parents=True,exist_ok=True); t=p.with_name(p.name+'.tmp-'+uuid.uuid4().hex)
    try: t.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8'); os.replace(t,p)
    finally:
        if t.exists(): t.unlink()
def safe_relative(v):
    q=PurePosixPath(v)
    if not v or q.is_absolute() or '..' in q.parts or '\\' in v or ':' in v: raise ValueError('Unsafe manifest path: '+v)
    return Path(*q.parts)
def tree_hashes(root:Path):
    if not root.exists(): return {}
    if not root.is_dir(): raise ValueError('Expected directory: '+str(root))
    reject_links(root); out={}
    for p in sorted(root.rglob('*')):
        if any(part in ('.git', '__pycache__', '.pytest_cache') for part in p.parts):
            continue
        if p.name in ('.gitignore', '.DS_Store', 'Thumbs.db') or p.name.endswith('.pyc'):
            continue
        reject_links(p)
        if p.is_file(): out[p.relative_to(root).as_posix()]=digest(p)
    return out
def verify_package(package=PACKAGE):
    m=json.loads((package/'package-manifest.json').read_text(encoding='utf-8'))
    if m.get('name')!=NAME or m.get('schema_version')!=1: raise ValueError('Unrecognized package manifest')
    expected=m.get('files')
    if not isinstance(expected,dict) or not expected: raise ValueError('Empty package manifest')
    for rel,want in expected.items():
        p=package/safe_relative(rel); reject_links(p)
        if not p.is_file() or digest(p)!=want: raise ValueError('Package checksum mismatch: '+rel)
    extra=set(tree_hashes(package))-set(expected)-{'package-manifest.json'}
    if extra: raise ValueError('Unmanifested package files: '+', '.join(sorted(extra)[:10]))
    if NAME+'/SKILL.md' not in expected: raise ValueError('Missing canonical SKILL.md')
    return m

def roots(home:Path,agent:str,project=None,skills_dir=None):
    if skills_dir: return skills_dir.expanduser().absolute(), None
    if project:
        p=project.expanduser().absolute()
        if not p.is_dir(): raise ValueError('Project directory does not exist: '+str(p))
        sub='.claude/skills' if agent=='claude' else '.opencode/skills' if agent=='opencode' else '.agents/skills'
        return p/sub,None
    mapping={'codex':'.agents/skills','generic':'.agents/skills','claude':'.claude/skills','opencode':'.config/opencode/skills','antigravity':'.gemini/config/skills','antigravity-cli':'.gemini/antigravity-cli/skills','gemini':'.gemini/skills','cursor':'.cursor/skills','copilot':'.copilot/skills','windsurf':'.codeium/windsurf/skills','cline':'.cline/skills'}
    return home/mapping[agent], None
def plugin_root(home:Path,agent:str):
    return home/'.gemini/config/plugins' if agent=='antigravity' else home/'.gemini/antigravity-cli/plugins' if agent=='antigravity-cli' else None
def detect(home:Path):
    checks=[('codex',('.codex','.agents')),('claude',('.claude',)),('opencode',('.config/opencode',)),('antigravity',('.gemini/config','.gemini/antigravity')),('antigravity-cli',('.gemini/antigravity-cli',)),('gemini',('.gemini',)),('cursor',('.cursor',)),('copilot',('.copilot',)),('windsurf',('.codeium/windsurf',)),('cline',('.cline',))]
    found=[]
    for name,paths in checks:
        if any((home/p).is_dir() for p in paths): found.append(name)
    return list(dict.fromkeys(found))
def resolve(a,home):
    a=ALIASES.get(a,a)
    if a=='all': return a
    if a!='auto':
        if a not in AGENTS: raise ValueError('Unknown agent: '+a)
        return a
    found=detect(home)
    if len(found)>1: raise ValueError('Multiple agents detected ('+', '.join(found)+'). Select --agent explicitly; no files changed.')
    return found[0] if found else 'generic'
def copy_checked(src:Path,dst:Path):
    shutil.copytree(src,dst)
    if tree_hashes(src)!=tree_hashes(dst): raise RuntimeError('Checksum mismatch while staging '+str(src))
def backup_dir(target:Path,tx:Path,record:dict,replace:bool):
    existing=tree_hashes(target)
    if not existing: return existing
    marker=target/'.super-global-native.json'
    if not replace:
        if not marker.is_file(): raise ValueError('Unmanaged destination exists: '+str(target)+'; use --replace after review')
        try: m=json.loads(marker.read_text(encoding='utf-8'))
        except json.JSONDecodeError as e: raise ValueError('Invalid install marker: '+str(target)) from e
        if m.get('files') != {k:v for k,v in existing.items() if k!='.super-global-native.json'}: raise ValueError('Locally modified destination: '+str(target))
    previous=tx/'previous-native'/target.name; previous.parent.mkdir(parents=True,exist_ok=True); target.rename(previous); record['previous']=str(previous); record['had_previous']=True; return existing

def sync_native(source_roots:list[Path],target_root:Path,tx:Path,records:list,replace:bool,dry:bool):
    sources=[]
    for root in source_roots:
        if root.is_dir(): sources += [p for p in sorted(root.iterdir()) if p.is_dir() and (p/'SKILL.md').is_file()]
    seen=set(); sources=[p for p in sources if not (p.name in seen or seen.add(p.name))]
    if dry: return [p.name for p in sources]
    target_root.mkdir(parents=True,exist_ok=True)
    for src in sources:
        dst=target_root/src.name; incoming=tree_hashes(src); existing=tree_hashes(dst)
        if existing and {k:v for k,v in existing.items() if k!='.super-global-native.json'}==incoming: continue
        record={'target':str(dst),'after':incoming,'had_previous':False}
        if dst.exists(): backup_dir(dst,tx,record,replace)
        stage=tx/('.native-stage-'+src.name); copy_checked(src,stage); atomic_json(stage/'.super-global-native.json',{'name':src.name,'version':VERSION,'files':incoming}); record['after']=tree_hashes(stage); stage.rename(dst); records.append(record)

def sync_plugins(source_root,target_root,tx,records,replace,dry):
    if not target_root or not source_root.is_dir(): return []
    names=[p.name for p in sorted(source_root.iterdir()) if p.is_dir()]
    if dry: return names
    target_root.mkdir(parents=True,exist_ok=True)
    for src in sorted(source_root.iterdir()):
        if not src.is_dir(): continue
        dst=target_root/src.name; incoming=tree_hashes(src); existing=tree_hashes(dst)
        if existing==incoming: continue
        rec={'target':str(dst),'after':incoming,'had_previous':False,'plugin':True}
        if dst.exists():
            if not replace: raise ValueError('Native plugin exists and differs: '+str(dst)+'; use --replace')
            prev=tx/'previous-plugins'/dst.name; prev.parent.mkdir(parents=True,exist_ok=True); dst.rename(prev); rec['previous']=str(prev); rec['had_previous']=True
        stage=tx/('.plugin-stage-'+src.name); copy_checked(src,stage); stage.rename(dst); records.append(rec)
    return names

def sync_rules(agent,home,package,tx,records,replace,dry):
    src=package/NAME/'references/platforms/antigravity/rules'
    if not src.is_dir(): return []
    if agent=='claude': destroot=home/'.claude'; names={'AGENTS.md':'AGENTS.md','SOUL.md':'SOUL.md','CLAUDE.md':'AGENTS.md'}
    elif agent in ('antigravity','gemini'): destroot=home/'.gemini'; names={'AGENTS.md':'AGENTS.md','GEMINI.md':'SOUL.md'}
    elif agent=='antigravity-cli': destroot=home/'.gemini/antigravity-cli'; names={'AGENTS.md':'AGENTS.md','GEMINI.md':'SOUL.md'}
    elif agent=='codex': destroot=home/'.codex'; names={'AGENTS.md':'AGENTS.md'}
    else: return []
    if dry: return [str(destroot/n) for n in names]
    destroot.mkdir(parents=True,exist_ok=True)
    for out,inside in names.items():
        source=src/inside; dest=destroot/out
        if not source.is_file(): continue
        if dest.exists() and dest.read_bytes()==source.read_bytes(): continue
        rec={'target':str(dest),'after':digest(source),'rule':True,'had_previous':dest.exists()}
        if dest.exists():
            if not replace: raise ValueError('Rule exists and differs: '+str(dest)+'; use --replace')
            prev=tx/'previous-rules'/dest.name; prev.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(dest,prev); rec['previous']=str(prev)
        shutil.copy2(source,dest); records.append(rec)
    return list(names)

def install(agent,home,project=None,skills_dir=None,dry=False,replace=False,universal_only=False,skip_plugins=False,install_rules=False,package=PACKAGE,_manifest=None,_incoming=None):
    manifest=_manifest or verify_package(package); home=home.expanduser().absolute(); project=project.expanduser().absolute() if project else None
    if agent=='all':
        if project or skills_dir: raise ValueError('--agent all cannot be combined with --project/--skills-dir')
        incoming=tree_hashes(package/NAME) if _incoming is None else _incoming
        results=[install(a,home,dry=dry,replace=replace,universal_only=universal_only,skip_plugins=skip_plugins,install_rules=install_rules,package=package,_manifest=manifest,_incoming=incoming) for a in AGENTS[:-1]]
        return {'status':'planned' if dry else 'installed','agent':'all','results':results,'version':manifest['version']}
    agent=resolve(agent,home); root,_=roots(home,agent,project,skills_dir); target=root/NAME; source=package/NAME; reject_links(root); reject_links(target)
    incoming=tree_hashes(source) if _incoming is None else _incoming; existing=tree_hashes(target); existing_payload={k:v for k,v in existing.items() if k!='.super-skill-install.json'}; marker=target/'.super-skill-install.json'
    if existing and existing_payload!=incoming and not replace:
        if not marker.is_file(): raise ValueError('Unmanaged destination exists: '+str(target)+'; use --replace')
        m=json.loads(marker.read_text(encoding='utf-8'))
        if m.get('files')!=existing_payload: raise ValueError('Installed skill was modified: '+str(target)+'; use --replace')
    # The Antigravity payload is installed natively only on Antigravity profiles.
    # Other agents receive the universal entry point; this avoids exposing
    # upstream directory names that are not valid for every host's discovery rules.
    native_sources=[source/'references/platforms/antigravity/skills',source/'references/reuseforge-skills'] if agent in ('antigravity','antigravity-cli') else []
    native_target=root
    psource=source/'references/platforms/antigravity/plugins'; ptarget=plugin_root(home,agent)
    if dry:
        return {'status':'planned','agent':agent,'target':str(target),'files':len(incoming),'native_skills':sum(1 for r in native_sources if r.is_dir() for p in r.iterdir() if p.is_dir() and (p/'SKILL.md').is_file()) if not universal_only else 0,'native_plugins':len(list(psource.iterdir())) if ptarget and psource.is_dir() and not skip_plugins else 0,'rules':bool(install_rules)}
    state=root.parent/('.'+NAME+'-backups'); reject_links(state); tx=state/(datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'-'+uuid.uuid4().hex[:10]); tx.mkdir(parents=True); (target.parent).mkdir(parents=True,exist_ok=True); receipt_path=tx/'receipt.json'
    receipt={'schema_version':1,'name':NAME,'version':manifest['version'],'status':'preparing','agent':agent,'target':str(target),'had_previous':bool(existing),'previous_hashes':existing,'after':{},'native':[],'rules':[],'plugins':[]}
    atomic_json(receipt_path,receipt); moved=False
    try:
        stage=tx/('.universal-stage-'+uuid.uuid4().hex); copy_checked(source,stage); atomic_json(stage/'.super-skill-install.json',{'name':NAME,'version':VERSION,'files':incoming}); receipt['after']=tree_hashes(stage); receipt['status']='staged'; atomic_json(receipt_path,receipt)
        if tree_hashes(target)!=existing: raise RuntimeError('Destination changed during installation')
        if target.exists(): target.rename(tx/'previous-universal'); receipt['previous_universal']=str(tx/'previous-universal'); moved=True
        stage.rename(target)
        if not universal_only: sync_native(native_sources,native_target,tx,receipt['native'],replace,False)
        if ptarget and not skip_plugins and not universal_only: sync_plugins(psource,ptarget,tx,receipt['plugins'],replace,False)
        if install_rules: sync_rules(agent,home,package,tx,receipt['rules'],replace,False)
        receipt['status']='installed'; atomic_json(receipt_path,receipt)
    except Exception:
        # Restore the universal tree and every native item changed in this transaction.
        if target.exists() and tree_hashes(target)==receipt.get('after'): target.rename(tx/'failed-universal')
        if moved and not target.exists(): (tx/'previous-universal').rename(target)
        for rec in reversed(receipt['native']+receipt['plugins']):
            dst=Path(rec['target'])
            if dst.exists() and tree_hashes(dst)==rec['after'] or (dst.exists() and rec.get('plugin') and tree_hashes(dst)==rec['after']): shutil.rmtree(dst)
            if rec.get('had_previous') and Path(rec.get('previous','')).exists(): Path(rec['previous']).rename(dst)
        for rec in reversed(receipt['rules']):
            dst=Path(rec['target'])
            if rec.get('had_previous') and Path(rec.get('previous','')).exists(): shutil.copy2(rec['previous'],dst)
            elif dst.exists(): dst.unlink()
        receipt['status']='failed'; atomic_json(receipt_path,receipt); raise
    return {'status':'installed','agent':agent,'target':str(target),'files':len(incoming),'native_skills':len(receipt['native']),'native_plugins':len(receipt['plugins']),'receipt':str(receipt_path),'rollback':'python install.py --rollback "'+str(receipt_path)+'"'}

def rollback(path):
    path=path.expanduser().absolute(); reject_links(path); r=json.loads(path.read_text(encoding='utf-8'))
    if r.get('schema_version')!=1 or r.get('name')!=NAME: raise ValueError('Unrecognized receipt')
    if r.get('status')=='rolled_back': return {'status':'already_rolled_back'}
    if r.get('status')!='installed': raise ValueError('Receipt is not installed')
    target=Path(r['target']); reject_links(target)
    if tree_hashes(target)!=r['after']: raise ValueError('Installed universal skill changed; refusing rollback')
    for rec in r['native']+r['plugins']:
        dst=Path(rec['target'])
        if dst.exists() and tree_hashes(dst)!=rec['after']: raise ValueError('Installed native payload changed: '+str(dst))
    for rec in r['rules']:
        dst=Path(rec['target'])
        if dst.exists() and digest(dst)!=rec['after']: raise ValueError('Installed rule changed: '+str(dst))
    rolled=path.parent/('rolled-back-'+uuid.uuid4().hex[:8]); target.rename(rolled)
    if r.get('had_previous'): Path(r['previous_universal']).rename(target)
    for rec in reversed(r['native']+r['plugins']):
        dst=Path(rec['target'])
        if dst.exists(): shutil.rmtree(dst)
        if rec.get('had_previous') and Path(rec.get('previous','')).exists(): Path(rec['previous']).rename(dst)
    for rec in reversed(r['rules']):
        dst=Path(rec['target'])
        if rec.get('had_previous') and Path(rec.get('previous','')).exists(): shutil.copy2(rec['previous'],dst)
        elif dst.exists(): dst.unlink()
    r['status']='rolled_back'; atomic_json(path,r); return {'status':'rolled_back','target':str(target),'preserved_new_version':str(rolled)}

def main(argv=None):
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('--agent',default='auto'); p.add_argument('--home',type=Path,default=Path.home()); p.add_argument('--project',type=Path); p.add_argument('--skills-dir',type=Path); p.add_argument('--dry-run',action='store_true'); p.add_argument('--replace',action='store_true'); p.add_argument('--universal-only',action='store_true'); p.add_argument('--skip-plugins',action='store_true'); p.add_argument('--install-rules',action='store_true'); p.add_argument('--verify',action='store_true'); p.add_argument('--rollback',type=Path); a=p.parse_args(argv)
    if a.project and a.skills_dir: p.error('Choose --project or --skills-dir, not both')
    if a.rollback: out=rollback(a.rollback)
    elif a.verify:
        m=verify_package(); out={'status':'verified','name':m['name'],'version':m['version'],'files':len(m['files'])}
    else: out=install(a.agent,a.home,a.project,a.skills_dir,a.dry_run,a.replace,a.universal_only,a.skip_plugins,a.install_rules)
    print(json.dumps(out,ensure_ascii=False,indent=2)); return 0
if __name__=='__main__':
    try: sys.exit(main())
    except (ValueError,RuntimeError,OSError,KeyError,json.JSONDecodeError) as e: print('ERROR: '+str(e),file=sys.stderr); sys.exit(1)
