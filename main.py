"""
This is dictionary
"""


import json
from utils import *

data_dictionary = json.load(open('dictionary.json','r'))

while True:
    command = raw_input('Enter R to read from dictionary or E to exit: ')
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
                print 'Maybe you mean ' + close_word + ' ?'
                command = raw_input("Y/N").upper()
                if command == 'Y':
                    description_lst = get_description(close_word, data_dictionary)
                    if len(description_lst) > 0:
                        for description in description_lst:
                            print '*** ' + description
                elif command == 'N':
                    continue
                else:
                    print 'Invalid command'
            else:
                print 'We do not have this word in dictionary!'
    elif command.upper() == 'W':
        pass
    else:
        print 'Invalid command'