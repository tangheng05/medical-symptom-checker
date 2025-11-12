# 🏥 Medical Symptom Checker

An intelligent symptom diagnosis system built with Flask that analyzes symptoms and provides potential diagnoses with confidence scores and personalized recommendations.

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-3.0+-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](LICENSE)
![Status](https://img.shields.io/badge/Status-Educational%20Project-yellow.svg)
![Educational](https://img.shields.io/badge/Note-Educational%20Use%20Only-orange.svg)

> **⚠️ DISCLAIMER**: This is an educational project and **NOT perfect**. Do **NOT** use it as a substitute for professional medical advice. Always consult qualified healthcare professionals for medical concerns.

## 📸 Screenshots

### Main Interface
![Symptom Input Interface](screenshots/Screenshot%202025-11-12%20140704.png)
*Symptom assessment form with temperature input*

### Pain/Severity Level Assessment
![Pain Level Rating](screenshots/Screenshot%202025-11-12%20140722.png)
*Interactive sliders to rate symptom severity from 0-10*

### Diagnosis Results
![Diagnosis Results](screenshots/Screenshot%202025-11-12%20140743.png)
*Disease detection with confidence scores and matched symptoms*

### Medical Recommendations
![Medical Recommendations](screenshots/img.png)
*Personalized suggestions and home care instructions*

## ✨ Features

- **Multi-Disease Detection**: Analyzes 9+ medical conditions (COVID-19, Flu, Pneumonia, Strep Throat, etc.)
- **Symptom Tracking**: 22+ symptoms across respiratory, general, and sensory categories
- **Confidence Scoring**: Percentage-based confidence levels for each diagnosis
- **Smart Recommendations**: Emergency alerts, medical guidance, and home care tips
- **Modern Interface**: Responsive design with interactive sliders and color-coded indicators
- **Privacy-First**: No data stored or transmitted - all processing happens locally

## 📋 Requirements

- Python 3.7+
- Flask 3.0+

## 🚀 Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/medical-symptom-checker.git
   cd medical-symptom-checker
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python app.py
   ```

4. **Open your browser:**
   ```
   http://localhost:5000
   ```

## 💡 How to Use

1. Enter your body temperature in Celsius
2. Rate each symptom from 0 (none) to 10 (severe) using the sliders
3. Click "Analyze Symptoms"
4. Review the diagnosis results and recommendations

## 📁 Project Structure

```
medical-symptom-checker/
├── app.py                 # Flask application & diagnostic logic
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Main UI
├── static/
│   ├── style.css         # Styling
│   └── script.js         # Client-side logic
└── screenshots/          # App screenshots
```

## 🧠 How It Works

1. **Symptom Collection**: User inputs via interactive sliders and temperature field
2. **Disease Matching**: Weighted symptom analysis calculates confidence scores for each disease
3. **Severity Assessment**: Evaluates temperature, critical symptoms, and overall intensity
4. **Recommendations**: Generates personalized advice based on top diagnosis and severity

## ⚠️ Important Notes

**This is an educational project and NOT perfect:**

- ✅ Good for learning about expert systems
- ✅ Demonstrates Flask web development
- ❌ Limited to 9 common conditions
- ❌ Rule-based, not AI/machine learning
- ❌ No personalization (age, gender, medical history)
- ❌ Not tested by medical professionals
- ❌ **NOT for actual medical diagnosis**

**Always consult healthcare professionals for real medical concerns.**

## 📝 License

Licensed under GNU General Public License v3.0 - see [LICENSE](LICENSE) file.

## 🤝 Contributing

Contributions welcome! Fork the repo, make your changes, and submit a pull request.

## 🙏 Acknowledgments

- Y3S1 Expert Systems course project at Norton University
- Built with Flask and Python
- Medical data compiled from reputable sources

---

**Remember**: This is an educational tool - always seek professional medical advice for health concerns.

**Version**: 2.0 | **Last Updated**: November 2025

