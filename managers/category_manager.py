from controllers import category_controller

def compileDataForNewCategoryEntry(data):
    data["Description"] = data["Description"][:50]
    category_controller.addNewCategory(data)