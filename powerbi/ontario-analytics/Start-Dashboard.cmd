@echo off
cd /d "%~dp0"
python serve.py
if errorlevel 1 (
  echo Install dependencies first: python -m pip install -r requirements.txt
  pause
)
