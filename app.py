from flask import Flask, render_template, request
import sqlite3
import joblib

# Load the trained model and vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        url = request.form["url"]

        check_url = (
            url.lower()
            .replace("https://", "")
            .replace("http://", "")
            .replace("www.", "")
        )

        # AI Prediction
        url_vector = vectorizer.transform([check_url])
        prediction = model.predict(url_vector)[0]
        confidence = model.predict_proba(url_vector).max() * 100

        if prediction == "bad":
            result = f"⚠️ Phishing Website ({confidence:.2f}% Confidence)"
        else:
            result = f"✅ Safe Website ({confidence:.2f}% Confidence)"

        # Save result
        conn = sqlite3.connect("phishing.db")
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO history (url, result) VALUES (?, ?)",
            (url, result)
        )

        conn.commit()
        conn.close()

    # Dashboard Statistics
    conn = sqlite3.connect("phishing.db")
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM history")
    total = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM history WHERE result LIKE '%Safe%'")
    safe = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM history WHERE result LIKE '%Phishing%'")
    phishing = cursor.fetchone()[0]

    conn.close()

    return render_template(
        "index.html",
        result=result,
        total=total,
        safe=safe,
        phishing=phishing
    )


@app.route("/history")
def history():
    conn = sqlite3.connect("phishing.db")
    cursor = conn.cursor()

    try:
        cursor.execute(
            "SELECT id, url, result, scan_time FROM history ORDER BY id DESC"
        )
    except:
        cursor.execute(
            "SELECT id, url, result FROM history ORDER BY id DESC"
        )

    rows = cursor.fetchall()

    conn.close()

    return render_template("history.html", rows=rows)


@app.route("/clear_history")
def clear_history():
    conn = sqlite3.connect("phishing.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM history")

    conn.commit()
    conn.close()

    return history()


if __name__ == "__main__":
    app.run(debug=True)