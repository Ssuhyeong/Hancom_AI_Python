# Day_28_03_Voting.py

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

cancer = load_breast_cancer()
data_df = pd.DataFrame(cancer.data, columns=cancer.feature_names)
# print(data_df.head(3))

lr_clf = LogisticRegression()
knn_clf = KNeighborsClassifier(n_neighbors=8)

vo_clf = VotingClassifier(estimators=[('LR', lr_clf), ('KNN', knn_clf)], voting='soft')
x_train, x_test, y_train, y_test = train_test_split(cancer.data, cancer.target, test_size=0.2, random_state=11)
vo_clf.fit(x_train, y_train)
VotingClassifier(estimators=[('LR', LogisticRegression()),('KNN', KNeighborsClassifier(n_neighbors=8))], voting='soft')
pred = vo_clf.predict(x_test)

print('Voting Classifier Accuracy: {0:.4f}'.format(accuracy_score(y_test, pred)))

classifiers = [lr_clf, knn_clf]

for classifiers in classifiers :
    classifiers.fit(x_train, y_train)
    pred = classifiers.predict(x_test)
    class_name = classifiers.__class__.__name__

    print('{0} Accuracy: {1:.4f}'.format(class_name, accuracy_score(y_test, pred)))