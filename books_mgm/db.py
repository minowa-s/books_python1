import os
import psycopg2

def get_connection():
    url = os.environ['DATABASE_URL']
    connection = psycopg2.connect(url)
    return connection

def insert_book(title, author, publisher, pages):
    connection = get_connection()
    cursor = connection.cursor()
    sql = "INSERT INTO books_python1 VALUES (default,%s, %s, %s, %s)"
    
    cursor.execute(sql,(title, author, publisher, pages))
    
    connection.commit()
    cursor.close()
    connection.close()

def edit_book(title, author, publisher, pages):
    connection = get_connection()
    cursor = connection.cursor()
    sql ="UPDATE books_python1 SET title = ?, author = ?, publisher = ?, pages = ?, WHERE id = ?";
    
    cursor.execute(sql,(title,author, publisher,pages))
    
    connection.commit()
    cursor.close()
    connection.close()
    

    
# def select_all_book():
#     connection = get_connection()
#     cursor = connection.cursor()
    
#     sql = 'SELECT title, author, publisher, pages FROM books_sample'
    
#     cursor.execute(sql)
#     rows = cursor.fetchall()
    
    # cursor.close()
    # connection.close()
    # return rows