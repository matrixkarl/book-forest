# dictionary will contain 
'''
book title: 1984
book author: George Orwell
word: silhoutte
definition: the outline of a person or object 

'''
'''
wordy_collector = {
    "book title": None,
    "book author": None,
    "book word": None,
    "word definition": None
}
'''

import json 

# pathlib lets us work with files and folders and Path is a class that represents the location of a file or folder
from pathlib import Path

# create a function to load data
def load_data(file):
    if file.exists():
        with open(file, 'r') as f:
            return json.load(f)
    else:
        return {}


# create function to save data
def save_data(word_collector, file):
    with open(file, mode='w') as f:
        json.dump(word_collector, f)

# create an object or an instance of the Path class, but it does not create the file itself or open a file 
file = Path('wordy_collector.json')

# check if the file exists
wordy_collector = load_data(file)

choice = ''

while choice != 'n':
    # acquire the book name
    # the strip strips whitespace like if the user entered  ' george' notice the space in front so .strip would go like 'george'
    # title capitalizes the beginning of each word such as 'George Orwell'
    book_name = input('Enter your book name: ').strip().title()

    # add to dictionary
    # check if the key is in there first
    if book_name not in wordy_collector:
        wordy_collector[book_name] = {}
        print('successfully added')

    word_choice = ''

    while word_choice != 'n':
        # acquire the word
        book_word = input('\nEnter the word: ').strip().title()

        # acquire the definition
        word_definition = input('\nEnter your definition of the word or copy and paste from the web: ').strip()

        # add to dictionary
        wordy_collector[book_name][book_word] = word_definition

        print('successfully added\n')

        word_choice = input('add more words?\ny for yes n for no:').lower()

        # save data
        save_data(wordy_collector, file)
        
    choice = input('would you like to add another book?\ny for yes n for no: ').lower()


print(wordy_collector)

