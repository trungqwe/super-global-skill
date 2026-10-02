#!/usr/bin/env python3
"""Offline, bounded, diacritic-insensitive lookup over the bundled skill catalog."""
from __future__ import annotations
import argparse,json,re,unicodedata
import sys
from pathlib import Path
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
ROOT=Path(__file__).resolve().parents[1]

def normalize(value):
    value=value.lower().replace('đ','d')
    return ''.join(c for c in unicodedata.normalize('NFD',value) if not unicodedata.combining(c))
ALIASES={
 'clean-code':['code sach','code gon','de doc','readable','refactor clean'],
 'database-design':['thiet ke bang','database','csdl','schema','sql'],
 'ui-ux-pro-max':['giao dien dep','lam lai ui','ui ux','design system'],
 'lieflat-charts':['ve bieu do','lam chart','dashboard','visualization'],
 'humanizer':['khử giọng ai','khu giong ai','nguoi hon','humanize'],
 'docx':['file word','xuat word','word document'], 'pptx':['lam slide','thuyet trinh','presentation'],
 'xlsx':['tinh toan','xuat excel','spreadsheet'], 'code-review-skill':['review code','review pr'],
 'rune-debug':['bi loi','tim nguyen nhan','tai sao bi','debug'],
 'rune-audit':['audit','soi he thong','kiem toan'], 'rune-verification':['nghiem thu','kiem chung','xac minh'],
 'architecture-solution-review':['kien truc','nen chon cong nghe','architecture'],
 'context-memory-ops':['ban giao','tiep tuc phien','nen context','handoff'],
 'rune-plan':['lap ke hoach','plan','roadmap'], 'rune-test':['test','kiem thu','regression'],
 'reuseforge-orchestrator':['tim skill','tim repo','reuseforge','tai su dung'],
 'reuseforge-asset-scout':['tim repository','tim package','tim component','asset discovery'],
}
def search(query,limit=5):
    try: limit=max(1,min(int(limit),5))
    except (TypeError,ValueError): limit=5
    q=normalize(query); words=set(w for w in re.findall(r'[a-z0-9][a-z0-9-]*',q) if len(w)>2 and w not in {'use','when','the','and','for','cho','mot','toi','can','lam','make'})
    data=json.loads((ROOT/'references/skill-index.json').read_text(encoding='utf-8')); out=[]
    for item in data:
        ident=normalize(item['id']); desc=normalize(item.get('description','')); hay=ident+' '+desc
        score=sum(8 if w in ident.split('-') else 2 if w in hay else 0 for w in words)
        score+=30 if ident in q else 0
        for phrase in ALIASES.get(item['id'],[]):
            if normalize(phrase) in q: score+=12
        if score: out.append({'skill':item['id'],'kind':item['kind'],'source':item['source'],'description':item['description'],'path':str(ROOT/item['path']),'score':score})
    return sorted(out,key=lambda x:(-x['score'],x['skill'],x['path']))[:limit]
if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('query');p.add_argument('--limit',type=int,default=5);a=p.parse_args();print(json.dumps(search(a.query,a.limit),ensure_ascii=False,indent=2))
