from flask import Flask, render_template, request
import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, precision_score
from sklearn.model_selection import train_test_split
app = Flask(__name__)
# 🔹 Clean text function
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9 ]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text
# 🔹 Load dataset
data = pd.read_csv("spam.csv", encoding='latin-1')
data = data[['v1', 'v2']]
data.columns = ['label', 'message']
data['label'] = data['label'].map({'ham': 0, 'spam': 1})
# 🔹 Clean data
data['message'] = data['message'].apply(clean_text)
# 🔹 Vectorizer
vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1,2))
X = vectorizer.fit_transform(data['message'])
y = data['label']
# 🔹 Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# 🔹 Model training
model = MultinomialNB()
model.fit(X_train, y_train)
# 🔹 Metrics
y_pred = model.predict(X_test)
accuracy = round(accuracy_score(y_test, y_pred) * 100, 2)
precision = round(precision_score(y_test, y_pred) * 100, 2)
# 🔹 Route
@app.route('/', methods=['GET', 'POST'])
def home():
    result = ""
    msg = ""
    if request.method == 'POST':
        msg = request.form['message']
        cleaned = clean_text(msg)
        
        spam_keywords = ["free money", "click here", "win", "prize", "urgent"]
        for word in spam_keywords:
            if word in cleaned:
                result = "Spam ❌"
                return render_template(
                    'index.html',
                    result=result,
                    user_input=msg,
                    accuracy=accuracy,
                    precision=precision
                )
        vec = vectorizer.transform([cleaned])
        prediction = model.predict(vec)
        result = "Spam ❌" if prediction[0] == 1 else "Not Spam ✅"
    return render_template(
        'index.html',
        result=result,
        user_input=msg,
        accuracy=accuracy,
        precision=precision
    )
if __name__ == '__main__':
    app.run(debug=True)