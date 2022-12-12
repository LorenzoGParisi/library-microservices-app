def dict_lowerCase(dict):
    for key in dict:
        if type(dict[key]) != type([]):
            dict[key] = dict[key].lower()
        elif type(dict[key]) == type([]):
            for index, item in enumerate(dict[key]):
                dict[key][index] = item.lower()
