AI-Phishing-URL-Detection
A lightweight python based web project that detects Phishing URL and flags it as legit or illegit
AI Phishing URL Detection

 Overview
AI Phishing URL Detection is a web-based application that uses Machine Learning to classify website URLs as Safe or Phishing.

The system accepts a URL from the user, processes it using TF-IDF vectorization, and uses a trained Logistic Regression model to predict the URL category. It also displays the model confidence, stores scan history in an SQLite database, and provides a dashboard with scan statistics.

 Features
- Detects phishing and safe URLs using Machine Learning
- Shows prediction confidence percentage
- Dashboard with total, safe, and phishing URL counts
- Scan history with date and time
- SQLite database for storing results
- Clear History option
- Pie chart for Safe vs Phishing results
- Simple web interface

Technologies Used

 Frontend
- HTML
- CSS
- Chart.js

 Backend
- Python
- Flask

  Machine Learning
- Scikit-learn
- TF-IDF Vectorizer
- Logistic Regression
- Joblib

  Database
- SQLite

Project Structure

```text
AI_Phishing_URL_Detection/
│
├── app.py
├── database.py
├── train_model.py
├── phishing_site_urls.csv
├── model.pkl
├── vectorizer.pkl
├── phishing.db
│
└── templates/
    ├── index.html
    └── history.html
```

 How It Works

1. The user enters a website URL.
2. Flask receives the URL from the web form.
3. The URL is cleaned and passed to the TF-IDF vectorizer.
4. TF-IDF converts the URL text into numerical features.
5. The Logistic Regression model predicts whether the URL is safe or phishing.
6. The application displays the prediction and confidence percentage.
7. The URL, result, and scan time are stored in SQLite.
8. The dashboard updates the Safe and Phishing counts.
9. The history page displays previous scans.

 Installation

1. Check Python

```bash
python --version
```

 2. Install Required Packages

Open the VS Code terminal and run:

```bash
pip install flask pandas scikit-learn joblib
```

 Setup and Running

 Step 1: Create the Database

```bash
python database.py
```

 Step 2: Train the Machine Learning Model

```bash
python train_model.py
```

This creates:

```text
model.pkl
vectorizer.pkl
```

Step 3: Start the Flask Application

```bash
python app.py
```

Open the local address shown by Flask, usually:

```text
http://127.0.0.1:5000
```

 Example

 Safe URL

```text
https://www.google.com
```

The application predicts the URL based on the trained model.

 Demonstration Phishing-like URL

```text
http://verify-account.com
```

Use synthetic/test URLs for demonstrations rather than visiting real suspected phishing sites.

> Note: The application is an educational classifier and does not guarantee that a real website is safe.

 Machine Learning Model

The project uses Logistic Regression for URL classification.

The dataset contains labels such as:

- `good` – Safe URL
- `bad` – Phishing URL

TF-IDF is used to convert URL text into numerical features before training the Logistic Regression model.

 Database

SQLite is used to store scan history.

| Field | Description |
|---|---|
| ID | Unique scan ID |
| URL | Scanned website URL |
| Result | Safe or phishing prediction |
| Scan Time | Date and time of the scan |

 Future Enhancements

- Improve detection using additional URL and domain features
- Compare multiple Machine Learning algorithms
- Add real-time threat intelligence checks
- Add user authentication
- Export scan history to CSV or PDF
- Deploy the application online
- Add email and QR-code phishing detection

 Disclaimer

This project is developed for educational and demonstration purposes. Machine Learning predictions can contain false positives and false negatives. A prediction from this application should not be considered a guarantee of website safety.

