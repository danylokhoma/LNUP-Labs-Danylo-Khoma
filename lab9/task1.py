import glob
import os
import shutil
import time
from datetime import datetime

print("1. Поточний каталог:", os.getcwd())
print("   Файли:", os.listdir("."))

print("2. Розмір task1.py:", os.path.getsize("task1.py"), "байт")

print("3. Файли за шаблоном *.py:", glob.glob("*.py"))

shutil.copyfile("first.txt", "second.txt")
with open("second.txt", encoding="utf-8") as f:
    print("4. Вміст second.txt:", f.read().strip())
os.remove("first.txt")
print("   first.txt видалено:", not os.path.exists("first.txt"))

print("5. Поточні дата й час:", datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

days = time.time() // 86400
print(f"6. Від початку епохи Unix минуло {days:.0f} днів, або {days // 365:.0f} років")
