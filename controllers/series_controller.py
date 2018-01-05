from controllers.connector import dbConnect


def listAllSeries():
    with dbConnect() as cursor:
        cursor.execute('SELECT SeriesId, Name,Description FROM Series')
        return cursor.fetchall()

def getSeriesIdByName(name):
    with dbConnect() as cursor:
        cursor.execute('SELECT SeriesId FROM Series where Name = ?',name)
        return cursor.fetchone()

def addNewSeries(data):
    with dbConnect() as cursor:
        cursor.execute('INSERT INTO Series(Name,Description,Category) '
                       'Values(?,?,?)',(data["Name"], data["Description"], data["Category"],))
        print("Insert Successful")
        return cursor.fetchone()

def listSeriesByCategory(id):
    id = str(id)
    with dbConnect() as cursor:
        cursor.execute("SELECT Name, Description FROM Series where Category LIKE ?",("%"+id+",%",))
        return cursor.fetchall()