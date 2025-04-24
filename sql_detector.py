from sklearn.feature_extraction.text import TfidfVectorizer
from joblib import load

model = load('sql_model.joblib') 

def is_malicious(query):
    # Feature extraction
    features = vectorizer.transform([query])
    # Prediction (0=clean, 1=SQLi)
    return model.predict(features)[0] == 1

# Example: 
is_malicious("admin' OR 1=1--")  # Returns 1 (malicious)
