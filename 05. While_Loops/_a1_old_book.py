book_name = input()
books_checked = 0
is_book_found = False
current_book = input()
while current_book != "No More Books":
    if current_book == book_name:
        is_book_found = True
        print(f"You checked {books_checked} books and found it.")
        break
    books_checked += 1
    current_book = input()
if not is_book_found:
    print("The book you search is not here!")
    print(f"You checked {books_checked} books.")
