Spam Detection Web Application

A Machine Learning based Spam Detection Web Application that classifies messages as Spam ❌ or Not Spam ✅.
This project uses Natural Language Processing (NLP) and a trained machine learning model to analyze text messages and identify spam patterns.

🚀 Project Overview

Spam messages are very common in emails and SMS. This project helps automatically detect spam messages using text preprocessing, feature extraction, and machine learning classification.

The user can enter a message in the web application, and the system will instantly predict whether the message is Spam or Not Spam.

⚙️ Technologies Used
Python – Programming language used to build the application
Flask – Web framework used to create the user interface
Pandas – Used for data handling and dataset processing
Scikit-learn – Used for machine learning model training
TF-IDF Vectorizer – Used to convert text into numerical features
HTML & CSS – Used to design the web page
🧠 Machine Learning Model

The project uses the Multinomial Naive Bayes Algorithm, which works very well for text classification problems like spam detection.

Model Workflow
Load the spam dataset
Clean the text messages (remove special characters, convert to lowercase)
Convert text into numerical form using TF-IDF Vectorization
Split the dataset into training and testing data
Train the Naive Bayes model
Evaluate the model using accuracy and precision
Deploy the model using Flask web application
📊 Model Performance
Metric	Score
Accuracy	96%
Precision	100%

This shows that the model correctly identifies most spam messages with very high reliability.

✨ Features
Detects spam messages instantly
Uses Machine Learning + NLP
Performs text preprocessing and cleaning
Uses TF-IDF feature extraction
Includes keyword-based spam detection for better accuracy
Interactive Flask web interface
Fast prediction time (less than 1 second)
🛡️ Spam Keywords Detection

The system also checks common spam keywords such as:

free
win
prize
click here
urgent

If these words appear in a message, the system can directly identify it as spam.

📂 Project Structure
spam-detection-project
│
├── app.py
├── spam.csv
├── templates
│   └── index.html
│
├── static
│   └── style.css
│
└── README.md
▶️ How to Run the Project
1️⃣ Clone the Repository
git clone https://github.com/yourusername/spam-detection-project.git
2️⃣ Open the Project Folder
cd spam-detection-project
3️⃣ Install Required Libraries
pip install flask pandas scikit-learn
4️⃣ Run the Application
python app.py
5️⃣ Open in Browser
http://127.0.0.1:5000/
💡 Example Predictions
Message	Prediction
Call me when you are free	Not Spam ✅
Click here to win prize	Spam ❌
Let's meet tomorrow	Not Spam ✅
Urgent! Claim your reward now	Spam ❌
