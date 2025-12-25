from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Model files are stored in the repository's AI/ folder
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'AI'))
MODEL_PATH = os.path.join(BASE_DIR, 'workout_model_top20_tuned.pkl')
SCALER_PATH_TOP20 = os.path.join(BASE_DIR, 'top20_scaler.pkl')
SCALER_PATH_FULL = os.path.join(BASE_DIR, 'full_dataset_scaler.pkl')
LABEL_ENCODER_PATH = os.path.join(BASE_DIR, 'target_label_encoder.pkl')

# Load model, scaler, and label encoder
model = None
scaler = None
label_encoder = None

try:
    print(f"Loading model from: {MODEL_PATH}")
    if os.path.exists(MODEL_PATH):
        model = joblib.load(MODEL_PATH)
        print("✓ Model loaded successfully.")
    else:
        print(f"✗ Model file not found at {MODEL_PATH}")

    print(f"Loading scaler...")
    if os.path.exists(SCALER_PATH_TOP20):
        scaler = joblib.load(SCALER_PATH_TOP20)
        print("✓ Using top20_scaler.pkl (optimized for 20 features)")
    elif os.path.exists(SCALER_PATH_FULL):
        scaler = joblib.load(SCALER_PATH_FULL)
        print("⚠ Using full_dataset_scaler.pkl as fallback. Note: This may cause errors if feature dimensions don't match.")
    else:
        print("✗ No scaler file found in AI folder. Please run AI/Test/create_scaler.py")

    if os.path.exists(LABEL_ENCODER_PATH):
        label_encoder = joblib.load(LABEL_ENCODER_PATH)
        print("✓ Label encoder loaded successfully.")
    else:
        print(f"✗ Label encoder not found at {LABEL_ENCODER_PATH}")

    print("Backend initialization complete.")
except Exception as e:
    print(f"Critical error during model initialization: {e}")
    model = None
    scaler = None
    label_encoder = None

TOP_20_FEATURES = [
    'Calories_Burned',
    'cal_balance',
    'Session_Duration (hours)',
    'expected_burn',
    'Experience_Level',
    'Weight (kg)',
    'Calories',
    'Workout_Frequency (days/week)',
    'lean_mass_kg',
    'Water_Intake (liters)',
    'BMI',
    'BMI_calc',
    'protein_per_kg',
    'Burns Calories (per 30 min)_bc',
    'Burns Calories (per 30 min)',
    'cook_time_min',
    'cholesterol_mg',
    'sodium_mg',
    'Fat_Percentage',
    'serving_size_g'
]

@app.route('/')
def index():
    return jsonify({'status': 'ok', 'message': 'FitLab backend running'})

@app.route('/health')
def health():
    status = {
        'model_loaded': model is not None,
        'scaler_loaded': scaler is not None,
        'label_encoder_loaded': label_encoder is not None
    }
    return jsonify(status)

@app.route('/predict', methods=['POST'])
def predict():
    if model is None or scaler is None or label_encoder is None:
        return jsonify({'error': 'Model/scaler/encoder not loaded. See backend logs.'}), 500
    try:
        data = request.get_json()
        feature_values = []
        for feature in TOP_20_FEATURES:
            value = data.get(feature, 0)
            try:
                feature_values.append(float(value))
            except (ValueError, TypeError):
                return jsonify({'error': f'Invalid value for {feature}'}), 400

        features_array = np.array(feature_values).reshape(1, -1)
        
        try:
            features_scaled = scaler.transform(features_array)
        except ValueError as ve:
            if "n_features" in str(ve) or "X has" in str(ve):
                return jsonify({
                    'error': 'Scaler dimension mismatch. The loaded scaler expects more features than provided. ' +
                             'Please run AI/Test/create_scaler.py to generate the correct top20_scaler.pkl.'
                }), 500
            raise ve

        prediction = model.predict(features_scaled)[0]
        probabilities = model.predict_proba(features_scaled)[0]

        workout_type = label_encoder.inverse_transform([prediction])[0]
        workout_probs = {}
        for i, class_name in enumerate(label_encoder.classes_):
            workout_probs[class_name] = float(probabilities[i] * 100)

        return jsonify({
            'prediction': workout_type,
            'probabilities': workout_probs,
            'confidence': float(max(probabilities) * 100)
        })
    except Exception as e:
        return jsonify({'error': f'Prediction error: {str(e)}'}), 500

# Example lightweight endpoints for workouts and meals (stub data)
@app.route('/workouts', methods=['GET'])
def get_workouts():
    # In a full implementation, this would query a DB
    sample = [
        {'id': 1, 'name': 'Full Body Beginner', 'duration_min': 45, 'difficulty': 'Beginner'},
        {'id': 2, 'name': 'HIIT Advanced', 'duration_min': 30, 'difficulty': 'Advanced'}
    ]
    return jsonify(sample)

@app.route('/meals', methods=['GET'])
def get_meals():
    sample = [
        {'id': 1, 'name': 'Chicken Salad', 'calories': 400},
        {'id': 2, 'name': 'Oatmeal and Fruit', 'calories': 350}
    ]
    return jsonify(sample)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
