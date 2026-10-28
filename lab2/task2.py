a = float(input("a = "))
n = int(input("n = "))

p = 1
for k in range(n + 1):
    p *= a - k * n

print(f"P = {p:g}")
