import sqlite3 as sq
from contextlib import contextmanager

# def dbConnect():
#     try :
#         db = sq.connect("VideoPlayer")
#         return db
#         print("Connected")
#     except Exception as e:
#         print("error: " ,e)

@contextmanager
def dbConnect():
    connection = sq.connect("VideoPlayer")
    cursor = connection.cursor()
    try:
        yield cursor
    except:
        connection.rollback()
        raise
    else:
        connection.commit()
