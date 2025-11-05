"""
Script to create a scaler for only the top 20 features.
This should be run once to create the proper scaler for the Flask app.
"""
import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np

# Load the original scaler
SCALER_PATH = '../full_dataset_scaler.pkl'
DATA_PATH = '../Dataset/Final_data.csv'

# Top 20 features (must match the order in app.py)
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

try:
    # Load the dataset to get the feature scaling parameters
    print("Loading dataset...")
    df = pd.read_csv(DATA_PATH)
    
    # Apply the same preprocessing as in the notebook
    # Drop columns that were dropped
    df = df.drop(['meal_name', 'Name of Exercise', 'Benefit', 'Equipment Needed', 'Workout'], axis=1, errors='ignore')
    
    # Simplify Target Muscle Group
    if 'Target Muscle Group' in df.columns:
        df['Target Muscle Group'] = df['Target Muscle Group'].apply(lambda x: x.split(',')[0].strip() if pd.notna(x) else '')
    
    # One-hot encoding
    from sklearn.preprocessing import LabelEncoder
    one_hot_cols = ['Gender', 'Workout_Type', 'meal_type', 'diet_type', 
                    'cooking_method', 'Target Muscle Group', 'Body Part', 'Type of Muscle']
    one_hot_cols = [col for col in one_hot_cols if col in df.columns]
    df = pd.get_dummies(df, columns=one_hot_cols, drop_first=True)
    
    # Label encoding
    label_cols = ['Difficulty Level', 'Burns_Calories_Bin']
    label_cols = [col for col in label_cols if col in df.columns]
    le = LabelEncoder()
    for col in label_cols:
        if col in df.columns:
            df[col] = le.fit_transform(df[col])
    
    # Check if all top 20 features exist
    missing_features = [f for f in TOP_20_FEATURES if f not in df.columns]
    if missing_features:
        print(f"Warning: Missing features: {missing_features}")
        print("Available columns:", [col for col in df.columns if col in TOP_20_FEATURES])
        # Use only available features
        available_features = [f for f in TOP_20_FEATURES if f in df.columns]
        print(f"Using {len(available_features)} available features")
    else:
        available_features = TOP_20_FEATURES
    
    # Extract only the top 20 features
    X_top20 = df[available_features]
    
    # Create and fit scaler on top 20 features only
    print("Creating scaler for top 20 features...")
    scaler_top20 = StandardScaler()
    scaler_top20.fit(X_top20)
    
    # Save the scaler
    output_path = 'top20_scaler.pkl'
    joblib.dump(scaler_top20, output_path)
    print(f"✓ Scaler saved to {output_path}")
    print(f"✓ Scaler fitted on {len(available_features)} features")
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()

