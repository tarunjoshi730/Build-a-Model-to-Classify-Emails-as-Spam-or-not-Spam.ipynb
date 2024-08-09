# Step 1: Load and Prepare the Dataset
import pandas as pd
data = { 
'email': [ 
'Free money!!!',  
'Hi Bob, how about a game of golf tomorrow?',  
'Limited time offer, buy now!',  
'Are you available for a meeting tomorrow?',  
'Congratulations, you have won a lottery!' 
], 
'label': ['spam', 'not spam', 'spam', 'not spam', 'spam'] 
}
df = pd.DataFrame(data) 
print(df)
# Step 2: Text Preprocessing
from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.model_selection import train_test_split 
from sklearn.naive_bayes import MultinomialNB 
from sklearn.metrics import accuracy_score, classification_report
# Convert text to lowercase 
df['email'] = df['email'].str.lower()
# Split the data into training and testing sets 
X_train, X_test, y_train, y_test = train_test_split(df['email'], df['label'], test_size=0.2, random_state=42)
# Vectorize the text data 
vectorizer = CountVectorizer() 
X_train_vec = vectorizer.fit_transform(X_train) 
X_test_vec = vectorizer.transform(X_test) 

# Step 4: Model Evaluation
# Model evaluation 
y_pred = model.predict(X_test_vec) 
accuracy = accuracy_score(y_test, y_pred) 
report = classification_report(y_test, y_pred, zero_division=0) 
print(f'Accuracy: {accuracy}') 
print('Classification Report:') 
print(report) 