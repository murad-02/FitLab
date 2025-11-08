# FitLab Frontend Setup Guide

## Quick Start

### 1. Install Dependencies

```bash
cd frontend
npm install
```

### 2. Configure Environment

Create a `.env` file in the `frontend` directory:

```env
REACT_APP_API_URL=http://localhost:5000
```

### 3. Start the Development Server

```bash
npm start
```

The application will open at `http://localhost:3000`.

## Prerequisites

- **Node.js**: Version 14 or higher
- **npm**: Version 6 or higher (comes with Node.js)
- **Backend**: Flask backend must be running on port 5000

## Backend Setup

Before running the frontend, ensure the Flask backend is set up:

1. Navigate to the backend directory:
```bash
cd ../AI/Test
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Start the Flask server:
```bash
python app.py
```

The backend should be running on `http://localhost:5000`.

## Troubleshooting

### Port Already in Use

If port 3000 is already in use, React will prompt you to use a different port. You can also specify a port:

```bash
PORT=3001 npm start
```

### Backend Connection Issues

If you see "Unable to connect to the server":

1. Verify the backend is running:
```bash
curl http://localhost:5000/predict
```

2. Check the `.env` file has the correct API URL

3. Ensure CORS is enabled in the Flask backend (should be done automatically with flask-cors)

### Build Errors

If you encounter build errors:

1. Clear node_modules and reinstall:
```bash
rm -rf node_modules package-lock.json
npm install
```

2. Clear npm cache:
```bash
npm cache clean --force
```

## Production Build

To create a production build:

```bash
npm run build
```

This creates an optimized build in the `build` directory that can be served by any static file server.

## Project Structure

```
frontend/
├── public/                 # Static files
│   └── index.html
├── src/
│   ├── components/         # React components
│   │   ├── Header.js
│   │   ├── WorkoutPredictionForm.js
│   │   └── PredictionResults.js
│   ├── pages/              # Page components
│   │   └── Home.js
│   ├── services/           # API services
│   │   └── api.js
│   ├── App.js              # Main app component
│   └── index.js            # Entry point
├── package.json
└── README.md
```

## Development Notes

- The frontend uses React Router for navigation (currently just one route)
- All API calls are centralized in `src/services/api.js`
- Form validation is handled client-side before API calls
- Error handling includes user-friendly messages
- The UI is fully responsive and mobile-friendly

## Next Steps

- Add more routes/pages if needed
- Implement user authentication if required
- Add data visualization charts
- Implement workout history tracking
- Add user profiles and saved predictions

