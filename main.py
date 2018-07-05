"""
This is dictionary
"""
import json
from utils import *
dictionary_file_name = 'dictionary.json'

while True:
    with open(dictionary_file_name,'r') as dictionary_file:
        data_dictionary = json.load(dictionary_file)
    command = raw_input('Enter R to read from dictionary, W to write new word or E to exit: ')
    if command.upper() == 'E':
        print 'Good luck'
        break
    elif command.upper() == 'R':
        word = raw_input('Enter word: ').lower()
        description_lst = get_description(word, data_dictionary)
        if len(description_lst) > 0:
            for description in description_lst:
                print '*** ' + description
        else:
            close_word = get_close_word(word, data_dictionary)
            if len(close_word) > 0:
                while True:
                    command = raw_input('Maybe you mean %s ? Y/N ' %(close_word)).upper()
                    if command == 'Y':
                        description_lst = get_description(close_word, data_dictionary)
                        if len(description_lst) > 0:
                            for description in description_lst:
                                print '*** ' + description
                        break
                    elif command == 'N':
                        break
                    else:
                        print 'Invalid command'
                        continue
            else:
                command = raw_input('We do not have this word in dictionary! Add to dictionary? Y/N ').upper()
                if command == 'Y':
                    description = raw_input('Enter description: ')
                    data_dictionary[word] = [description]
                    add_data_in_json(data_dictionary, dictionary_file_name)
                    print 'Data was appended successfully'
                elif command == 'N':
                    continue
                else:
                    print 'Invalid command'
    elif command.upper() == 'W':
        word = raw_input("Enter word: ").lower()
        description = raw_input("Enter description: ")
        data_dictionary[word] = [description]
        add_data_in_json(data_dictionary, dictionary_file_name)
        print 'Data was appended successfully'
    else:
        print 'Invalid command'
