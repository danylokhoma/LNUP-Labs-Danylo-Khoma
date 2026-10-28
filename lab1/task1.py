x = int(input("x = "))
y = int(input("y = "))

if y != 0 and x % y == 0:
    print(f"{y} є дільником {x}")
elif x != 0 and y % x == 0:
    print(f"{x} є дільником {y}")
else:
    print("Жодне з чисел не є дільником іншого")
