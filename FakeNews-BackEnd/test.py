import numpy as np
import pandas as pd
import itertools
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import pickle

df = pd.read_csv('news.csv')

df.shape
df.head(10)

print(df.isnull().sum())

labels = df.label
labels.head()

text = df.text
text.head()

title = df.title
title.head()

x_train, x_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2, random_state=5) #change test_size accself.

tfidf_vectorizer=TfidfVectorizer(stop_words='english', max_df=0.7)

tfidf_train=tfidf_vectorizer.fit_transform(x_train) 

tfidf_test=tfidf_vectorizer.transform(x_test)


model=PassiveAggressiveClassifier(max_iter=50)
model.fit(tfidf_train,y_train)

y_pred=model.predict(tfidf_test)
score=accuracy_score(y_test,y_pred)
print(f'Accuracy: {round(score*100,2)}%')

confusion_matrix(y_test,y_pred, labels=['FAKE','REAL'])

input_data = ["Bush died"]
vectorized_input_data = tfidf_vectorizer.transform(input_data)
prediction = model.predict(vectorized_input_data)
print(prediction)
