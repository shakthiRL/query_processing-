import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = np.exp(x / 10)

fig = plt.figure(figsize=(10, 8))

plt.subplot(2, 1, 1)
plt.plot(x, y1, color='blue')
plt.title("Sine Wave")

plt.subplot(2, 3, 4)
plt.plot(x, y2, color='green')
plt.title("Cosine Wave")

plt.subplot(2, 3, 5)
plt.plot(x, y3, color='red')
plt.title("Tangent Wave")

plt.subplot(2, 3, 6)
plt.plot(x, y4, color='purple')
plt.title("Exponential")

plt.tight_layout()
plt.show()