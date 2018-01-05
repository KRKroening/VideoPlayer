from controllers.connector import dbConnect


def listAllCategories():
    with dbConnect() as cursor:
        cursor.execute('SELECT CategoryId,Description FROM Category')
        return cursor.fetchall()


def getCategoryIdByName(name):
    id_list = []
    for n in name:
        with dbConnect() as cursor:
            cursor.execute('SELECT CategoryId FROM Category where Description = ?', (n,))
            id_list.append(cursor.fetchone()[0])
    return id_list

def getCategoryNameById(id):
    with dbConnect() as cursor:
        cursor.execute('SELECT Description FROM Category where CategoryId = ?', (id,))
        return cursor.fetchone()

def addNewCategory(data):
    with dbConnect() as cursor:
        cursor.execute("INSERT INTO Category(Description) Values(?)",(data["Description"],))