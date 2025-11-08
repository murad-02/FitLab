# FitLab Frontend - Quick Start Guide

## 🚀 Getting Started

### Prerequisites
- Node.js (v14 or higher) and npm
- Flask backend running on port 5000

### Installation Steps

1. **Navigate to frontend directory:**
```bash
cd frontend
```

2. **Install dependencies:**
```bash
npm install
```

3. **Create environment file:**
Create a `.env` file in the `frontend` directory:
```env
REACT_APP_API_URL=http://localhost:5000
```

4. **Start the development server:**
```bash
npm start
```

The application will open at `http://localhost:3000` in your browser.

## 📁 Project Structure

```
frontend/
├── public/
│   └── index.html          # HTML template
├── src/
│   ├── components/         # React components
│   │   ├── Header.js       # App header
│   │   ├── WorkoutPredictionForm.js  # Input form
│   │   └── PredictionResults.js      # Results display
│   ├── pages/
│   │   └── Home.js         # Main page
│   ├── services/
│   │   └── api.js          # API service
│   ├── App.js              # Root component
│   └── index.js            # Entry point
├── package.json
└── README.md
```

## 🔧 Backend Setup

Before running the frontend, ensure the Flask backend is running:

1. **Navigate to backend directory:**
```bash
cd AI/Test
```

2. **Install Python dependencies:**
```bash
pip install -r requirements.txt
```

3. **Start Flask server:**
```bash
python app.py
```

The backend should be running on `http://localhost:5000`.

## ✨ Features

- ✅ **Workout Prediction Form**: 20 input fields organized into sections
- ✅ **Real-time Validation**: Client-side form validation
- ✅ **Results Visualization**: Probability distribution with visual bars
- ✅ **Responsive Design**: Mobile-friendly interface
- ✅ **Error Handling**: User-friendly error messages
- ✅ **Loading States**: Visual feedback during API calls

## 🎨 UI Features

- Modern gradient design
- Smooth animations and transitions
- Color-coded confidence scores
- Interactive probability bars
- Responsive grid layout

## 🔌 API Integration

The frontend communicates with the Flask backend via:
- **Endpoint**: `POST /predict`
- **Request**: JSON with 20 feature values
- **Response**: Prediction, confidence, and probabilities

## 🐛 Troubleshooting

### Port already in use
```bash
PORT=3001 npm start
```

### Backend connection issues
1. Verify backend is running: `curl http://localhost:5000/predict`
2. Check `.env` file has correct API URL
3. Ensure CORS is enabled in Flask backend

### Build errors
```bash
rm -rf node_modules package-lock.json
npm install
```

## 📦 Production Build

```bash
npm run build
```

This creates an optimized production build in the `build` directory.

## 📚 Documentation

- **README.md**: Comprehensive documentation
- **SETUP.md**: Detailed setup instructions
- **ARCHITECTURE.md**: Architecture and design patterns

## 🎯 Next Steps

1. Start both backend and frontend servers
2. Open `http://localhost:3000` in your browser
3. Fill in the workout prediction form
4. View your predicted workout type and probabilities

## 💡 Tips

- All form fields are required
- Experience Level must be between 1-3
- Use decimal values for precise measurements
- Check the browser console for debugging information

---

For more detailed information, see the `frontend/README.md` file.

