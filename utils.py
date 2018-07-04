def print_description(word, data_dictionary):
    if word in data_dictionary:
        for description in data_dictionary[word]:
            print '*** ' + description
    else:
        print 'We do not have this word in dictionary!'