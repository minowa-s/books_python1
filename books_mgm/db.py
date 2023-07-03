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
    
def dis_all_book():
    connection = get_connection()
    cursor = connection.cursor()
    
    sql = 'SELECT id, title, author, publisher, pages FROM books_python1'
    
    cursor.execute(sql)
    rows = cursor.fetchall()
    
    cursor.close()
    connection.close()
    return rows

def delete_book(id):
    connection = get_connection()
    cursor = connection.cursor()
    
    sql = "DELETE FROM books_python1 WHERE id = %s"
    
    cursor.execute(sql,(id,))
    
    connection.commit()
    cursor.close()
    connection.close()


def edit_book(id, title, author, publisher, pages):
    connection = get_connection()
    cursor = connection.cursor()
    
    sql ="UPDATE books_python1 SET title = %s, author = %s, publisher = %s, pages = %s WHERE id = %s"
    
    cursor.execute(sql,(title, author, publisher, pages, id))
    
    connection.commit()
    cursor.close()
    connection.close()
    

