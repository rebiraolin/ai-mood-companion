# AI Mood Companion

AI Mood Companion is a lightweight, privacy-focused tool designed to help users process their emotions through text analysis. By combining a modern Flutter interface with a FastAPI-powered Machine Learning backend, the app provides immediate, non-judgmental feedback and encourages emotional awareness through local history tracking.

## 🚀 Features

- **Emotion Analysis**: Uses a custom-trained ML model to detect emotions (Happy, Sad, Anxious, Stressed, Neutral) from text input.
- **Supportive Responses**: Provides gentle, non-diagnostic reminders tailored to the detected emotion.
- **Local History**: Automatically saves your check-ins to your device using `shared_preferences`.
- **Privacy-First**: All personal data and history stay on your local device. No cloud sync, no accounts, and no tracking.
- **Clean UI**: A calm, minimal design built with Flutter's Material 3 system.

## 🛠️ Tech Stack

### Frontend
- **Flutter & Dart**: For a responsive, cross-platform mobile experience.
- **shared_preferences**: Local persistent storage for mood history.

### Backend
- **FastAPI (Python)**: High-performance API framework for serving ML predictions.
- **Uvicorn**: ASGI server for running the FastAPI application.

### Machine Learning
- **scikit-learn**: Used for TF-IDF vectorization and Logistic Regression classification.
- **Custom Pipeline**: A lightweight NLP pipeline for efficient text processing and emotion prediction.

## 🧠 How It Works

1. **Input**: The user describes their current feelings in the Flutter app.
2. **Analysis**: The text is sent to the FastAPI `/analyze` endpoint.
3. **ML Inference**: The backend uses a pre-trained `scikit-learn` pipeline to predict the dominant emotion.
4. **Responde Generation**: A supportive, non-diagnostic response is selected based on the prediction.
5. **Persistence**: The result is returned to the app, displayed to the user, and saved locally to the device's history.

## 💻 How to Run Locally

### 1. Backend Setup (FastAPI)
1. Navigate to the `backend` directory:
   ```bash
   cd backend
   ```
2. (Recommended) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the server:
   ```bash
   uvicorn main:app --reload
   ```
   *The API will be available at `http://127.0.0.1:8000`.*

### 2. Frontend Setup (Flutter)
1. Ensure you have the [Flutter SDK](https://docs.flutter.dev/get-started/install) installed.
2. Navigate to the `frontend` directory:
   ```bash
   cd frontend
   ```
3. Install dependencies:
   ```bash
   flutter pub get
   ```
4. Run the app:
   ```bash
   flutter run
   ```
   *Note: If running on a physical device, ensure the API URL in `lib/services/api_service.dart` is updated to your machine's local IP address.*

## ⚖️ Ethics & Limitations

- **Not Therapy**: AI Mood Companion is a self-reflection tool, not a substitute for professional mental health services, therapy, or medical advice.
- **Non-Diagnostic**: The "emotions" detected are based on statistical patterns in text and should not be taken as a clinical diagnosis.
- **Crisis Support**: If you are in a crisis, please contact local emergency services or a mental health hotline immediately.
- **Privacy**: We do not collect, store, or share your data. All records are stored locally on your device and can be cleared at any time.

## 🔮 Future Improvements

- **Data Visualization**: Adding weekly and monthly mood charts to track emotional trends over time.
- **Enhanced ML**: Incorporating Transformer-based models (like BERT) for more nuanced emotion detection.
- **Daily Reminders**: Optional local notifications to encourage consistent check-ins.
- **Export Functionality**: Ability to export local history as a PDF or CSV for personal review.

---
*Developed as a project for exploring the intersection of AI and Mental Wellbeing.*
