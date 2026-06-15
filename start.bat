@echo off
cd /d "%~dp0"

echo Configurando _pth...

(
echo python314.zip
echo.
echo Lib\site-packages
echo import site
) > python314._pth

echo _pth configurado correctamente

echo.
echo Ejecutando bootstrap...

python.exe bootstrap.py

echo.
echo Proceso finalizado
pause