## lets create fake news detector
## import the libraries
from nltk.stem.porter import porterStemmer
# use for change word like (loved and loving)into (love)
from nltk.corpus import stopwords
# use for remove the some words like [ the , for ,of, in with]

import numpy as np
import pandas as pd
import re
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer # use for convert words into metrics
import sklearn.datasets
import sklearn

news_df = pd.read_csv('../train.csv')
news_df.head()

## removing the null values
news_df.isna().sum()
news_df = news_df.fillna('')
news_df.isna().sum()


## Stemming to remove all udeless words and expresions like [,._- ing s etc]
ps = porterStemmer()
def steaming(content):
   steamed_content = re.sub('[^a-zA-Z]'," ",content)
   # convert to lower case
   steamed_content = steamed_content.lower()
   # split the content
   steamed_content = steamed_content.split()
   # remove the stopword like loving loved into love
   steamed_content = [ps.stem(word) for word in steamed_content if not word in stopwords.words('english')]
   steamed_content = "".join(steamed_content)
   return steamed_content

news_df['content'] = news_df['content'].apply(steaming)

## seperating data
x= news_df['content'].values
y= news_df['label'].values

## convert the words into metrics vector
vector = TfidfVectorizer()
vector.fit(x)
vector.transform(x)
print(x)

## split the data
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,stratify=y,random_state=2)

## Train the model
model =LogisticRegression()
model.fit(x_train,y_train)

# prediction
x_train_pred = model.predict(x_train)
print('train accuacy:', accuracy_score(x_train_pred,y_train))

# prediction
y_train_pred = model.predict(y_train)
print('train accuacy:', accuracy_score(y_train_pred,y_test))

## pridiction system
input_data = x_test[10]
prediction = model.predict(input_data)
if prediction[0]== 1:
   print("Fake news")
else:
   print('Real news')


## Creating website 
## pip install streamlit
# streamlit app.py --> for run project on web 

import streamlit as st 
st.title('Fake News Article')
input_text = st.text_input('Enter news Article')

def prediction(input_text):
   input_data = vector.transform(input_text)
   prediction = model.predict(input_data)
   return prediction[0]

if input_text:
   pred = prediction(input_text)
   if pred == 1:
      st.write("The News is Fake")
   else:
      st.write("The news is Real")
      
st.write("Training accuracy score :",accuracy_score(x_train, y_train))
st.write("Testing accuracy score :",accuracy_score(x_test, y_test))

   

      
      