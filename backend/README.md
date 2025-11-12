Backend for FitLab

This folder contains a minimal Flask-based backend that exposes:

- GET / -> health/status
- GET /health -> model/scaler/encoder load status
- POST /predict -> accepts JSON with top-20 features and returns a predicted workout type
- GET /workouts -> sample workout list (stub)
- GET /meals -> sample meal list (stub)

Notes
- The model and related files are expected in the repository `AI/` folder:
  - `AI/workout_model_top20_tuned.pkl`
  - `AI/top20_scaler.pkl` or `AI/full_dataset_scaler.pkl`
  - `AI/target_label_encoder.pkl`

Running locally (Windows, cmd.exe)

1. Create and activate a virtual environment (recommended):

    python -m venv .venv
    .venv\Scripts\activate

2. Install requirements:

    pip install -r requirements.txt

3. Run the app:

    python app.py

The Flask app will listen on port 5000 by default. The React frontend expects the backend at http://localhost:5000 unless `REACT_APP_API_URL` is set in the frontend environment.
