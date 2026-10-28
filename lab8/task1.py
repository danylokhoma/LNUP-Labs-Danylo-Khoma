import csv

test1 = "Test variable to write to file"
with open("tests.txt", "w", encoding="utf-8") as f:
    f.write(test1)

with open("tests.txt", encoding="utf-8") as f:
    test2 = f.read()

print("1-3. test1 == test2:", test1 == test2)

with open("painters.csv", "w", encoding="utf-8") as f:
    f.write('author, canvas\n')
    f.write('Vincent Willem van Gogh, "Vase with sunflowers"\n')
    f.write('Rembrandt Harmenszoon van Rijn, "Aristotle"\n')
    f.write('Leonardo da Vinci, "Selfportrait"\n')

with open("painters.csv", encoding="utf-8") as f:
    painters = list(csv.DictReader(f, skipinitialspace=True))

print("4-5. painters:")
for painter in painters:
    print("  ", painter)

imdb = [
    {"title": "Lord of the Rings: Two towers", "year": 2002, "rating": 8.7},
    {"title": "Matrix", "year": 1999, "rating": 8.7},
    {"title": "Interstellar", "year": 2014, "rating": 8.5},
    {"title": "Back to the Future", "year": 1985, "rating": 8.5},
    {"title": "Logan: Wolverine", "year": 2017, "rating": 8.1},
]

with open("imdb.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["title", "year", "rating"])
    writer.writeheader()
    writer.writerows(imdb)

print("6. imdb.csv:")
with open("imdb.csv", encoding="utf-8") as f:
    print(f.read())
