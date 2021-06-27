import sqlite3

def connect():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS bookStore (ID INTEGER PRIMARY KEY AUTOINCREMENT, TITLE TEXT, AUTHOR TEXT,YEAR INTEGER, ISBN INTEGER )")
    conn.commit()
    conn.close()

def insert(title,author,year,isbn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO bookStore (TITLE, AUTHOR, YEAR, ISBN) VALUES (?,?,?,?)",
                             (title, author, year, isbn))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM bookStore")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(title="",author="",year="",isbn=""):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM bookStore WHERE TITLE=? OR AUTHOR=? OR YEAR = ? OR ISBN= ?",(title,author,year,isbn))
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM bookStore WHERE ID=?",(id,))
    conn.commit()
    conn.close()

def update(id,title,author,year,isbn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("UPDATE bookStore SET TITLE=?, AUTHOR =?, YEAR=?, ISBN=?  WHERE ID=?",(title,author,year,isbn,id))
    conn.commit()
    conn.close()

connect()
