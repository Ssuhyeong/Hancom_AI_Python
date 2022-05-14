# Day_27_03_Metrics.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_recall_curve
from sklearn.preprocessing import Binarizer
from sklearn.metrics import precision_score, recall_score, f1_score

### evaluation metrics ###

def get_clf_eval(y_test, pred) :
    confusion = confusion_matrix(y_test, pred)
    accuracy = accuracy_score(y_test, pred)
    precision = precision_score(y_test, pred)
    recall = recall_score(y_test, pred)

    print('Confusion Matrixs')
    print(confusion)
    print('Accuracy : {0:.4f}, Precision: {1:.4f}, Recall: {2:.4f}'.format(accuracy, precision, recall))

df_titanic = pd.read_csv('data/train.csv')

df_y = df_titanic['Survived']
# df_x = df_titanic.drop('Survived', axis=1)
# df_x = transform_features(df_x_titanic)
df_titanic.drop(['PassengerId','Name','Ticket','Cabin'],axis=1,inplace=True)
df_titanic.isnull().sum()

df_titanic['Age'].fillna(df_titanic['Age'].mean(),inplace=True)
df_titanic['Age']

df_titanic['Embarked'].replace('nan',np.nan,inplace=True)
df_titanic['Embarked'].fillna(df_titanic['Embarked'].mode()[0],inplace=True)

# print(df_titanic)

df_titanic['Sex']=df_titanic['Sex'].map({'male':0,'female':1})
df_titanic['Sex']

# print(df_titanic)
df_titanic['Embarked']=df_titanic['Embarked'].map({'S':0,'C':1,'Q':2})

df_x=df_titanic.drop(['Survived'],axis=1)

# print(df_titanic)

x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size=0.2, random_state=11)
x_train.shape

lr_clf = LogisticRegression()
lr_clf.fit(x_train, y_train)

pred = lr_clf.predict(x_test)

# get_clf_eval(y_test, pred)

### precision_recall_curve() API ###

pred_proba = lr_clf.predict_proba(x_test)[:, 1]
precision, recalls, thresholds = precision_recall_curve(y_test, pred_proba)
print('Shape Of Threshold List: ', thresholds.shape)
thr_index = np.arange(0, thresholds.shape[0], 15)
print('Sample Threshold Index: ', thr_index)
print('Sample Threshold Value: ', np.round(thresholds[thr_index], 2))
print('Sample Threshold Precision: ', np.round(precision[thr_index], 3))
print('Sample Threshold Recall: ', np.round(recalls[thr_index], 3))

def precision_recall_curve_plot(y_test, pred_proba):
    precision, recalls, thres = precision_recall_curve(y_test, pred_proba)
    thres_cnt = thres.shape[0]

    plt.figure(figsize=(8, 6))

    plt.plot(thres, precision[0:thres_cnt], linestyle='--', label='precision')
    plt.plot(thres, recalls[0:thres_cnt], label='recall')

    plt.xlabel('Treshold')
    plt.ylabel('Precision and Recall')
    plt.legend()
    plt.show()

# precision_recall_curve_plot(y_test, lr_clf.predict_proba(x_test)[:, 1])

x = [[1, -1, 2],
     [2, 0, 0],
     [0, 1.1, 1.2]]

binarizer = Binarizer(thresholds=1.1)
print(binarizer.fit_transform(x))

def get_clf_eval(y_test, pred) :
    confusion = confusion_matrix(y_test, pred)
    accuracy = accuracy_score(y_test, pred)
    precision = precision_score(y_test, pred)
    recall = recall_score(y_test, pred)
    f1 = f1_score(y_test, pred)

    print('Confusion Matrixs')
    print(confusion)
    print('Accuracy : {0:.4f}, Precision: {1:.4f}, Recall: {2:.4f}, F1:{3:.4f}'.format(accuracy, precision, recall, f1))

def get_eval_by_threshold(y_test, pred_proba, thresholds) :
    for custom_threshold in thresholds :
        binarizer = Binarizer(threshold=custom_threshold).fit(pred_proba)
        custom_predict = binarizer.transform(pred_proba)

        print('Treshold: ', custom_threshold)
        get_clf_eval(y_test, custom_predict)

pred_proba = lr_clf.predict_proba(x_test)
thresholds = [0.4, 0.45, 0.50, 0.55, 0.60]

get_eval_by_threshold(y_test, pred_proba[:, 1].reshape(-1, 1), thresholds)