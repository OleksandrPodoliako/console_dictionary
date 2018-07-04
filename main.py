'''
This is dictionary
'''
import json

data_dictionary = json.load(open('dictionary.json','r'))

while True:
    command = raw_input('Enter R to read from dictionary, W to write new word in dictionary and E to exit: ')
    if command.upper() == 'E':
        print 'Good luck'
        break
    elif command.upper() == 'R':
        word = raw_input('Enter word: ')
        try:
            for description in data_dictionary[word]:
                print '*** '+ description
        except KeyError:
            print 'We do not have this word in dictionary!'
        pass
    elif command.upper() == 'W':
        pass
    else:
        print 'Invalid command'