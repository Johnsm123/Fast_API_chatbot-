@echo off
echo Activating virtual environment...
call .venv\Scripts\activate.bat

echo Starting FastAPI application...
cd "Project Fast API"
python -m uvicorn main:app --reload

pause