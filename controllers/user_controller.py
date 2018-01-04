from controllers.connector import dbConnect

def listAllUsers():
    with dbConnect() as cursor:
        cursor.execute('SELECT Username, Psssword FROM User')
        return cursor.fetchall()


def VerifyUser(un,ps):
    with dbConnect() as cursor:
        cursor.execute('SELECT Username, Password, Role FROM User WHERE Username = ? and Password = ?', (un,ps))
        return cursor.fetchall()
