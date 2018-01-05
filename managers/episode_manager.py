from controllers import episode_controller,series_controller
import datetime

def compileDataForNewEpisodeEntry(data):
    data["Series"] = series_controller.getSeriesIdByName(data["Series"])
    data["DateAdded"] = datetime.datetime.now()
    data["Description"] = data["Description"][:50]
    data["Name"] = data["Name"][:20]
    episode_controller.addNewEpisode(data)