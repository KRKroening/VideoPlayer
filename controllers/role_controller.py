from controllers.connector import dbConnect


def listAllRoles():
    with dbConnect() as cursor:
        cursor.execute('SELECT Description FROM Roles')
        return cursor.fetchall()
