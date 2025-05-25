
# import sqlite3

# # Connect to database
# conn = sqlite3.connect("data base/data.sqlite3")
# c = conn.cursor()

# def create_table():
#     sql = """
#     CREATE TABLE IF NOT EXISTS USER (
#         id INTEGER PRIMARY KEY,
#         NAME TEXT NOT NULL,
#         EMAIL TEXT NOT NULL UNIQUE,
#         ADDRESS TEXT
#     )
#     """
#     c.execute(sql)
#     conn.commit()

# create_table()
# conn.close()

import sqlite3

conn=sqlite3.connect("data base/product.sqlite3")
myc=conn.cursor()

def table():
    sql="""
    CREATE TABLE IF NOT EXISTS PRODUCT(
    id INTEGER PRIMARY KEY,
    NAME TEXT NOT NULL,
    PRICE INTEGER,
    QUANTITY INTEGER
    )
    """
    myc.execute(sql)
    conn.commit()
    
table()
conn.close()
