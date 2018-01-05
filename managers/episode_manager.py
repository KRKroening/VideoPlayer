from controllers import episode_controller,series_controller
import datetime
import re

def compileDataForNewEpisodeEntry(data):
    regex = re.compile('[^a-zA-Z ]')
    deries = regex.sub('', data["Series"])
    #deries = ''.join([i for i in data["Series"] if i.isalpha()])
    data["Series"] = series_controller.getSeriesIdByName(deries)[0]
    data["DateAdded"] = datetime.datetime.now()
    data["Description"] = data["Description"][:50]
    data["Name"] = data["Name"][:20]
    episode_controller.addNewEpisode(data)