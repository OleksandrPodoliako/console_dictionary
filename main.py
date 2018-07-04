'''
This is dictionary
'''
import json
from utils import print_description

data_dictionary = json.load(open('dictionary.json','r'))

while True:
    command = raw_input('Enter R to read from dictionary, W to write new word in dictionary and E to exit: ')
    if command.upper() == 'E':
        print 'Good luck'
        break
    elif command.upper() == 'R':
        word = raw_input('Enter word: ').lower()
        print_description(word, data_dictionary)
    elif command.upper() == 'W':
        pass
    else:
        print 'Invalid command'