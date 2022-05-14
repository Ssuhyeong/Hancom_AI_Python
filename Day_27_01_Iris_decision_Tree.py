# Day_27_01_Iris_decision_Tree.py

import sklearn
import pandas as pd
import numpy as np

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.model_selection import KFold
from sklearn.datasets import load_iris
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV



# print(sklearn.__version__)
# iris = load_iris()
#
# iris_data = iris.data
# # print(iris_data)
# iris_label = iris.target
# # print(iris_label)
#
# # print('iris target value : ', iris_label)
# # print('iris target name : ', iris.target_names)
#
# df_iris = pd.DataFrame(data=iris_data, columns = iris.feature_names)
# df_iris['label'] = iris.target
# # print(df_iris)
#
# x_train, x_test, y_train, y_test = train_test_split(iris_data, iris_label, test_size = 0.2, random_state =11)
#
# df_clf = DecisionTreeClassifier(random_state = 11)
# df_clf.fit(x_train, y_train)
# pred = df_clf.predict(x_test)
# print('predict accuracy: {}'.format(accuracy_score(y_test, pred)))
#
# # df_clf = DecisionTreeClassifier()
# # train_data = iris.data
# # train_label = iris.target
# # df_clf.fit(train_data, train_label)
# # pred = df_clf.predict(train_data)
# # print(accuracy_score(train_label, pred))
#
# ### Train_test_split() API ###
#
# iris = load_iris()
# x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.5, random_state = 121)
# print(x_train.shape)
#
# ### KFold API ###
#
# dt_clf = DecisionTreeClassifier(random_state=156)
# cv_accuracy = []
# iris = load_iris()
# features = iris_data
# label = iris.target
# KFold = KFold(n_splits=3, random_state=156, shuffle=True)
#
# fold_index = 0
# for train_index, test_index in KFold.split(features) :
#     x_train, x_test = features[train_index], features[test_index]
#     y_train, y_test = label[train_index], label[test_index]
#
#     dt_clf.fit(x_train, y_train)
#     pred = dt_clf.predict(x_test)
#
#     fold_index += 1
#     accuracy = np.round(accuracy_score(y_test, pred), 4)
#     train_size = x_train.shape[0]
#     test_size = x_test.shape[0]
#
# #     print('\n #{0} fold accury : {1}, train size : {2}, val size : {3}'.format(fold_index, accuracy, train_size, test_size))
# #     print('#{0} val index : {1}'.format(fold_index, test_index))
# #
# #     cv_accuracy.append(accuracy)
# #
# # print('\n## avg val accuracy: ', np.mean(cv_accuracy))

### stratified K Fold API ###

# iris = load_iris()
# df_iris = pd.DataFrame(data=iris, columns=iris.feature_names)
# df_iris['label'] = iris.target
# df_iris['label'].value_counts()
# kfold = KFold(n_splits=3)
# fold_index = 0
# for train_index, test_index in kfold.split(df_iris) :
#     fold_index += 1
#
#     label_train = df_iris['label'].iloc[train_index]
#     label_test = df_iris['label'].iloc[test_index]
#
#     print('## Cross validation : {0}'.format(fold_index))
#     print('Train label distribution: ')
#     print(label_train.value_counts(), end='\n\n')
#     print('Val label distribution: ')
#     print(label_test.value_counts(), end='\n\n')
#
# skf = StratifiedKFold(n_splits=3)
# fold_index = 0
# for train_index, test_index in skf.split(df_iris, df_iris['label']) :
#     fold_index += 1
#
#     label_train = df_iris['label'].iloc[train_index]
#     label_test = df_iris['label'].iloc[test_index]
#
#     print('## Cross validation : {0}'.format(fold_index))
#     print('Train label distribution: ')
#     print(label_train.value_counts(), end='\n\n')
#     print('Val label distribution: ')
#     print(label_test.value_counts(), end='\n\n')

# iris = load_iris()
# features = iris.data
# label = iris.target
#
# df_clf = DecisionTreeClassifier(random_state=156)
# skfold = StratifiedKFold(n_splits=3)
# fold_index = 0
# list_accuracy = []
#
# for train_index, test_index in skfold.split(features, label) :
#     x_train, x_test = features[train_index], features[test_index]
#     y_train, y_test = label[train_index], label[test_index]
#
#     df_clf.fit(x_train, y_train)
#     pred = df_clf.predict(x_test)
#
#     fold_index += 1
#     accuracy = np.round(accuracy_score(y_test, pred), 4)
#     train_size = x_train.shape[0]
#     test_size = x_test.shape[0]
#
#     print('\n #{0} Cross val accuracy : {1}, train size : {2}, test size : {3}'.format(fold_index, accuracy, train_size, test_size))
#     print('#{0} Val index : {1}'.format(fold_index, test_index))
#
#     list_accuracy.append(accuracy)
#
# print('\n ## fold val accuracy: ', np.round(list_accuracy, 4))
# print('## avg val accuracy: ', np.mean(list_accuracy))

## cross_val_score() API ##

# iris = load_iris()
#
# data = iris.data
# label = iris.target
#
# dt_clf = DecisionTreeClassifier(random_state=156)
#
# scores = cross_val_score(estimator=dt_clf, X=data, y=label, scoring='accuracy', cv=3)
# print('Fold val accuracy : ', np.round(scores, 4))
# print('Avg val accuracy : ', np.round(np.mean(scores), 4))

### GridSearchCV API ###

# iris = load_iris()
#
# x_train, x_test, y_train, y_test = train_test_split(iris.data,
#                                                      iris.target,
#                                                      test_size=0.2,
#                                                      random_state=121)
# dtree = DecisionTreeClassifier()
# parameters = {'max_depth':[1,2,3], 'min_samples_split':[2,3]}
# grid_dtree = GridSearchCV(dtree, param_grid=parameters, cv=3, refit=True)
# grid_dtree.fit(x_train, y_train)
#
# scores_df = pd.DataFrame(grid_dtree.cv_results_)
# scores_df[['params', 'mean_test_score', 'rank_test_score', 'split0_test_score', 'split1_test_score', 'split2_test_score']]
# print('Optimal Prameter: ', grid_dtree.best_params_)
# print('Max accuracy: {0:.4f}'.format(grid_dtree.best_score_))
#
# estimator = grid_dtree.best_estimator_
# pred = estimator.predict(x_test)
#
# print('Test dataset accuracy : {0:.4f}'.format(accuracy_score(y_test, pred)))
