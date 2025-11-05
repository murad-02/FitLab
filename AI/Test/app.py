from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import os

app = Flask(__name__)

# Load the model and related files
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'workout_model_top20_tuned.pkl')
# Try to use top20_scaler.pkl first, fallback to full_dataset_scaler.pkl
SCALER_PATH_TOP20 = os.path.join(os.path.dirname(__file__), 'top20_scaler.pkl')
SCALER_PATH_FULL = os.path.join(BASE_DIR, 'full_dataset_scaler.pkl')
LABEL_ENCODER_PATH = os.path.join(BASE_DIR, 'target_label_encoder.pkl')

# Load model, scaler, and label encoder
try:
    model = joblib.load(MODEL_PATH)
    
    # Try to load top20_scaler first, fallback to full scaler
    if os.path.exists(SCALER_PATH_TOP20):
        scaler = joblib.load(SCALER_PATH_TOP20)
        print("Using top20_scaler.pkl")
    else:
        scaler = joblib.load(SCALER_PATH_FULL)
        print("Warning: Using full_dataset_scaler.pkl. Consider running create_scaler.py to create top20_scaler.pkl")
    
    label_encoder = joblib.load(LABEL_ENCODER_PATH)
    print("Model, scaler, and label encoder loaded successfully!")
except Exception as e:
    print(f"Error loading files: {e}")
    model = None
    scaler = None
    label_encoder = None

# Top 20 features in order (from notebook Cell 56)
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
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if model is None or scaler is None or label_encoder is None:
        return jsonify({'error': 'Model not loaded. Please check the model files.'}), 500
    
    try:
        # Get form data
        data = request.get_json()
        
        # Extract features from form data
        feature_values = []
        for feature in TOP_20_FEATURES:
            value = data.get(feature, 0)
            try:
                feature_values.append(float(value))
            except (ValueError, TypeError):
                return jsonify({'error': f'Invalid value for {feature}'}), 400
        
        # Convert to numpy array and reshape
        features_array = np.array(feature_values).reshape(1, -1)
        
        # Scale the features
        features_scaled = scaler.transform(features_array)
        
        # Make prediction
        prediction = model.predict(features_scaled)[0]
        probabilities = model.predict_proba(features_scaled)[0]
        
        # Get workout type name
        workout_type = label_encoder.inverse_transform([prediction])[0]
        
        # Get probabilities for all classes
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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

