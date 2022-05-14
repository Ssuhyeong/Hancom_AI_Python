from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import adjusted_rand_score
from sklearn.metrics import normalized_mutual_info_score
from sklearn.metrics import silhouette_samples, silhouette_score

import pandas as pd
import matplotlib.pyplot as plt

iris = load_iris()
feature_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
irisDF = pd.DataFrame(data=iris.data, columns=feature_names)
irisDF.head()

kmeans = KMeans(n_clusters=3, init='k-means++', max_iter=300, random_state=0).fit(iris.data)

print(kmeans.labels_)

irisDF['target'] = iris.target
irisDF['cluster'] = kmeans.labels_

iris_result = irisDF.groupby(['target', 'cluster'])['sepal_length'].count()
# print(iris_result)

### PCA(Principal Component Analysis) ###

pca = PCA(n_components=2)
pca_trasformed = pca.fit_transform(iris.data)
irisDF['pca_x'] = pca_trasformed[:, 0]
irisDF['pca_y'] = pca_trasformed[:, -1]

irisDF.head(3)

marker0_ind = irisDF[irisDF['cluster'] == 0].index
marker1_ind = irisDF[irisDF['cluster'] == 1].index
marker2_ind = irisDF[irisDF['cluster'] == 2].index

plt.scatter(x=irisDF.loc[marker0_ind, 'pca_x'], y=irisDF.loc[marker0_ind, 'pca_y'], marker='o')
plt.scatter(x=irisDF.loc[marker1_ind, 'pca_x'], y=irisDF.loc[marker1_ind, 'pca_y'], marker='s')
plt.scatter(x=irisDF.loc[marker2_ind, 'pca_x'], y=irisDF.loc[marker2_ind, 'pca_y'], marker='^')

plt.xlabel('PCA1')
plt.ylabel('PCA2')
plt.title('3 Clusters Visualization by 2 PCA Components')

# plt.show()

### Evaluation of Kmeans ###

ARI = adjusted_rand_score(irisDF['cluster'], kmeans.labels_)

NMI = normalized_mutual_info_score(iris.target, irisDF['cluster'])
print(NMI)

score_samples = silhouette_samples(iris.data, irisDF['cluster'])
irisDF['silhouette_coeff'] = score_samples
average_score = silhouette_score(iris.data, irisDF['cluster'])
print('iris dataset Silhuette Analysis Score : {0:.3f}'.format(average_score))

