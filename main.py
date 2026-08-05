from tabulate import tabulate

from database import init_db
import book_model as model

def handle_add_book():
    print("\n--- Adding Book ---\n")
    title = input("Enter book title: ").strip()
    author = input("Enter book author: ").strip()
    price = input("Enter book price: ").strip()

    # Bắt lỗi nhập số cho quantity
    try:
        quantity = int(input("Enter book quantity: ").strip())
    except ValueError:
        print("Error: Quantity must be a valid integer number!")
        return

    success, result = model.add_book(title, author, price, quantity)
    if success:
        print("Book added successfully")
    else:
        print(f"Error: {result}")

def handle_update_book():
    print("\n--- Update Book ---\n")
    # Bắt lỗi nhập ID
    try:
        book_id = int(input("Enter the book id that needs editing: "))
    except ValueError:
        print("Error: Invalid book ID!")
        return
    book = model.get_book_by_id(book_id)
    if not book:
        print("This book could not be found")
        return
    print(f"Sửa thông tin cho: {book['title']} (Nhấn Enter để giữ nguyên như cũ)")

    new_title = input("Enter new book title: ").strip()
    new_author = input("Enter new book author: ").strip()
    new_price = input("Enter new book price: ").strip()
    new_quantity = input("Enter new book quantity: ").strip()

    final_title = new_title if new_title else book['title']
    final_author = new_author if new_author else book['author']

    try:
        final_price = float(new_price) if new_price else book['price']
        final_quantity = int(new_quantity) if new_quantity else book['quantity']
    except ValueError:
        print("Error: Price and Quantity must be valid numbers!")
        return

    success, msg = model.update_book(book_id, final_title, final_author, final_price, final_quantity)
    if success:
        print("Book updated successfully")
    else:
        print(f"Error: {msg}")

def handle_delete_book():
    print("\n--- Delete Book ---\n")
    try:
        book_id = int(input("Enter the book id that needs deleting: "))
    except ValueError:
        print("Error: Invalid book id!")
        return
    book = model.get_book_by_id(book_id)
    if not book:
        print("This book could not be found")
        return

    confirm = input("Do you want to delete this book? (y/n): ").strip().lower()

    if confirm == "y":
        success, result = model.delete_book(book_id)
        if success:
            print("Book deleted successfully")
        else:
            print(f"Error: {result}")

def handle_search_book():
    print("\n--- Search Book ---\n")
    title_keyword = input("Enter book title keyword to search ")
    book = model.search_books_by_title(title_keyword)
    if not book:
        print("This book could not be found")
        return
    table_data = [[s["id"], s["title"], s["author"], s["price"], s["quantity"]] for s in book]
    print(tabulate(table_data, headers=["ID", "title", "Author", "Price", "Quantity"], tablefmt="fancy_grid"))

def handle_list_available_books():
    print("\n--- List Available Books ---\n")
    books = model.get_available_books()
    table_data = [[s["id"], s["title"], s["author"], s["price"], s["quantity"]] for s in books]
    print(tabulate(table_data, headers=["ID", "Title", "Author", "Price", "Quantity"], tablefmt="fancy_grid"))

def display_menu():
    while True:
        print("\n--- Menu ---\n")
        print("1. Add Book")
        print("2. Update Book")
        print("3. Delete Book")
        print("4. Search Book")
        print("5. List Available Books")
        print("6.List Available Books")
        print("7. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number from 1 to 6")
            continue

        if choice == 1:
            handle_add_book()
        elif choice == 2:
            handle_update_book()
        elif choice == 3:
            handle_delete_book()
        elif choice == 4:
            handle_search_book()
        elif choice == 5:
            handle_list_available_books()
        elif choice == 6:
            handle_list_available_books()
        elif choice == 7:
            print("Exiting")
            break
        else:
            print("Invalid choice")





if __name__ == '__main__':
    init_db()
    display_menu()