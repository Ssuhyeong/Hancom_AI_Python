# Day_29_01_Regression_Tree.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV

### Decision Tree Regression ###

boston = load_boston()

x_train, x_test, y_train, y_test = train_test_split(boston.data, boston.target, test_size=0.3, random_state=156)

dt_reg = DecisionTreeRegressor()
dt_reg.fit(x_train, y_train)
y_pred = dt_reg.predict(x_test)
print('MAE: {0:.3f}'.format(mean_absolute_error(y_test, y_pred)))   # MAE: 2.387

### RandomForestRegressor API ###

rf_reg = RandomForestRegressor(random_state=0)
rf_reg.fit(x_train, y_train)

y_pred = rf_reg.predict(x_test)
print("MAE: {0:.3f}".format(mean_absolute_error(y_test, y_pred)))    # MAE: 2.134

params = {'n_estimator':[50], 'max_depth':[6, 8, 10, 12], 'min_sample_leaf':[8, 12, 18]}
rf_reg = RandomForestRegressor(random_state=0, n_jobs=-1)

grid_cv = GridSearchCV(rf_reg, param_grid=params, cv=4, n_jobs=-1)
grid_cv.fit(x_train, y_train)
print('Optimal Hyper Parameter')
print(grid_cv.best_params_)
print('Min R^2: {0:.4f}'.format(grid_cv.best_score_))

rf_reg1 = RandomForestRegressor(n_estimators=300, max_depth=8, min_samples_leaf=8, min_samples_split=8, random_state=0)
rf_reg1.fit(x_train, y_train)
y_pred = rf_reg1.predict(x_test)
print('MAE: {0:.3f}'.format(mean_absolute_error(y_test, y_pred)))

ftr_importances_values = rf_reg1.feature_importances_
ftr_importances = pd.Series(ftr_importances_values, index=feature_names)
ftr_top20 = ftr_importances.sort_values(ascending=False)[:20]
plt.figure(x=ftr_top20, y= f)

