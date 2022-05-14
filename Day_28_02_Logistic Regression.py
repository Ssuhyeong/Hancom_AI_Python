import numpy as np
import pandas as pd

from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

cancer = load_breast_cancer()
df_cancer = pd.DataFrame(cancer.data, columns=cancer.feature_names)
df_cancer['CANCER'] = cancer.target
scaler = StandardScaler()
data_scaled = scaler.fit_transform(cancer.data)
x_train, x_test, y_train, y_test = train_test_split(data_scaled, cancer.target, test_size=0.3, random_state=0)
# print(x_train.shape)

lf_clf = LogisticRegression()
lf_clf.fit(x_train, y_train)

lr_pred = lf_clf.predict(x_test)
print('Accuracy: {:0.3f}'.format(accuracy_score(y_test, lr_pred)))

bias = np.round(lf_clf.intercept_, 11)
weight = np.round(lf_clf.coef_[0], 1)

# print('Bias: ', np.round(bias))
# print('Weight: ', np.round(weight))

coeff = pd.Series(data=weight, index=df_cancer.columns[:30])
# coeff = coeff.sort