
# coding: utf-8

# In[29]:


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


# In[30]:


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import matplotlib.cm as cmap
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score
#

# In[31]:

def predict(filename):
    df=pd.read_csv('C:\\Users\\Niladri Shekhar Dutt\\Desktop\\IET-FE\\FakeNews\\fakenewsFE\\fake_or_real_news.csv')
    #df = df.set_index("Unnamed: 0")
    # Set `y`
    y = df.label

    # Drop the `label` column
    df.drop("label", axis=1)
    # Make training and test sets
    X_train, X_test, y_train, y_test = train_test_split(df['text'], y, test_size=0.5, random_state=53)

    # Initialize the `count_vectorizer`
    count_vectorizer = CountVectorizer(stop_words='english')

    # Fit and transform the training data
    count_train = count_vectorizer.fit_transform(X_train)

    # Initialize the `tfidf_vectorizer`
    tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)

    # Fit and transform the training data
    tfidf_train = tfidf_vectorizer.fit_transform(X_train)
    # Get the feature names of `tfidf_vectorizer`
    print(tfidf_vectorizer.get_feature_names()[-10:])

    # Get the feature names of `count_vectorizer`
    print(count_vectorizer.get_feature_names()[:10])


    # In[32]:


    count_df = pd.DataFrame(count_train.A, columns=count_vectorizer.get_feature_names())


    # In[33]:


    tfidf_df = pd.DataFrame(tfidf_train.A, columns=tfidf_vectorizer.get_feature_names())
    difference = set(count_df.columns) - set(tfidf_df.columns)
    set()
    print(count_df.equals(tfidf_df))
    count_df.head()


    # In[34]:


    tfidf_df.head()


    # In[40]:


    linear_clf = PassiveAggressiveClassifier(n_iter=50)
    linear_clf.fit(tfidf_train, y_train)


    # In[41]:

    #vec_clf = Pipeline([('vectorizer', tfidf_train), ('pac', linear_clf)])
    linear_clf.fit(tfidf_train, y_train)


    # In[42]:


    a=pd.read_csv(filename,encoding='latin1')
    # Set index
    #a=a.set_index("Unnamed: 0")
    # Print first lines of `df`
    X_test=a['text']


    # In[45]:



    # Transform the test set
    count_test = count_vectorizer.transform(X_test)
    # Transform the test set
    tfidf_test = tfidf_vectorizer.transform(X_test)
    pred=linear_clf.predict(tfidf_test)
    probs=linear_clf.decision_function(tfidf_test)


    # In[46]:


    probs=(probs+1.0)/2.0
    print(probs)


    # In[47]:

    flag=True
    for i in probs:
        if(i>(0.25)):
            flag=True
        else:
            flag=False

    print(flag)
    return (probs[0]*100)
    # In[48]:


    #print(pred)


    # In[49]:


    #print(probs)
