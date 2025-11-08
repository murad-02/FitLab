import React, { useState } from 'react';
import './WorkoutPredictionForm.css';

const WorkoutPredictionForm = ({ onSubmit, onReset, loading }) => {
  const [formData, setFormData] = useState({
    'Calories_Burned': '',
    'cal_balance': '',
    'Session_Duration (hours)': '',
    'expected_burn': '',
    'Experience_Level': '',
    'Weight (kg)': '',
    'Calories': '',
    'Workout_Frequency (days/week)': '',
    'lean_mass_kg': '',
    'Water_Intake (liters)': '',
    'BMI': '',
    'BMI_calc': '',
    'protein_per_kg': '',
    'Burns Calories (per 30 min)_bc': '',
    'Burns Calories (per 30 min)': '',
    'cook_time_min': '',
    'cholesterol_mg': '',
    'sodium_mg': '',
    'Fat_Percentage': '',
    'serving_size_g': ''
  });

  const [errors, setErrors] = useState({});

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
    // Clear error for this field
    if (errors[name]) {
      setErrors(prev => ({
        ...prev,
        [name]: ''
      }));
    }
  };

  const validateForm = () => {
    const newErrors = {};
    
    Object.keys(formData).forEach(key => {
      if (!formData[key] || formData[key] === '') {
        newErrors[key] = 'This field is required';
      } else {
        const value = parseFloat(formData[key]);
        if (isNaN(value)) {
          newErrors[key] = 'Please enter a valid number';
        }
      }
    });

    // Specific validations
    if (formData['Experience_Level']) {
      const expLevel = parseFloat(formData['Experience_Level']);
      if (expLevel < 1 || expLevel > 3) {
        newErrors['Experience_Level'] = 'Experience level must be between 1 and 3';
      }
    }

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (validateForm()) {
      // Convert all values to numbers
      const numericData = {};
      Object.keys(formData).forEach(key => {
        numericData[key] = parseFloat(formData[key]);
      });
      onSubmit(numericData);
    }
  };

  const handleReset = () => {
    setFormData({
      'Calories_Burned': '',
      'cal_balance': '',
      'Session_Duration (hours)': '',
      'expected_burn': '',
      'Experience_Level': '',
      'Weight (kg)': '',
      'Calories': '',
      'Workout_Frequency (days/week)': '',
      'lean_mass_kg': '',
      'Water_Intake (liters)': '',
      'BMI': '',
      'BMI_calc': '',
      'protein_per_kg': '',
      'Burns Calories (per 30 min)_bc': '',
      'Burns Calories (per 30 min)': '',
      'cook_time_min': '',
      'cholesterol_mg': '',
      'sodium_mg': '',
      'Fat_Percentage': '',
      'serving_size_g': ''
    });
    setErrors({});
    onReset();
  };

  const renderInput = (key, label, type = 'number', placeholder = '', helpText = '') => {
    return (
      <div className="form-group">
        <label htmlFor={key}>
          {label} <span className="required">*</span>
        </label>
        <input
          type={type}
          id={key}
          name={key}
          value={formData[key]}
          onChange={handleChange}
          placeholder={placeholder}
          step="0.01"
          className={errors[key] ? 'error' : ''}
          disabled={loading}
        />
        {helpText && <small className="help-text">{helpText}</small>}
        {errors[key] && <span className="error-message">{errors[key]}</span>}
      </div>
    );
  };

  return (
    <div className="prediction-form-container">
      <form onSubmit={handleSubmit} className="prediction-form">
        {/* Basic Information Section */}
        <div className="form-section">
          <h2>Basic Information</h2>
          <div className="form-grid">
            {renderInput('Weight (kg)', 'Weight (kg)', 'number', 'e.g., 70.5')}
            {renderInput('BMI', 'BMI (Body Mass Index)', 'number', 'e.g., 22.5')}
            {renderInput('BMI_calc', 'BMI (Calculated)', 'number', 'e.g., 22.5')}
            {renderInput('Fat_Percentage', 'Fat Percentage (%)', 'number', 'e.g., 15.0')}
            {renderInput('lean_mass_kg', 'Lean Mass (kg)', 'number', 'e.g., 60.0')}
          </div>
        </div>

        {/* Workout & Exercise Data Section */}
        <div className="form-section">
          <h2>Workout & Exercise Data</h2>
          <div className="form-grid">
            {renderInput('Calories_Burned', 'Calories Burned', 'number', 'e.g., 500')}
            {renderInput('Session_Duration (hours)', 'Session Duration (hours)', 'number', 'e.g., 1.5')}
            {renderInput('Workout_Frequency (days/week)', 'Workout Frequency (days/week)', 'number', 'e.g., 4')}
            {renderInput('Experience_Level', 'Experience Level (1-3)', 'number', '1 = Beginner, 2 = Intermediate, 3 = Advanced', '1 = Beginner, 2 = Intermediate, 3 = Advanced')}
            {renderInput('Burns Calories (per 30 min)', 'Calories Burned (per 30 min)', 'number', 'e.g., 200')}
            {renderInput('Burns Calories (per 30 min)_bc', 'Calories Burned (per 30 min)_bc', 'number', 'e.g., 200')}
            {renderInput('expected_burn', 'Expected Burn', 'number', 'e.g., 450')}
          </div>
        </div>

        {/* Nutrition & Diet Section */}
        <div className="form-section">
          <h2>Nutrition & Diet</h2>
          <div className="form-grid">
            {renderInput('Calories', 'Daily Calories', 'number', 'e.g., 2000')}
            {renderInput('protein_per_kg', 'Protein per kg (g/kg)', 'number', 'e.g., 2.0')}
            {renderInput('cholesterol_mg', 'Cholesterol (mg)', 'number', 'e.g., 200')}
            {renderInput('sodium_mg', 'Sodium (mg)', 'number', 'e.g., 2300')}
            {renderInput('serving_size_g', 'Serving Size (g)', 'number', 'e.g., 100')}
            {renderInput('cook_time_min', 'Cook Time (minutes)', 'number', 'e.g., 30')}
          </div>
        </div>

        {/* Advanced Metrics Section */}
        <div className="form-section">
          <h2>Advanced Metrics</h2>
          <div className="form-grid">
            {renderInput('cal_balance', 'Calorie Balance', 'number', 'e.g., 500', 'Calories consumed - Calories burned')}
            {renderInput('Water_Intake (liters)', 'Water Intake (liters)', 'number', 'e.g., 2.5')}
          </div>
        </div>

        {/* Form Actions */}
        <div className="form-actions">
          <button 
            type="submit" 
            className="btn-primary"
            disabled={loading}
          >
            {loading ? 'Predicting...' : 'Predict Workout Type'}
          </button>
          <button 
            type="button" 
            className="btn-secondary"
            onClick={handleReset}
            disabled={loading}
          >
            Reset Form
          </button>
        </div>
      </form>
    </div>
  );
};

export default WorkoutPredictionForm;

