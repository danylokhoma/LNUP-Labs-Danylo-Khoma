from math import cos

a = float(input("a = "))
b = float(input("b = "))
h = float(input("h = "))

product = 1
count = 0

print(f"{'x':>6} | {'y':>8}")
for i in range(round((b - a) / h) + 1):
    x = a + i * h
    y = 2 * cos(x) - 1
    print(f"{x:6.2f} | {y:8.4f}")
    if y > 0:
        product *= y
        count += 1

print(f"Кількість додатних значень: {count}")
if count:
    print(f"Добуток додатних значень: {product:.4f}")
