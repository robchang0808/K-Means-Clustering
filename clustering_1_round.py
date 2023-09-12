# clustering_1_round.py
# Observing clusters using the k-means algorithm after one round of execution
# Robert Chang
# 9/12/23

import numpy as np
import matplotlib.pyplot as plt

# function for finding euclidean distance
def euclidean_distance(point1, point2):
    return np.sqrt(np.sum((point1 - point2) ** 2))

# k-means function
def k_means(points, k, initial_centroids):
    centroids = initial_centroids.copy()
    first_round = True

    while True:
        # assign points to clusters
        clusters = [[] for _ in range(k)]
        for point in points:
            distances = [euclidean_distance(point, centroid) for centroid in centroids]
            cluster_index = np.argmin(distances)
            clusters[cluster_index].append(point)

        # update cluster centers
        new_centroids = []
        for cluster in clusters:
            new_centroid = np.mean(cluster, axis=0)
            new_centroids.append(new_centroid)

        # check for convergence between old centroids and new centroids
        if np.allclose(centroids, new_centroids):
            break

        centroids = new_centroids

        # break after updating the centers once if it is the first round
        if first_round:
            break

        # set first_round variable to false to break the loop after the first round
        first_round = False

    return clusters, centroids

# A, B, C data points
points = np.array([[2, 10], [2, 5], [8, 4], [5, 8], [7, 5], [6, 4], [1, 2], [4, 9]])
k = 3
initial_centroids = np.array([[2, 10], [5, 8], [1, 2]])

# initialize k-means clustering
clusters, centroids = k_means(points, k, initial_centroids)

# convert centers to numpy array
centroids = np.array(centroids)

# plot the points on a scatter plot
colors = ['r', 'g', 'b']
for i, cluster in enumerate(clusters):
    cluster_points = np.array(cluster)
    plt.scatter(cluster_points[:, 0], cluster_points[:, 1], c=colors[i], label=f'Cluster {chr(65 + i)}')

# plot the cluster centers
plt.scatter(centroids[:, 0], centroids[:, 1], c='k', marker='x', label='Cluster Centroids')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('K-means Clustering After First Round')
plt.legend()
plt.show()

