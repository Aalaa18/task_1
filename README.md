# Weather CLI

Small Python program that calls the OpenWeatherMap API, parses the JSON into a class, and prints a summary.

## Setup
```
python -m venv venv
venv\Scripts\Activate.ps1      # Mac/Linux: source venv/bin/activate
pip install -r requirements.txt
```
Create a `.env` file (see `.env.example`) containing:
```
OPENWEATHER_API_KEY=your_key_here
```

## Run
```
python simple.py
```

## Test
```
pip install -r requirements-dev.txt
pytest -v
```
