def get_num_of_words(string):
    contents = string.split()
    return len(contents)

def get_num_of_characters(string):
    lower_contents = string.lower()
    characters_dict = {} 
    for char in lower_contents:
        count = 1
        if char in characters_dict:
            characters_dict[char] += 1
        else:
            characters_dict.update({char : count})

    return characters_dict 

def dict_to_list(dict):
    list_of_dicts = []
    for key in dict:
        list_of_dicts.append({"char" : key, "count" : dict[key]})


    return list_of_dicts
