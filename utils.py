import difflib
import json


def get_description(word, data_dictionary):
    description_lst = []
    if word in data_dictionary:
        for description in data_dictionary[word]:
            description_lst.append(description)
    elif word.title() in data_dictionary:
        for description in data_dictionary[word.title()]:
            description_lst.append(description)
    elif word.upper() in data_dictionary:
        for description in data_dictionary[word.upper()]:
            description_lst.append(description)
    return description_lst


def get_close_word(word, data_dictionary):
    close_word = ''
    if len(difflib.get_close_matches(word, data_dictionary.keys())):
        close_word = difflib.get_close_matches(word, data_dictionary.keys())[0]
    return close_word

def add_data_in_json(data, file_name):
    with open(file_name,'w') as json_file:
        json.dump(data, json_file)