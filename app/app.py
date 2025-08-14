from flask import Flask, render_template, request
import re
import joblib
import os

# Constants
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODELS_DIR = os.path.join(BASE_DIR, "../models")

# Load artifacts once at startup
model = joblib.load(os.path.join(MODELS_DIR, "log_model.pkl"))
vectorizer = joblib.load(os.path.join(MODELS_DIR, "tfidf_vectorizer.pkl"))
label_encoder = joblib.load(os.path.join(MODELS_DIR, "label_encoder.pkl"))

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\S+|www\S+", "", text)
    text = re.sub(r"@\w+", "", text)
    text = re.sub(r"#\w+", "", text)
    text = re.sub(r"[^a-z\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST" and (tweet := request.form.get("tweet")):
        cleaned = clean_text(tweet)
        vectorized = vectorizer.transform([cleaned])
        pred_encoded = model.predict(vectorized)[0]
        prediction = label_encoder.inverse_transform([pred_encoded])[0]
    
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)