x = float(input("x = "))

if x <= 3:
    f = x ** 2 - 3 * x + 9
else:
    f = 1 / (x ** 3 + 6)

print(f"F({x}) = {f:.4f}")
