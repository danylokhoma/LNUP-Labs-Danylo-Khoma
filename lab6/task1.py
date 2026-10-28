text = input("Рядок: ").strip()

words = text.rstrip(".").split()
words[0], words[-1] = words[-1], words[0]

print("Результат:", " ".join(words) + ".")
