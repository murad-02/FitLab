# FitLab Frontend

React-based frontend application for the FitLab AI-Powered Workout Type Prediction System.

## Features

- 🎯 **Workout Type Prediction**: Input your fitness data and get AI-powered workout recommendations
- 📊 **Probability Visualization**: View detailed probability distribution for all workout types
- 🎨 **Modern UI**: Beautiful, responsive design with smooth animations
- ✅ **Form Validation**: Comprehensive client-side validation for all input fields
- 🔄 **Real-time Feedback**: Loading states and error handling

## Prerequisites

- Node.js (v14 or higher)
- npm or yarn
- Flask backend running on `http://localhost:5000`

## Installation

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

## Configuration

Create a `.env` file in the frontend directory to configure the API URL:

```env
REACT_APP_API_URL=http://localhost:5000
```

If not specified, it defaults to `http://localhost:5000`.

## Running the Applications

### Development Mode

```bash
npm start
```

The application will open at `http://localhost:3000` in your browser.

### Production Build

```bash
npm run build
```

This creates an optimized production build in the `build` directory.

## Project Structure

```
frontend/
├── public/
│   └── index.html
├── src/
│   ├── components/
│   │   ├── Header.js
│   │   ├── Header.css
│   │   ├── WorkoutPredictionForm.js
│   │   ├── WorkoutPredictionForm.css
│   │   ├── PredictionResults.js
│   │   └── PredictionResults.css
│   ├── pages/
│   │   ├── Home.js
│   │   └── Home.css
│   ├── services/
│   │   └── api.js
│   ├── App.js
│   ├── App.css
│   ├── index.js
│   └── index.css
├── package.json
└── README.md
```

## Components

### Header
Displays the application title and description.

### WorkoutPredictionForm
Form component with 20 input fields organized into sections:
- Basic Information (Weight, BMI, Fat Percentage, etc.)
- Workout & Exercise Data (Calories Burned, Session Duration, etc.)
- Nutrition & Diet (Daily Calories, Protein, etc.)
- Advanced Metrics (Calorie Balance, Water Intake)

### PredictionResults
Displays the predicted workout type with:
- Confidence score
- Probability distribution for all workout types
- Visual probability bars

## API Integration

The frontend communicates with the Flask backend via the `/predict` endpoint:

**Endpoint:** `POST /predict`

**Request Body:**
```json
{
  "Calories_Burned": 500,
  "cal_balance": 200,
  "Session_Duration (hours)": 1.5,
  ...
}
```

**Response:**
```json
{
  "prediction": "Cardio",
  "confidence": 85.5,
  "probabilities": {
    "Cardio": 85.5,
    "Strength": 10.2,
    ...
  }
}
```

## Features in Detail

### Form Validation
- All fields are required
- Numeric validation for all inputs
- Experience Level validation (1-3 range)
- Real-time error display

### Responsive Design
- Mobile-friendly layout
- Adaptive grid system
- Touch-friendly buttons
- Optimized for all screen sizes

### User Experience
- Loading states during API calls
- Error messages with helpful feedback
- Smooth animations and transitions
- Clear visual hierarchy

## Development

### Adding New Features

1. Create new components in `src/components/`
2. Add routes in `src/App.js` if needed
3. Update API service in `src/services/api.js` for new endpoints
4. Add styling in component-specific CSS files

### Testing

```bash
npm test
```

## Troubleshooting

### Backend Connection Issues

If you see "Unable to connect to the server":
1. Ensure the Flask backend is running on port 5000
2. Check the `REACT_APP_API_URL` in your `.env` file
3. Verify CORS is enabled on the backend

### Build Issues

If you encounter build errors:
1. Delete `node_modules` and `package-lock.json`
2. Run `npm install` again
3. Clear npm cache: `npm cache clean --force`

## License

This project is part of the FitLab system.

