# Bootstrap para inicialização local
# Use: bash bootstrap.sh ou ./bootstrap.ps1
python -m venv .venv
source .venv/bin/activate || .venv\Scripts\Activate.ps1
pip install -r requirements.txt
