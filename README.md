# K-Means-Clustering
Python programs which perform k-means clustering on a set of data points with a specified number of clusters.

# Logistics
The programs are coded in Python and require the imports of numpy and matplotlib.pyplot. The file labeled "clustering_1_round.py" visualizes clustering after one round of execution, while the file labeled "clustering_final_round.py" visualizes the most optimal stage after clustering for however many rounds it takes to reach that stage. The library "matplotlib.pyplot" is used to project the results of each program in a graphical format, with different colors corresponding to the different clusters and their centroids.

# Process
The programs consist of two main functions: k_means and euclidean_distance. k_means takes arguments of "points", "k", and "initial_centroids", which correspond to the data points (in list format), the desired number of clusters, and the initial centroid points respectively. All three of these variables can be modified according to user preference. In the programs provided, 9 data points and 3 centroids are specified, with k = 3. 

The programs then follow the general k-means clustering process: 
1) Points are assigned to clusters based on their distances from the specified centroids, calculated using the Euclidean distance formula. numpy.argmin (abbreviated as np.argmin) is used to minimize the distances between data points and the centroids in the cluster assignment process.
2) New centroids are calculated by finding the mean data point of all the points within the individual clusters. This calculation is done by using numpy.mean (abbreviated as np.mean).
3) The old centroids and the new centroids are compared using numpy.allclose (abbreviated as np.allclose). If they are the same, then it means that the optimal centroids have been reached.
4) Steps 1, 2, and 3 are repeated until step 3 yields the optimal centroids and breaks the loop.

In "clustering_1_round.py", a few extra lines of code are added so that only one round of clustering (steps 1, 2, 3 run once) is visualized. In "clustering_final_round.py", steps 1, 2, and 3 are run until the optimal centroids are reached. The graph of the clusters and centroids is then constructed using a series of pyplot functions. The images provided ("clustering_1_round_result.png" and "clustering_final_round_result.png") display the difference in clusters between the first round and the final round of clustering.  
