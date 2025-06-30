# Health Risk Predictor using ML, DL, QML and QNN

This is a Flask-based web application that predicts health risks for **Diabetes**, **Heart Disease**, and **Lung Cancer** using four different types of models:
- Machine Learning (Random Forest)
- Deep Learning (Keras)
- Quantum Machine Learning (hybrid models)
- Quantum Neural Networks (QNN with PennyLane and PyTorch)

The application also integrates the **Gemini API** to provide evidence-based medical recommendations if any model flags the patient as at risk.
![image](https://github.com/user-attachments/assets/9491c482-9999-47fc-9f98-c8f761cac8ac)

---

## Technologies Used

- Python, Flask, HTML/CSS
- scikit-learn, TensorFlow/Keras, PyTorch
- PennyLane, Qiskit
- Gemini LLM API
- Docker (for containerization)
- GitHub Actions (CI/CD)

---

## Project Structure

```
.
├── app.py                  # Main Flask app
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker deployment file
├── .gitignore              # Files to exclude from Git
├── .dockerignore           # Docker ignore list
│
├── templates/              # HTML templates
├── static/                 # CSS, images
│
├── ml_model/               # Machine learning models and scaler
├── dl_model/               # Deep learning models and metrics
├── qml_model/              # Quantum ML (classical-quantum models)
├── qnn_model/              # Quantum neural networks (PyTorch)
├── qml-env/                # Environment setup for QML
├── data/                   # Dataset (optional)
├── .github/workflows/      # GitHub CI workflow (optional)
```

---

## Supported Predictions

### Diabetes
- Glucose
- BMI
- Age
- Diabetes Pedigree Function

### Heart Disease
- Age
- Sex
- Chest Pain Type
- Max Heart Rate
- ST Depression
- Exercise-Induced Angina

### Lung Cancer
- Age
- Gender
- Smoking Habit
- Coughing
- Chest Pain
- Shortness of Breath

Each prediction triggers all four models (ML, DL, QML, QNN). If any model detects risk, the app fetches a Gemini-powered recommendation.

---

## Running the App Locally

1. Clone the repository:

```bash
git clone https://github.com/pavani0410/health-risk-predictor.git
cd health-risk-predictor
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Set up environment variables:

Create a file named `.env` in the root directory and add:

```
GEMINI_API_KEY=your_gemini_api_key
```

5. Run the app:

```bash
python app.py
```

Then open your browser to `http://localhost:5000`

---

## Docker Deployment

To build and run the app in a Docker container:

```bash
docker build -t health-risk-app .
docker run -p 5000:5000 health-risk-app
```

---

## Gemini LLM Integration

The app uses Google’s Gemini API to provide medical recommendations when risk is detected. Prompts are optimized and cached using MD5 hashing for efficiency.

---

## Output Example

- Displays prediction from all four models (ML, DL, QML, QNN)
- Shows accuracy of each model from corresponding `metrics.json`
- If risk is detected, the Gemini API suggests 2–3 helpful actions
![image](https://github.com/user-attachments/assets/194e1299-407b-4356-8b86-56be325c6197)

---

## License

This project is open-source and available under the MIT License.

---

## Credits

Developed by Pavani Sharma and Shreya Bidare as a hybrid classical-quantum health prediction system with real-time LLM integration.
