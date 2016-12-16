import matplotlib.pyplot as plt

x_value = [1, 2, 3, 4, 5]
square = [1, 4, 9, 16, 25]

plt.plot(x_value, square, linewidth=5)
# plt title
plt.title("Square Numbers", fontsize=24)
# x label
plt.xlabel("Value", fontsize=14)
# y label
plt.ylabel("Square of Value", fontsize=14)
# label mark
plt.tick_params(axis='both', labelsize=14)
plt.show()
