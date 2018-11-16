# ========Exercise 1========

phonebook_dict = {
    'Alice': '706-493-1834',
    'Bob': '857-384-1234',
    'Elizabeth': '484-584-2923'
}

# 1. Print Elizabeth's phone number.
print phonebook_dict['Elizabeth']

# 2. Add a entry to the dictionary: Kareem's number is 938-489-1234.
phonebook_dict['Kareem'] = '938-489-1234'

# 3. Delete Alice's phone entry.
del phonebook_dict['Alice']

# 4. Change Bob's phone number to '968-345-2345'.
phonebook_dict['Bob'] = '968-345-2345'

# 5. Print all the phone entries.
print phonebook_dict

# ========Exercise 2: Nested Dictionaries========

ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}

# 1. Write a python expression that gets the email address of Ramit.
print ramit['email']

# 2. Write a python expression that gets the first of Ramit's interests.
print ramit['interests'][0]

# 3. Write a python expression that gets the email address of Jasmine.
print ramit['friends'][0]['email']

# 4. Write a python expression that gets the second of Jan's two interests.
print ramit['friends'][1]['interests'][1]

# ========Letter Summary========
# Write a letter_histogram function that takes a word as its input, 
# and returns a dictionary containing the tally of how many times 
# each letter in the alphabet was used in the word.

letter_histogram = raw_input("Word: ").lower()
# letter_histogram = letter_histogram.lower()
dictionary = dict()
for letter in letter_histogram:
    if letter not in dictionary:
        dictionary[letter] = 1
    else:
        dictionary[letter] += 1
print dictionary

# # Write a word_histogram function that takes a paragraph of text 
# # as its input, and returns a dictionary containing the tally of 
# # how many times each word in the alphabet was used in the text.

word_histogram = raw_input("Sentence: ")
word_histogram = word_histogram.lower()
split_word = word_histogram.split()
dictionary = dict()
for word in split_word:
    if word not in dictionary:
        dictionary[word] = 1
    else:
        dictionary[word] += 1
print dictionary

# ========Bonus Challenge========
# Given a histogram tally (one returned from either letter_histogram 
# or word_summary), print the top 3 words or letters.

letter_histogram = raw_input("Word: ")
letter_histogram = letter_histogram.lower()
dictionary = dict()
for letter in letter_histogram:
    if letter not in dictionary:    
        dictionary[letter] = 1
    else:
        dictionary[letter] += 1
    key = dictionary.items()
    l = list()
    for i, value in key:
        l.append((value, i))
    l.sort(reverse=True)

print l[0:3]

# ========Super Bonus Challenge========
# Given a list (example below), create a function that takes the list and returns 
# a dictionary that has a key "one," "two," "three," and so on. Assign the value for 
# each key to be a list of however many times a value shows up in the list. 

 