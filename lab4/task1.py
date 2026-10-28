n, m = map(int, input("Розмір матриці (n m): ").split())
matrix = [list(map(int, input(f"Рядок {i + 1}: ").split())) for i in range(n)]

print("Матриця:")
for row in matrix:
    print("".join(f"{x:5}" for x in row))

rows = [i + 1 for i, row in enumerate(matrix) if all(row[j] < row[j + 1] for j in range(m - 1))]

if rows:
    print("Рядки, впорядковані за зростанням:", *rows)
else:
    print("Таких рядків немає")
