def read_matrix(name):
    n = int(input(f"Порядок матриці {name}: "))
    return [list(map(float, input(f"{name}, рядок {i + 1}: ").split())) for i in range(n)]


def print_matrix(name, matrix):
    print(f"Матриця {name}:")
    for row in matrix:
        print("".join(f"{x:7g}" for x in row))


def norm(matrix):
    return max(sum(abs(x) for x in row) for row in matrix)


a = read_matrix("A")
b = read_matrix("B")

print_matrix("A", a)
print_matrix("B", b)

norm_a, norm_b = norm(a), norm(b)
print(f"||A|| = {norm_a:g}, ||B|| = {norm_b:g}")

if norm_a > norm_b:
    print("Більша норма у матриці A")
elif norm_b > norm_a:
    print("Більша норма у матриці B")
else:
    print("Норми матриць рівні")
