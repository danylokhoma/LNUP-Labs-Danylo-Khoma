numbers = list(map(int, input("Масив: ").split()))

found = False
for x in numbers:
    for y in numbers:
        if y != x and y * y == x:
            print(f"{x} = {y}²")
            found = True
            break

if not found:
    print("Таких чисел немає")
