# Fábrica de Marketing con IA — instalador para Windows
# Uso normal:   clic derecho -> "Ejecutar con PowerShell"
# Elegir niveles:   powershell -ExecutionPolicy Bypass -File instalar.ps1 -Modulos base,anuncios
# Probar sin tocar tu equipo:   .\instalar.ps1 -Destino C:\ruta\de\prueba
# Niveles: base | anuncios | video   (por defecto: los tres)
param(
    [string]$Destino = "",
    [string[]]$Modulos = @("base", "anuncios", "video")
)
$ErrorActionPreference = "Stop"
$aqui = Split-Path -Parent $MyInvocation.MyCommand.Path
$Modulos = @($Modulos | ForEach-Object { $_ -split "," } | ForEach-Object { $_.Trim().ToLower() } | Where-Object { $_ })
$modoPrueba = $PSBoundParameters.ContainsKey("Destino")
if (-not $Destino) { $Destino = Join-Path $env:USERPROFILE ".claude" }
$dSkills = Join-Path $Destino "skills"
$dAgentes = Join-Path $Destino "agents"
$version = (Get-Content (Join-Path $aqui "VERSION") -ErrorAction SilentlyContinue | Select-Object -First 1)

Write-Host ""
Write-Host "Fábrica de Marketing con IA $version" -ForegroundColor Cyan
Write-Host "Niveles a instalar: $($Modulos -join ', ')"
Write-Host "Skills en:  $dSkills"
Write-Host "Agentes en: $dAgentes"
Write-Host ""

foreach ($m in $Modulos) {
    if (-not (Test-Path (Join-Path $aqui "modulos\$m\skills"))) {
        Write-Host "No existe el nivel '$m'. Usa: base, anuncios o video." -ForegroundColor Red
        exit 1
    }
}
if ($Modulos -notcontains "base") {
    Write-Host "Aviso: sin el nivel 'base' no hay director ni panel. Se recomienda incluirlo." -ForegroundColor Yellow
}

New-Item -ItemType Directory -Force $dSkills | Out-Null
New-Item -ItemType Directory -Force $dAgentes | Out-Null
$stamp = Get-Date -Format "yyyyMMdd-HHmmss"
$respaldoRaiz = Join-Path $Destino "respaldo-fabrica-marketing"
$nSkills = 0; $nResp = 0

function Copiar-Con-Respaldo($origen, $destino, $nombre, $tipo) {
    if (Test-Path $destino) {
        $bakDir = Join-Path $respaldoRaiz $stamp
        New-Item -ItemType Directory -Force $bakDir | Out-Null
        Move-Item $destino (Join-Path $bakDir "$tipo-$nombre")
        $script:nResp++
        Write-Host "  Ya tenías '$nombre': la versión anterior quedó en $bakDir" -ForegroundColor Yellow
    }
    Copy-Item $origen $destino -Recurse -Force
}

foreach ($m in $Modulos) {
    Write-Host "Nivel $m" -ForegroundColor Green
    foreach ($d in Get-ChildItem (Join-Path $aqui "modulos\$m\skills") -Directory) {
        Copiar-Con-Respaldo $d.FullName (Join-Path $dSkills $d.Name) $d.Name "skill"
        $nSkills++
        Write-Host "  ✔ $($d.Name)"
    }
    # ejemplos del nivel video (van dentro de la skill fabrica-de-video)
    $ej = Join-Path $aqui "modulos\$m\ejemplos"
    if ((Test-Path $ej) -and (Test-Path (Join-Path $dSkills "fabrica-de-video"))) {
        Copy-Item $ej (Join-Path $dSkills "fabrica-de-video\ejemplos") -Recurse -Force
    }
}

$nAg = 0
if ($Modulos -contains "base") {
    Write-Host "Agentes del equipo" -ForegroundColor Green
    foreach ($f in Get-ChildItem (Join-Path $aqui "agentes") -Filter "fm-agente-*.md") {
        $dest = Join-Path $dAgentes $f.Name
        if (Test-Path $dest) {
            $bakDir = Join-Path $respaldoRaiz $stamp
            New-Item -ItemType Directory -Force $bakDir | Out-Null
            Move-Item $dest (Join-Path $bakDir ("agente-" + $f.Name))
            $nResp++
        }
        Copy-Item $f.FullName $dest -Force
        $nAg++
        Write-Host "  ✔ $($f.BaseName)"
    }
}

# Registro de la versión instalada (lo usa la skill fm-actualizar para avisar de novedades)
$info = @{ version = "$version"; modulos = @($Modulos); fecha = (Get-Date -Format "yyyy-MM-dd") } | ConvertTo-Json -Compress
Set-Content -Path (Join-Path $Destino "fabrica-de-marketing-ia.version.json") -Value $info -Encoding UTF8
Write-Host ""
Write-Host "Listo: $nSkills skills y $nAg agentes instalados ($nResp respaldados)." -ForegroundColor Green
Write-Host ""
Write-Host "Siguiente paso:"
Write-Host "  1. Cierra y vuelve a abrir Claude (para que cargue las skills y los agentes)."
Write-Host "  2. Crea una carpeta 'Mi Fábrica de Marketing' en Documentos y abre Claude dentro."
Write-Host "  3. Escribe:  Quiero empezar"
Write-Host ""
Write-Host "Guía paso a paso: ver README.md"
if ($Modulos -contains "video") {
    Write-Host "Nivel Video: la primera vez, la Fábrica de Video revisará tu equipo (ffmpeg, Node, Python, Whisper) y te pedirá permiso antes de instalar algo."
}
if ($Host.Name -eq "ConsoleHost" -and -not $modoPrueba) { Read-Host "Pulsa Enter para cerrar" | Out-Null }
