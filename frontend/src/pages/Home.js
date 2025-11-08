import React, { useState } from 'react';
import WorkoutPredictionForm from '../components/WorkoutPredictionForm';
import PredictionResults from '../components/PredictionResults';
import { predictWorkout } from '../services/api';
import './Home.css';

const Home = () => {
  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handlePredict = async (formData) => {
    setLoading(true);
    setError(null);
    setPrediction(null);

    try {
      const result = await predictWorkout(formData);
      setPrediction(result);
    } catch (err) {
      setError(err.message || 'An error occurred while predicting workout type');
    } finally {
      setLoading(false);
    }
  };

  const handleReset = () => {
    setPrediction(null);
    setError(null);
  };

  return (
    <div className="home-container">
      <div className="content-wrapper">
        <div className="intro-section">
          <h2>Predict Your Optimal Workout Type</h2>
          <p>
            Enter your fitness data below and let our AI model predict the best workout type for you
            based on your physical metrics, exercise history, and nutritional data.
          </p>
        </div>

        <WorkoutPredictionForm 
          onSubmit={handlePredict} 
          onReset={handleReset}
          loading={loading}
        />

        {error && (
          <div className="error-message">
            <span>⚠️</span>
            <p>{error}</p>
          </div>
        )}

        {prediction && (
          <PredictionResults prediction={prediction} />
        )}
      </div>
    </div>
  );
};

export default Home;

