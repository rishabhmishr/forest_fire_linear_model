# 🔥 Forest Fire Prediction System

A machine learning-based web application to predict the area of forest that may be burned based on weather conditions and Fire Weather Index (FWI) components.

## 📋 Project Overview

This project uses a **Linear Regression model** trained on the Algerian Forest Fires dataset to predict burned area (in hectares) given:
- Weather conditions (Temperature, Humidity, Wind Speed, Rain)
- Fire Weather Index (FWI) components (FFMC, DMC, DC, ISI)
- Fire classification status (Fire/Not Fire)

The application is built with **Flask** for the backend and includes a user-friendly web interface for making predictions.

## 🎯 Features

- ✅ **Interactive Web UI** — Clean, responsive form to input prediction parameters
- ✅ **Real-time Predictions** — Instant prediction results displayed on the same page
- ✅ **Pre-trained Model** — Linear Regression model trained and optimized
- ✅ **Data Standardization** — Input data scaled using StandardScaler for consistency
- ✅ **Mobile-Friendly** — Works on desktop and mobile devices
- ✅ **Error Handling** — Robust exception handling with detailed logging

## 📁 Project Structure

```
forest_fire_implementation/
├── application.py                 # Flask application & routes
├── README.md                       # This file
├── requirement.txt                 # Python dependencies
├── Models/
│   ├── Forest_Fire_Linrear_Regression.pkl    # Trained model
│   └── Forest_Fire_scaler.pkl                 # StandardScaler
├── Notebook/
│   ├── regression_complete.ipynb             # Full training notebook
│   └── Algerian_forest_fires_dataset*.csv    # Dataset files
├── templates/
│   └── home.html                  # Web form & prediction display
└── static/                         # CSS/JS assets (optional)
```

## 🛠️ Installation

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Setup Steps

1. **Navigate to project directory:**
   ```bash
   cd c:\Users\mishr\anaconda_projects\Notebooks\E2E_Implementation\forest_fire_implementation
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirement.txt
   ```

## 🚀 Running the Application

Start the Flask development server:

```bash
python application.py
```

The server will start on:
- **Local:** http://127.0.0.1:8080
- **Network:** http://192.168.0.100:8080 (or your local IP)

Open your browser and navigate to `http://127.0.0.1:8080`

## 📊 How to Use

1. **Fill the form with your data:**
   - **Fire Classification:** Select "Fire" or "Not Fire"
   - **Temperature:** In °C
   - **Relative Humidity:** In %
   - **Wind Speed:** In km/h
   - **Rain:** In mm
   - **FFMC:** Fine Fuel Moisture Code (0-100+)
   - **DMC:** Duff Moisture Code (0-600+)
   - **DC:** Drought Code (0-800+)
   - **ISI:** Initial Spread Index (0-50+)

2. **Click "Predict Burned Area" button**

3. **View the prediction result** in the blue box below the form (in hectares)

## 🤖 Model Details

- **Algorithm:** Linear Regression
- **Training Data:** Algerian Forest Fires Dataset
- **Input Features:** 9 (Classes + 8 weather/FWI features)
- **Target:** Burned area in hectares
- **Preprocessing:** StandardScaler normalization applied

### Model Files
- `Forest_Fire_Linrear_Regression.pkl` — Trained regression model
- `Forest_Fire_scaler.pkl` — Fitted scaler for input normalization

## 📦 Dependencies

See `requirement.txt` for all required packages:
- Flask — Web framework
- pandas — Data manipulation
- numpy — Numerical computing
- scikit-learn — ML model & preprocessing

Install with: `pip install -r requirement.txt`

## 🔌 API Routes

| Route | Method | Purpose |
|-------|--------|---------|
| `/` | GET | Home page (redirects to prediction form) |
| `/predictdata` | GET | Return prediction form |
| `/predictdata` | POST | Receive form data and return prediction |

## 🐛 Troubleshooting

**Port already in use:**
- Change port in `application.py` line 60 or set `PORT` environment variable
- Example: `PORT=5000 python application.py`

**Model/Scaler not found:**
- Ensure `Models/` folder contains both `.pkl` files
- Check file paths in `application.py` lines 17-18

**Prediction errors:**
- Verify all 9 input fields are filled with valid numbers
- Check browser console (F12) for JavaScript errors

## 📝 Notes

- The model works best with input values in the typical range of the training dataset
- Burned area predictions are based on statistical relationships, not real-time fire simulation
- For production use, consider using a WSGI server (Gunicorn, uWSGI) instead of Flask development server

## 👨‍💻 Development

To modify the model or retrain:
1. Open `Notebook/regression_complete.ipynb` in Jupyter
2. Make changes and train the model
3. Export model and scaler to `Models/` folder
4. Restart the Flask application

## 📄 License

Project for educational purposes.

## 📞 Support

For issues or questions, check:
- `application.py` console logs
- Browser console (F12) for frontend errors
- Training notebook for model details

---

**Last Updated:** December 28, 2025
