from controllers.connector import dbConnect


def listAllEpisodes():
    with dbConnect() as cursor:
        cursor.execute('SELECT Name, Description,EpisodeNumber, SeasonNumber, FileLocation FROM Episodes')
        return cursor.fetchall()

def listRecentEpisodes():
    with dbConnect() as cursor:
        cursor.execute('SELECT Name, Description,EpisodeNumber, SeasonNumber, FileLocation FROM Episodes ORDER BY DateAdded desc LIMIT 5')
        return cursor.fetchall()


def addNewEpisode(data):
    with dbConnect() as cursor:
        cursor.execute('INSET INTO Episodes(Name,Description,Series,EpisodeNumber,SeasonNumber,FileLocation,DateAdded) '
                       'Values(?,?,?,?,?,?,?)',
                       data["Name"], data["Description"], data["Series"], data["EpisodeNumber"], data["SeasonNumber"],
                       data["FileLocation"], data["FileLocation"])
        return cursor.fetchall()