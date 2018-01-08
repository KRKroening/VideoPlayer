from controllers.connector import dbConnect


def listAllEpisodes():
    with dbConnect() as cursor:
        cursor.execute('SELECT Name, Description,EpisodeNumber, SeasonNumber, FileLocation FROM Episodes')
        return cursor.fetchall()

def listRecentEpisodes():
    with dbConnect() as cursor:
        cursor.execute('SELECT Name, Description,EpisodeNumber, SeasonNumber, FileLocation FROM Episodes ORDER BY DateAdded desc LIMIT 5')
        return cursor.fetchall()

def listAllEpisodesBySeries(series):
    with dbConnect() as cursor:
        cursor.execute("SELECT e.EpisodeId, e.Name, e.EpisodeNumber, e.SeasonNumber FROM Episodes e inner join Series s on s.SeriesId = e.Series where s.Name = ?", (series,))
        return cursor.fetchall()

def getEpisodeByEpisodeId(id):
    with dbConnect() as cursor:
        cursor.execute(
            "SELECT Name, Description,EpisodeNumber, SeasonNumber, FileLocation from Episodes WHERE EpisodeId = ?",
            (id,))
        return cursor

def addNewEpisode(data):
    with dbConnect() as cursor:
        cursor.execute('INSERT INTO Episodes(Name,Description,Series,EpisodeNumber,SeasonNumber,FileLocation,DateAdded) '
                       'Values(?,?,?,?,?,?,?)',
                       (data["Name"], data["Description"], data["Series"], data["EpisodeNumber"], data["SeasonNumber"],
                       data["FileLocation"], data["DateAdded"],))
        return cursor.fetchall()