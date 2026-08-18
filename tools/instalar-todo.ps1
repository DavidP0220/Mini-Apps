<#
  INSTALADOR TODO-EN-UNO (Windows / PowerShell)

  Hace de una sola vez todo lo que se puede automatizar:
    1. Verifica que tengas Node.js
    2. Baja los últimos cambios del repositorio
    3. Instala claude-code-router
    4. Escribe tu configuración de OpenRouter (con tu API key)
    5. Te muestra el reporte de gasto de tokens

  USO — pega esta línea en PowerShell, dentro de la carpeta del proyecto:

      .\tools\instalar-todo.ps1 -ApiKey "sk-or-v1-tu-key-aqui"

  Si todavía no tienes la key de OpenRouter, ejecútalo sin ella:

      .\tools\instalar-todo.ps1

  (hará los pasos 1, 2 y 5, y te dirá dónde conseguir la key)
#>

param([string]$ApiKey = "")

$ErrorActionPreference = "Stop"
$raiz = Split-Path -Parent $PSScriptRoot

function Paso($n, $texto) { Write-Host "`n[$n] $texto" -ForegroundColor Cyan }
function Ok($texto)       { Write-Host "    OK  $texto" -ForegroundColor Green }
function Aviso($texto)    { Write-Host "    !   $texto" -ForegroundColor Yellow }

Write-Host "=====================================" -ForegroundColor White
Write-Host " Mini-Apps - instalacion y ahorro     " -ForegroundColor White
Write-Host "=====================================" -ForegroundColor White

# ---------- 1. Node.js ----------
Paso 1 "Verificando Node.js..."
try {
  $version = (node -v).TrimStart('v')
  if ([int]($version.Split('.')[0]) -lt 18) {
    throw "Tienes Node $version. Se necesita 18 o superior."
  }
  Ok "Node $version"
} catch {
  Write-Host "`n  FALTA NODE.JS." -ForegroundColor Red
  Write-Host "  Descargalo aqui: https://nodejs.org (boton LTS)"
  Write-Host "  Instalalo, cierra esta ventana, abre PowerShell de nuevo y repite el comando."
  exit 1
}

# ---------- 2. Actualizar el repositorio ----------
Paso 2 "Bajando los ultimos cambios del repositorio..."
Push-Location $raiz
try {
  git pull 2>&1 | Out-String | Write-Host
  Ok "Repositorio actualizado"
} catch {
  Aviso "No se pudo hacer git pull. Continuo con lo demas."
} finally {
  Pop-Location
}

# ---------- 3 y 4. Router + OpenRouter ----------
if ([string]::IsNullOrWhiteSpace($ApiKey)) {
  Paso 3 "OpenRouter: pendiente (no me pasaste la API key)"
  Aviso "Para trabajar gratis necesitas una key:"
  Write-Host "      1. Entra a https://openrouter.ai y crea cuenta (boton 'Sign in')"
  Write-Host "      2. Ve a https://openrouter.ai/keys y pulsa 'Create Key'"
  Write-Host "      3. Copia la key (empieza por sk-or-v1-)"
  Write-Host "      4. Vuelve a ejecutar:"
  Write-Host "         .\tools\instalar-todo.ps1 -ApiKey `"sk-or-v1-tu-key`"" -ForegroundColor White
} else {
  Paso 3 "Instalando claude-code-router..."
  npm install -g @musistudio/claude-code-router
  if ($LASTEXITCODE -ne 0) { throw "Fallo la instalacion de claude-code-router." }
  Ok "claude-code-router instalado"

  Paso 4 "Escribiendo tu configuracion de OpenRouter..."
  $dir = Join-Path $env:USERPROFILE ".claude-code-router"
  New-Item -ItemType Directory -Force -Path $dir | Out-Null
  $destino = Join-Path $dir "config.json"
  if (Test-Path $destino) {
    Copy-Item $destino "$destino.bak" -Force
    Aviso "Config anterior respaldada en $destino.bak"
  }
  $plantilla = Join-Path $PSScriptRoot "router\config.ejemplo.json"
  (Get-Content $plantilla -Raw).Replace("PON_AQUI_TU_OPENROUTER_API_KEY", $ApiKey) |
    Set-Content $destino -Encoding UTF8
  Ok "Configuracion escrita en $destino"
}

# ---------- 5. Reporte de tokens ----------
Paso 5 "Tu consumo de tokens hasta ahora:"
Push-Location $raiz
try { node tools/token-report.mjs } catch { Aviso "No se pudo generar el reporte." }
Pop-Location

# ---------- Resumen ----------
Write-Host "`n=====================================" -ForegroundColor White
Write-Host " QUE SIGUE" -ForegroundColor White
Write-Host "=====================================" -ForegroundColor White
if (-not [string]::IsNullOrWhiteSpace($ApiKey)) {
  Write-Host " Trabajar GRATIS :  ccr code" -ForegroundColor Green
  Write-Host " Volver a Claude :  claude" -ForegroundColor Green
}
Write-Host " Crear app nueva :  node tools/new-app.mjs mi-producto --titulo `"Mi Producto`""
Write-Host " Ver el gasto    :  node tools/token-report.mjs"
Write-Host ""
Write-Host " LO UNICO QUE NO PUEDO AUTOMATIZAR (son ajustes de tu cuenta):" -ForegroundColor Yellow
Write-Host " Apagar los conectores que no usas en:"
Write-Host "   https://claude.ai/customize/connectors" -ForegroundColor White
Write-Host " Deja solo 'github'. Ahorra mas que todo lo demas junto (40-70%)."
Write-Host ""
