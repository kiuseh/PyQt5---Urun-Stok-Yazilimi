import sqlite3 as sql

def insert(urun_adi, miktari, aciklama):
    conn = sql.connect("/home/kiuseh/Masaüstü/python/stok programı/Product_Database.db")
    cursor = conn.cursor()

    cursor.execute(""" CREATE TABLE IF NOT EXISTS PRODUCTS(
               urun_adi text,
               miktari integer,
               aciklama text
               )""")
    
    add_command = "INSERT INTO PRODUCTS VALUES (?,?,?)"
    data = (urun_adi, miktari, aciklama)
    cursor.execute(add_command, data)

    conn.commit()
    conn.close()

def deleteAllRows():
    conn = sql.connect("/home/kiuseh/Masaüstü/python/stok programı/Product_Database.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM PRODUCTS")

    conn.commit()
    conn.close()


def verileriAl(liste):
    conn = sql.connect("/home/kiuseh/Masaüstü/python/stok programı/Product_Database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT rowid, * FROM PRODUCTS")
    liste = cursor.fetchall()

    conn.commit()
    conn.close()