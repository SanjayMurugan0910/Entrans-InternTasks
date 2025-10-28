import matplotlib.pyplot as plt

years = [2019, 2020, 2021, 2022, 2023]
product_a = [50, 60, 70, 90, 110]
product_b = [40, 55, 65, 80, 95]

plt.plot(years, product_a, marker='o', label='Product A', color='green')
plt.plot(years, product_b, marker='s', label='Product B', color='orange')
plt.bar(years, product_b,  label='Product B', color='blue')
plt.title("Product Sales Comparison", fontsize=14, fontweight='bold')
plt.xlabel("Year")
plt.ylabel("Sales (in thousands)")
plt.legend()
plt.grid(True)
plt.show()