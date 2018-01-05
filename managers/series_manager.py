from controllers import series_controller, category_controller

def compileNewSeriesData(data):
    data["Category"] = str(category_controller.getCategoryIdByName(data["Category"]))
    data["Name"] = data["Name"][:20]
    data["Description"] = data["Description"][:100]
    series_controller.addNewSeries(data)