from controllers.connector import dbConnect


def listAllRoles():
    with dbConnect() as cursor:
        cursor.execute('SELECT Description FROM Roles')
        return cursor.fetchall()

def getRoleIdFromName(name):
    with dbConnect() as cursor:
        cursor.execute('SELECT RoleId FROM Roles where Description = ?', (name,))
        return cursor.fetchall()