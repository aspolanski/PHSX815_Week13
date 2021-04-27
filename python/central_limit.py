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

##### Author: Alex Polanski #####

for i in np.arange(1,1000,200):

    n = round(i)
    draws = np.random.rayleigh(3.0, size = (1000,n))

    draws_avg = np.mean(draws, axis=1)

    plt.hist(draws_avg, bins=50,alpha=0.5,label = f'Draws = {i}')


plt.title("Central Limit Theorem Using a Rayleigh Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.xlim(3,6)
plt.legend()
plt.show()
