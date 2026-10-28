from collections import Counter

import matplotlib.pyplot as plt

ALPHABET = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"

with open("text.txt", encoding="utf-8") as f:
    text = f.read().lower()

counts = Counter(ch for ch in text if ch in ALPHABET)
letters = [ch for ch in ALPHABET if counts[ch]]
values = [counts[ch] for ch in letters]

plt.figure(figsize=(12, 5))
plt.bar(letters, values, color="steelblue")
plt.xlabel("Літера")
plt.ylabel("Кількість")
plt.title("Частота появи літер у тексті")
plt.grid(True, axis="y")
plt.savefig("letters.png", dpi=200)

print("Усього літер:", sum(values))
print("Найчастіші літери:", ", ".join(f"{ch} - {n}" for ch, n in counts.most_common(5)))
print("Гістограму збережено у файл letters.png")
