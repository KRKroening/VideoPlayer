from controllers.connector import dbConnect


def listAllSeries():
    with dbConnect() as cursor:
        cursor.execute('SELECT SeriesId, Name,Description FROM Series')
        return cursor.fetchall()
