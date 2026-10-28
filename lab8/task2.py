with open("guest_book.txt", "w", encoding="utf-8") as book:
    while True:
        name = input("Ваше ім'я (q - вихід): ").strip()
        if name.lower() == "q":
            break
        greeting = f"Вітаємо, {name}! Дякуємо, що завітали."
        print(greeting)
        book.write(greeting + "\n")

print("\nВміст guest_book.txt:")
with open("guest_book.txt", encoding="utf-8") as book:
    print(book.read(), end="")
