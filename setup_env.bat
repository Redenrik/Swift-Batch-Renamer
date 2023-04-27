@echo off

echo Setting up the virtual environment...
python -m venv env

echo Installing dependencies...
env\Scripts\activate
pip install -r requirements.txt
env\Scripts\deactivate

echo Setup complete!