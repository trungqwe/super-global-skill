# Script cài đặt / đồng bộ plugins và rules sang Google Antigravity (~/.gemini/config/plugins/)
param (
    [string]$TargetPluginsDir = "$env:USERPROFILE\.gemini\config\plugins"
)

Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host " [Google Antigravity] Đồng bộ bộ kỹ năng & Plugins" -ForegroundColor Green
Write-Host "==========================================================" -ForegroundColor Cyan

if (-not (Test-Path $TargetPluginsDir)) {
    New-Item -ItemType Directory -Path $TargetPluginsDir -Force | Out-Null
}

$CurrentDir = Split-Path -Parent $PSScriptRoot
$PluginsSource = Join-Path $CurrentDir "plugins"
$RulesSource = Join-Path $CurrentDir "rules"

Write-Host ">> Nguồn plugins: $PluginsSource"
Write-Host ">> Đích Antigravity Plugins: $TargetPluginsDir"

if (Test-Path $PluginsSource) {
    $plugins = Get-ChildItem -Path $PluginsSource -Directory
    $count = 0
    foreach ($p in $plugins) {
        $dest = Join-Path $TargetPluginsDir $p.Name
        Copy-Item -Path $p.FullName -Destination $dest -Recurse -Force
        $count++
    }
    Write-Host ">> Đã đồng bộ thành công $count plugins sang Google Antigravity!" -ForegroundColor Green
}

# Cập nhật AGENTS.md vào antigravity-kit-plugin/rules
$agKitRules = "$TargetPluginsDir\antigravity-kit-plugin\rules"
if (Test-Path $agKitRules) {
    Copy-Item -Path "$RulesSource\AGENTS.md" -Destination "$agKitRules\AGENTS.md" -Force
    Copy-Item -Path "$RulesSource\SOUL.md" -Destination "$agKitRules\SOUL.md" -Force
    Write-Host ">> Đã cập nhật rules AGENTS.md & SOUL.md vào Antigravity Kit!" -ForegroundColor Yellow
}

Write-Host " Hoàn tất cấu hình Google Antigravity!" -ForegroundColor Cyan
