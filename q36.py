import matplotlib.pyplot as plt
import numpy as np

group1 = {'weight': np.random.randint(50, 70, 10), 'height': np.random.randint(150, 180, 10)}
group2 = {'weight': np.random.randint(60, 80, 10), 'height': np.random.randint(160, 190, 10)}
group3 = {'weight': np.random.randint(40, 60, 10), 'height': np.random.randint(140, 170, 10)}

plt.scatter(group1['weight'], group1['height'], label='Group 1', color='red')
plt.scatter(group2['weight'], group2['height'], label='Group 2', color='green')
plt.scatter(group3['weight'], group3['height'], label='Group 3', color='blue')

plt.title("Scatter Plot: Weights vs Heights")
plt.xlabel("Weight")
plt.ylabel("Height")
plt.legend()
plt.show()