# FitLab Workout Type Predictor - Flask UI

A Flask web application for predicting workout types (Cardio, HIIT, Strength, Yoga) based on fitness and nutrition data.

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Create the scaler for top 20 features (recommended):**
   ```bash
   python create_scaler.py
   ```
   This will create `top20_scaler.pkl` which is optimized for the 20 features used by the model.

3. **Run the Flask application:**
   ```bash
   python app.py
   ```

4. **Open your browser:**
   Navigate to `http://localhost:5000`

## Features

The application predicts workout types based on 20 key features:
- Basic information (Weight, BMI, Fat Percentage)
- Workout data (Calories Burned, Session Duration, Frequency)
- Nutrition data (Calories, Protein, Cholesterol, Sodium)
- Advanced metrics (Calorie Balance, Expected Burn, Lean Mass)

## Model Files Required

The following files should be in the parent directory (`AI/`):
- `workout_model_top20_tuned.pkl` - The trained model
- `target_label_encoder.pkl` - Label encoder for workout types
- `full_dataset_scaler.pkl` - Full dataset scaler (fallback)
- `top20_scaler.pkl` - Scaler for top 20 features (created by `create_scaler.py`)

## Project Structure

```
Test/
├── app.py                 # Flask application
├── create_scaler.py       # Script to create top20 scaler
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── templates/
│   └── index.html        # Main UI template
└── static/
    └── style.css         # CSS styling
```

## Notes

- The model was trained on 20 top features selected from feature importance analysis
- Workout types: Cardio (0), HIIT (1), Strength (2), Yoga (3)
- All input fields are required for prediction

