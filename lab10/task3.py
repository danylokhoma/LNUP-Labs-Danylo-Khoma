import re

import matplotlib.pyplot as plt

with open("text.txt", encoding="utf-8") as f:
    text = f.read()

endings = re.findall(r"[^.!?…]+(\.\.\.|…|[.!?]+)", text)

counts = {"Звичайні": 0, "Питальні": 0, "Окличні": 0, "З трикрапкою": 0}
for end in endings:
    if end in ("...", "…"):
        counts["З трикрапкою"] += 1
    elif "?" in end:
        counts["Питальні"] += 1
    elif "!" in end:
        counts["Окличні"] += 1
    else:
        counts["Звичайні"] += 1

plt.bar(counts.keys(), counts.values(), color=["steelblue", "orange", "green", "red"])
plt.ylabel("Кількість речень")
plt.title("Типи речень у тексті")
plt.grid(True, axis="y")
plt.savefig("sentences.png", dpi=200)

for kind, n in counts.items():
    print(f"{kind}: {n}")
print("Гістограму збережено у файл sentences.png")
