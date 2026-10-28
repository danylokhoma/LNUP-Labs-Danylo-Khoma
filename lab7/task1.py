from dataclasses import dataclass


@dataclass
class Student:
    surname: str
    name: str
    gender: str
    height: int


students = [
    Student("Шевченко", "Олена", "ж", 165),
    Student("Коваленко", "Андрій", "ч", 182),
    Student("Бондар", "Ірина", "ж", 158),
    Student("Ткачук", "Максим", "ч", 176),
    Student("Мельник", "Софія", "ж", 170),
    Student("Гнатюк", "Тарас", "ч", 188),
]

tallest_boy = max((s for s in students if s.gender == "ч"), key=lambda s: s.height)
shortest_girl = min((s for s in students if s.gender == "ж"), key=lambda s: s.height)

print("Найвищий хлопець:", tallest_boy.surname, f"({tallest_boy.height} см)")
print("Найнижча дівчина:", shortest_girl.surname, f"({shortest_girl.height} см)")

print("\nУчні в алфавітному порядку:")
for s in sorted(students, key=lambda s: (s.surname, s.name)):
    print(f"{s.surname:<10} {s.name:<8} {s.gender}  {s.height} см")
