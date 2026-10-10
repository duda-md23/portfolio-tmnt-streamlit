@echo off
title Portfolio Maria Eduarda - Streamlit Local
echo ========================================================
echo Iniciando Portfolio TMNT Data/Cyber Lab (Streamlit)
echo ========================================================
cd /d "%~dp0"

IF EXIST "venv\Scripts\activate.bat" (
    echo [OK] Ativando ambiente virtual...
    call venv\Scripts\activate.bat
) ELSE (
    echo [AVISO] Ambiente virtual nao encontrado. Usando Python global...
)

echo [OK] Abrindo aplicacao no navegador...
python -m streamlit run app.py
pause