

def returnDropDownList(collection,index):
    new_list = []
    for item in collection:
        new_list.append(item[index])
    return new_list