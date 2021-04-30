#!/usr/bin/env python3

#Default Modules:
import numpy as np
import pandas as pd
import scipy 
import matplotlib.pyplot as plt
import os, glob, sys
from tqdm import tqdm
from astropy import units as u

plt.style.use("../mpl_files/custom_style1.mplstyle")

#Other Modules:
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

##### Author: Alex Polanski #####


#Generate the data
X, y_true = make_blobs(n_samples=400, centers=3,
        cluster_std=0.5, random_state=0)


#Use KMeans to group data
kmeans = KMeans(3, random_state=0)

labels = kmeans.fit(X).predict(X)



#Plot the results
plt.scatter(X[:, 0], X[:, 1], c=labels,s=40, cmap='viridis');
plt.show()
