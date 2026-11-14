@echo off
REM Doble clic para abrir tu Panel en vivo (con subida de archivos).
REM Copia este archivo dentro de la carpeta Panel\ (junto a index.html y servidor.py).
cd /d "%~dp0"
title Panel en vivo - Fabrica de Marketing con IA
where python >nul 2>&1
if %errorlevel%==0 goto usar_python
where py >nul 2>&1
if %errorlevel%==0 goto usar_py
echo No encuentro Python. Abre Panel\index.html con doble clic para ver el Panel sin subida de archivos,
echo o pidele a Claude que instale Python.
pause
goto :eof
:usar_python
python servidor.py
goto :eof
:usar_py
py -3 servidor.py
