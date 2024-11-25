import numpy as np
import matplotlib.pyplot as plt

men_means = [22, 30, 35, 35, 26]
women_means = [25, 32, 30, 35, 29]
men_std = [4, 3, 4, 1, 5]
women_std = [3, 5, 2, 3, 3]

ind = np.arange(len(men_means)) 
width = 0.35  

plt.bar(ind, men_means, width, yerr=men_std, label='Men', color='blue')
plt.bar(ind, women_means, width, bottom=men_means, yerr=women_std, label='Women', color='orange')

plt.ylabel('Scores')
plt.title('Scores by group and gender')
plt.xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))
plt.legend()

plt.show()