from datetime import datetime

with open("today.txt", "w", encoding="utf-8") as f:
    f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

with open("today.txt", encoding="utf-8") as f:
    today_string = f.read()

today = datetime.strptime(today_string, "%Y-%m-%d %H:%M:%S")

print("Рядок з файлу:", today_string)
print("Рік:", today.year)
print("Місяць:", today.month)
print("День:", today.day)
print("Година:", today.hour)
print("Хвилина:", today.minute)
print("Секунда:", today.second)
