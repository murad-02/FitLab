import React from 'react';
import './PredictionResults.css';

const PredictionResults = ({ prediction }) => {
  const { prediction: workoutType, probabilities, confidence } = prediction;

  // Sort probabilities by value (descending)
  const sortedProbabilities = Object.entries(probabilities)
    .sort((a, b) => b[1] - a[1]);

  const getConfidenceColor = (conf) => {
    if (conf >= 80) return '#28a745';
    if (conf >= 60) return '#ffc107';
    return '#dc3545';
  };

  return (
    <div className="prediction-results-container">
      <div className="prediction-card">
        <div className="prediction-header">
          <div className="prediction-title">
            <h3>Recommended Workout Type</h3>
            <h2 className="workout-type">{workoutType}</h2>
          </div>
          <div 
            className="confidence-badge"
            style={{ backgroundColor: getConfidenceColor(confidence) }}
          >
            <span className="confidence-value">{confidence.toFixed(2)}%</span>
            <span className="confidence-label">Confidence</span>
          </div>
        </div>

        <div className="probabilities-section">
          <h4>Probability Distribution</h4>
          <p className="probabilities-description">
            Below are the probabilities for all possible workout types:
          </p>
          <div className="prob-bars">
            {sortedProbabilities.map(([workout, prob]) => (
              <div key={workout} className="prob-bar-container">
                <div className="prob-bar-label">
                  <span className="workout-name">{workout}</span>
                  <span className="prob-value">{prob.toFixed(2)}%</span>
                </div>
                <div className="prob-bar">
                  <div 
                    className="prob-bar-fill" 
                    style={{ 
                      width: `${prob}%`,
                      backgroundColor: workout === workoutType 
                        ? '#667eea' 
                        : '#764ba2'
                    }}
                  />
                </div>
              </div>
            ))}
          </div>
        </div>

        <div className="prediction-footer">
          <p>
            <strong>Note:</strong> This prediction is based on machine learning analysis of your input data. 
            Consult with a fitness professional for personalized advice.
          </p>
        </div>
      </div>
    </div>
  );
};

export default PredictionResults;

