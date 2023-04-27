@echo off

call env\Scripts\activate
python src\main.py
call env\Scripts\deactivate
pause
