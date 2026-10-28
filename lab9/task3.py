from datetime import date, timedelta

DAYS = ["понеділок", "вівторок", "середа", "четвер", "п'ятниця", "субота", "неділя"]

happy = date(2008, 3, 25)
milestone = happy + timedelta(days=13330)
tense = "буде" if milestone > date.today() else "було"

answers = [
    f"Яка дата вашого народження?: {happy:%d.%m.%Y}",
    f"У який день тижня ви народилися?: {DAYS[happy.weekday()]}",
    f"Коли вам {tense} 13 330 днів від народження?: {milestone:%d.%m.%Y}",
]

with open("birthday.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(answers) + "\n")

with open("birthday.txt", encoding="utf-8") as f:
    print(f.read(), end="")
