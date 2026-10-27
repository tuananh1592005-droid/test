
import csv
import random

# Read the CSV file
with open("books-en.csv", encoding="latin-1", newline="") as file:
    books = list(csv.DictReader(file, delimiter=";"))


# TASK 1: Count books with titles longer than 30 characters
print("\n========== ЗАДАНИЕ 1 ==========")

count = 0
for book in books:
    if len(book["Book-Title"]) > 30:
        count += 1

print("Названий длиннее 30 символов:", count)


# TASK 2: Search books by author (1991 or 1996)
input("\nНажмите Enter для задания 2...")
print("\n========== ЗАДАНИЕ 2 ==========")

author = input("Введите автора: ").strip().lower()
count = 0

for book in books:
    if author in book["Book-Author"].lower() and author:
        if book["Year-Of-Publication"] in ("1991", "1996"):
            print(book["Book-Author"], "-",
                  book["Book-Title"], "-",
                  book["Year-Of-Publication"])
            count += 1

print("Найдено книг:", count)


# TASK 3: Generate 20 bibliographic references
input("\nНажмите Enter для задания 3...")
print("\n========== ЗАДАНИЕ 3 ==========")

# Keep only books with valid publication years
valid_books = [
    book for book in books
    if book["Year-Of-Publication"].isdigit()
]

# Select 20 random books
selected = random.sample(valid_books, 20)

# Save references to a text file
with open("bibliography.txt", "w", encoding="utf-8") as file:
    for i, book in enumerate(selected, 1):
        text = (f'{i}. {book["Book-Author"]}. '
                f'{book["Book-Title"]} - '
                f'{book["Year-Of-Publication"]}')

        print(text)
        file.write(text + "\n")

print("\nФайл bibliography.txt создан!")
print("Все задания выполнены!")
