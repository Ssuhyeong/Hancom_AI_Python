# Day_37_02_SklearnKaggle.py


# 데이터 과학자
# 케글에서 대회 참가
# 코세라, tensorflow 등의 관련 자격증을 취득
# 깃허브에 공부한 흔적 남기기
# 링크드인 가입

# 문제
# 캐글의 leaf-classification 대회의 Code 섹션에 있는
# 10 Classifier Showdown in Scikit-Learn 문서의 내용을 복사해서 수정하도록 만드세요
# 최종적으로 서브미션 파일을 생성해서 캐글 업로드까지 수행합니다.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, log_loss
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC, NuSVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.model_selection import StratifiedShuffleSplit, train_test_split
from sklearn import preprocessing

def warn(*args, **kwargs): pass
import warnings
warnings.warn = warn

from sklearn.preprocessing import LabelEncoder

train = pd.read_csv('leaf-classification/train.csv')
test = pd.read_csv('leaf-classification/test.csv')


def encode(train, test):
    le = LabelEncoder().fit(train.species)
    labels = le.transform(train.species)  # encode species strings
    classes = list(le.classes_)  # save column names for submission
    test_ids = test.id  # save test ids for submission

    train = train.drop(['species', 'id'], axis=1)   # 내가 제외한 컬럼을 train에 넣어준다.
    test = test.drop(['id'], axis=1)

    return train, labels, test, test_ids, classes

train, labels, test, test_ids, classes = encode(train, test)
train.head(1)

classifiers = [
        KNeighborsClassifier(3),
        SVC(kernel="rbf", C=0.025, probability=True),
        NuSVC(probability=True),
        DecisionTreeClassifier(),
        RandomForestClassifier(),
        AdaBoostClassifier(),
        # GradientBoostingClassifier(),
        GaussianNB(),
        LinearDiscriminantAnalysis(),
        QuadraticDiscriminantAnalysis()]




sss = StratifiedShuffleSplit(n_splits=10, test_size=0.2, random_state=23)

# for train_index, test_index in sss.split(train, labels):
#     X_train, X_test = train.values[train_index], train.values[test_index]
#     y_train, y_test = labels[train_index], labels[test_index]

for i in range(1) :
    X_train, X_test, y_train, y_test = train_test_split(train.values, labels, train_size=0.8, stratify=labels)

    # Logging for Visual Comparison
    log_cols = ["Classifier", "Accuracy", "Log Loss"]
    log = pd.DataFrame(columns=log_cols)

    for clf in classifiers:
        clf.fit(X_train, y_train)
        name = clf.__class__.__name__

        print("=" * 30)
        print(name)

        print('****Results****')
        train_predictions = clf.predict(X_test)
        acc = accuracy_score(y_test, train_predictions)
        print("Accuracy: {:.4%}".format(acc))

        train_predictions = clf.predict_proba(X_test)
        ll = log_loss(y_test, train_predictions)
        print("Log Loss: {}".format(ll))

        log_entry = pd.DataFrame([[name, acc * 100, ll]], columns=log_cols)
        log = log.append(log_entry)

print("=" * 30)

# Predict Test Graph
sns.set_color_codes("muted")
sns.barplot(x='Accuracy', y='Classifier', data=log, color="b")

plt.xlabel('Accuracy %')
plt.title('Classifier Accuracy')
plt.show()

sns.set_color_codes("muted")
sns.barplot(x='Log Loss', y='Classifier', data=log, color="g")

plt.xlabel('Log Loss')
plt.title('Classifier Log Loss')
plt.show()

# Predict Test Set
favorite_clf = LinearDiscriminantAnalysis()
favorite_clf.fit(X_train, y_train)
test_predictions = favorite_clf.predict_proba(test)

# Format DataFrame
submission = pd.DataFrame(test_predictions, columns=classes)
submission.insert(0, 'id', test_ids)
submission.reset_index()

# Export Submission
submission.to_csv('leaf-classification/submission.csv', index = False)
submission.tail()
#
# for i, pred in zip(test_ids, test_predictions):
#     print(i, ','.join([str(p) for p in pred]), sep=',')