# Instala y configura claude-code-router para usar modelos gratuitos de OpenRouter.
# Uso (PowerShell, Windows):
#   .\tools\router\setup-openrouter.ps1 -ApiKey "sk-or-v1-..."

param([Parameter(Mandatory = $true)][string]$ApiKey)

Write-Host "1/3 Instalando claude-code-router..." -ForegroundColor Cyan
npm install -g @musistudio/claude-code-router
if ($LASTEXITCODE -ne 0) { throw "Fallo la instalacion. Necesitas Node.js 18+ (https://nodejs.org)" }

$dir = Join-Path $env:USERPROFILE ".claude-code-router"
New-Item -ItemType Directory -Force -Path $dir | Out-Null
$destino = Join-Path $dir "config.json"

if (Test-Path $destino) {
  $respaldo = "$destino.bak"
  Copy-Item $destino $respaldo -Force
  Write-Host "Config anterior respaldada en $respaldo" -ForegroundColor Yellow
}

Write-Host "2/3 Escribiendo $destino..." -ForegroundColor Cyan
$plantilla = Join-Path $PSScriptRoot "config.ejemplo.json"
(Get-Content $plantilla -Raw).Replace("PON_AQUI_TU_OPENROUTER_API_KEY", $ApiKey) |
  Set-Content $destino -Encoding UTF8

Write-Host "3/3 Listo." -ForegroundColor Green
Write-Host ""
Write-Host "Para trabajar GRATIS:   ccr code" -ForegroundColor Green
Write-Host "Para volver a Claude:   claude" -ForegroundColor Green
Write-Host "Cambiar de modelo dentro de la sesion:  /model openrouter,<id-del-modelo>"
