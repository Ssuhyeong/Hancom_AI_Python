import pandas as pd
import numpy as np

from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error



boston = load_boston()
df_boston = pd.DataFrame(boston.data, columns=boston.feature_names)
df_boston['PRICE'] = boston.target
# print('Boston Dataset Size: ', df_boston.size)
# print(df_boston.head())
y_target = df_boston['PRICE']
x_data = df_boston.drop(['PRICE'], axis=1, inplace=False)
x_train, x_test, y_train, y_test = train_test_split(x_data, y_target, test_size=0.3, random_state=156)
lr = LinearRegression()
lr.fit(x_train, y_train)
y_pred = lr.predict(x_test)
mae = mean_absolute_error(y_test, y_pred)
# print('MAE: {0:.3f}'.format(mae))

bias = np.round(lr.intercept_, 11)
weight = np.round(lr.coef_, 1)

# print('Bias : ', bias)
# print('Weight : ', weight)

coeff = pd.Series(data=weight, index=x_data.columns)
coeff.sort_values(ascending=False)
# print(coeff.sort_values(ascending=False))

