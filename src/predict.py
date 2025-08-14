import re
import os
import joblib

# =============================
# 1. Load model, vectorizer, and label encoder
# =============================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODELS_DIR = os.path.join(BASE_DIR, "../models")

model_path = os.path.join(MODELS_DIR, "log_model.pkl")
vectorizer_path = os.path.join(MODELS_DIR, "tfidf_vectorizer.pkl")
label_encoder_path = os.path.join(MODELS_DIR, "label_encoder.pkl")

# Check if files exist
for path in [model_path, vectorizer_path, label_encoder_path]:
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")

model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)
label_encoder = joblib.load(label_encoder_path)

# =============================
# 2. Text preprocessing function
# =============================
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\S+|www\S+", "", text)   # remove URLs
    text = re.sub(r"@\w+", "", text)             # remove mentions
    text = re.sub(r"#\w+", "", text)             # remove hashtags
    text = re.sub(r"[^a-z\s]", "", text)         # remove non-letters
    text = re.sub(r"\s+", " ", text).strip()     # remove extra spaces
    return text

# =============================
# 3. Predict function
# =============================
def predict_sentiment(text):
    cleaned = clean_text(text)
    vectorized = vectorizer.transform([cleaned])
    pred_label_encoded = model.predict(vectorized)[0]
    pred_label = label_encoder.inverse_transform([pred_label_encoded])[0]
    return pred_label

# =============================
# 4. Run example
# =============================
if __name__ == "__main__":
    text = input("Enter a tweet: ")
    sentiment = predict_sentiment(text)
    print(f"Predicted Sentiment: {sentiment}")
