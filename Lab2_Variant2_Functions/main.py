from utilities import read_books, read_currencies, write_file


# Task 1: Count titles longer than 30 characters
def task1(books):
    count = 0
    for book in books:
        if len(book["Book-Title"]) > 30:
            count += 1
    return f"ЗАДАНИЕ 1\nНазваний длиннее 30 символов: {count}\n"


# Task 2: Find books by author from 1991 or 1996
def task2(books, author):
    lines = [f"ЗАДАНИЕ 2\nАвтор: {author}"]
    count = 0

    for book in books:
        if (author.lower() in book["Book-Author"].lower()
                and book["Year-Of-Publication"] in ("1991", "1996")):
            lines.append(f'{book["Book-Author"]} - {book["Book-Title"]} - {book["Year-Of-Publication"]}')
            count += 1

    lines.append(f"Найдено книг: {count}")
    return "\n".join(lines) + "\n"


# Task 3: Generate 20 bibliography entries
def task3(books):
    lines = []
    for book in books[:20]:
        i = len(lines) + 1
        lines.append(f'{i}. {book["Book-Author"]}. {book["Book-Title"]} - {book["Year-Of-Publication"]}')

    write_file("bibliography.txt", "\n".join(lines) + "\n")
    return "ЗАДАНИЕ 3\n" + "\n".join(lines) + "\nФайл bibliography.txt создан\n"


# Task 4: Extract two lists from XML
def task4():
    names, values = read_currencies("currency.xml")
    return f"ЗАДАНИЕ 4\nName: {names}\nValue: {values}\n"


# Task 5: Show publishers without duplicates
def task5(books):
    publishers = set()
    for book in books:
        publishers.add(book["Publisher"])

    lines = ["ЗАДАНИЕ 5", f"Количество издательств: {len(publishers)}"]
    for publisher in sorted(publishers):
        lines.append(publisher)
    return "\n".join(lines) + "\n"


# Task 6: Show the 20 most downloaded books
def task6(books):
    top = sorted(books, key=lambda book: int(book["Downloads"]), reverse=True)[:20]
    lines = ["ЗАДАНИЕ 6", "20 самых популярных книг:"]
    for i, book in enumerate(top, 1):
        lines.append(f'{i}. {book["Book-Title"]} - {book["Downloads"]} скачиваний')
    return "\n".join(lines) + "\n"


def main():
    books = read_books("books-en.csv")
    author = "Grisham"  # Change the author name here

    results = [
        task1(books),
        task2(books, author),
        task3(books),
        task4(),
        task5(books),
        task6(books),
    ]

    write_file("output.txt", "\n".join(results))


if __name__ == "__main__":
    main()
