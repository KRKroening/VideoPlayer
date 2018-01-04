import sqlite3 as sq
from contextlib import contextmanager

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
