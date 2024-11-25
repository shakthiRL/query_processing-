import matplotlib.pyplot as plt
import numpy as np

means_men = [22, 30, 35, 35, 26]
means_women = [25, 32, 30, 35, 29]
groups = ['G1', 'G2', 'G3', 'G4', 'G5']

x = np.arange(len(groups))
width = 0.35

fig, ax = plt.subplots()
ax.bar(x - width/2, means_men, width, label='Men', color='green')
ax.bar(x + width/2, means_women, width, label='Women', color='red')

ax.set_xlabel('Person')
ax.set_ylabel('Scores')
ax.set_title('Scores by person')
ax.set_xticks(x)
ax.set_xticklabels(groups)
ax.legend()

plt.tight_layout()
plt.show()