# Hierarchical-KNN-Method-for-Change-Detection

a novel time series similarity based change detection framework for identifying inter-annual changes by exploiting phenological properties of growing crops from satellite time series imagery. 

The workflow of the algorithm: 

1. Perform random sampling from the two relevant years of original dataset to get a representative sample of the data in order to reduce computation.

2. Build a cluster hierarchy model using hierarchical clustering on the training data with the chosen inter-cluster similarity measures.

3. Pick the optimal number of clusters and cluster groupings through dendrogram exploration.

4. For the test data, (i) perform centroid based label assignment, and (ii) perform k-Nearest Neighbor classification based label assignment.

5. Generate change map based on inter-annual cluster memberships using hierarchical relationships between the cluster labels.

In this folder, the Hierarchical clustering is implemented in R, and the K-Nearest Neighbor Classification is implemented in python.

