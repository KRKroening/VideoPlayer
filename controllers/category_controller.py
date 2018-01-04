from controllers.connector import dbConnect


def listAllCategories():
    with dbConnect() as cursor:
        cursor.execute('SELECT CategoryId,Description FROM Category')
        return cursor.fetchall()
