import subprocess
import sys
import importlib.util
import os

def installed(module):
    return importlib.util.find_spec(module) is not None

def pip_install(pkg):
    subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])

if not installed("pip"):
    subprocess.check_call([sys.executable, "get-pip.py"])

required = ["argostranslate", "fastapi", "uvicorn"]

for pkg in required:
    if not installed(pkg):
        pip_install(pkg)

# modelo solo una vez
flag = "models_installed.flag"

if not os.path.exists(flag):
    subprocess.check_call([sys.executable, "install_models.py"])
    open(flag, "w").write("ok")

try:
    subprocess.check_call([
        sys.executable,
        "-m",
        "uvicorn",
        "app:app",
        "--host",
        "127.0.0.1",
        "--port",
        "8000"
    ])
except KeyboardInterrupt:
    print("\nServidor detenido manualmente.")