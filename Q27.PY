import matplotlib.pyplot as plt

languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

plt.figure(figsize=(10, 6))
plt.bar(languages, popularity, color='blue')
plt.title("Popularity of Programming Languages\nWorldwide, Oct 2017 compared to a year ago")
plt.xlabel("Languages")
plt.ylabel("Popularity")

plt.grid(True, color='red', linestyle='--', linewidth=0.5)

plt.show()