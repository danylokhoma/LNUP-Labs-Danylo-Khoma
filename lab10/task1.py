import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 2, 400)
y = x ** 3 * np.cos(x ** 2)

plt.plot(x, y, "b-", linewidth=2, label="Y(x) = x³·cos(x²)")
plt.axhline(0, color="k", linewidth=0.8)
plt.xlabel("x")
plt.ylabel("Y(x)")
plt.title("Графік функції Y(x) = x³·cos(x²), x ∈ [-2; 2]")
plt.grid(True)
plt.legend()
plt.savefig("graph.png", dpi=200)

print("Графік збережено у файл graph.png")
print(f"Найбільше значення: {y.max():.4f} при x = {x[y.argmax()]:.2f}")
print(f"Найменше значення: {y.min():.4f} при x = {x[y.argmin()]:.2f}")
