
import csv

# Read the CSV file
with open("books-en.csv", encoding="latin-1", newline="") as file:
    books = list(csv.DictReader(file, delimiter=";"))


# TASK 5: List unique publishers
print("\n========== ЗАДАНИЕ 5 ==========")

publishers = set()

for book in books:
    publishers.add(book["Publisher"])

print("Количество издательств:", len(publishers))

for publisher in sorted(publishers):
    print(publisher)


# TASK 6: Find the 20 most popular books
input("\nНажмите Enter для задания 6...")
print("\n========== ЗАДАНИЕ 6 ==========")

# Sort books by downloads in descending order
books.sort(
    key=lambda book: int(book["Downloads"]),
    reverse=True
)

# Print the top 20 books
for i, book in enumerate(books[:20], 1):
    print(
        f'{i}. {book["Book-Title"]} - '
        f'{book["Downloads"]} скачиваний'
    )

print("\nВсе задания выполнены!")
