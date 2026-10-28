from data import dishes, students


def menu_calories(dish):
    return dish["calorie_drink"] + dish["calorie_food"]


def menu(dish):
    return f'{dish["food"]} + {dish["drink"]} ({menu_calories(dish)} ккал)'


drink = max(dishes, key=lambda d: d["calorie_drink"])
food = min(dishes, key=lambda d: d["calorie_food"])

print("1. Калорійність страв:", ", ".join(f'{d["food"]} {d["calorie_food"]}' for d in dishes))
print("2. Найкалорійніше меню:", menu(max(dishes, key=menu_calories)))
print("3. Найменш калорійне меню:", menu(min(dishes, key=menu_calories)))
print("4. Меню до 300 ккал:", ", ".join(menu(d) for d in dishes if menu_calories(d) < 300))
print("5. Меню понад 500 ккал:", ", ".join(menu(d) for d in dishes if menu_calories(d) > 500))
print("6. Найкалорійніший напій:", f'{drink["drink"]} ({drink["calorie_drink"]} ккал)')
print("7. Найменш калорійна страва:", f'{food["food"]} ({food["calorie_food"]} ккал)')
print("8. Найвищий студент:", max(students, key=lambda s: s["height"])["name"])
print("9. Наймолодший студент:", min(students, key=lambda s: s["age"])["name"])
print("10. Сумарний вік студентів:", sum(s["age"] for s in students))
print("11. Сумарний зріст студентів:", sum(s["height"] for s in students))
print("12. Найстарший студент:", max(students, key=lambda s: s["age"])["name"])
print("13. Калорійність усіх напоїв:", sum(d["calorie_drink"] for d in dishes))
print("14. Калорійність усіх страв:", sum(d["calorie_food"] for d in dishes))
