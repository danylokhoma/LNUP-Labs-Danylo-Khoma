import random

number = random.randint(1, 100)
attempts = 0

print("Я загадав число від 1 до 100!")

while True:
    guess = int(input("Ваша спроба: "))
    attempts += 1
    if guess < number:
        print("Загадане число більше!")
    elif guess > number:
        print("Загадане число менше!")
    else:
        print("Ви вгадали!")
        break

print(f"Кількість спроб: {attempts}")
