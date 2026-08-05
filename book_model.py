from database import get_connection
import mysql.connector

def add_book(title, author, price, quantity):
    sql = "INSERT INTO books (title, author, price, quantity) VALUES (%s, %s, %s, %s)"
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(sql, (title, author, price, quantity))
        conn.commit()
        return True, cursor.lastrowid
    except mysql.connector.Error as err:
        return False, str(err)
    finally:
        cursor.close()
        conn.close()

def update_book(book_id, title, author, price, quantity):
    sql = "UPDATE books SET title=%s, author=%s, price=%s, quantity=%s WHERE id=%s"
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(sql, (title, author, price, quantity, book_id))
        conn.commit()
        if cursor.rowcount == 0:
            return False, "book_id not found to update"
        else:
            return True, "Book updated successfully"
    except mysql.connector.Error as err:
        return False, str(err)
    finally:
        cursor.close()
        conn.close()

def delete_book(book_id):
    sql = "DELETE FROM books WHERE id=%s"
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(sql, (book_id,))
        conn.commit()
        if cursor.rowcount == 0:
            return False, "book_id not found to delete"
        return True, "Book Deleted successfully"
    except mysql.connector.Error as err:
        return False, str(err)
    finally:
        cursor.close()
        conn.close()

def search_books_by_title(title_keyword):
    sql = "SELECT * FROM books WHERE title LIKE %s"
    conn =  get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute(sql, (f"%{title_keyword}%",))
        return cursor.fetchall()
    except mysql.connector.Error as err:
        return False, str(err)
    finally:
        cursor.close()
        conn.close()

def get_available_books():
    sql = "SELECT * FROM books WHERE quantity > 0"
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute(sql)
        return cursor.fetchall()
    except mysql.connector.Error as err:
        return False, str(err)
    finally:
        cursor.close()
        conn.close()

def get_book_by_id(book_id):
    sql = "SELECT * FROM books WHERE id=%s"
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute(sql, (book_id,))
        return cursor.fetchone()
    except mysql.connector.Error as err:
        return False, str(err)
    finally:
        cursor.close()
        conn.close()

def get_all_books():
    sql = "SELECT * FROM books"
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute(sql)
        return cursor.fetchall()
    except mysql.connector.Error as err:
        return False, str(err)
    finally:
        cursor.close()
        conn.close()
