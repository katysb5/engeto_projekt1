"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Katerina Novakova

email: katule.novakova@email.cz

discord: katysb5#4067

"""
users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123",
}

TEXTS = [
    """
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. """,
    """At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.""",
    """The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.""",
]

# this function takes the chosen text and transforms it into a list of words
def words_list(text):
    clean_text = list()
    for word in text.split():
        clean_text.append(word.strip(",.:;"))
    return clean_text


print("Your username:")
name = input()
print("Your password:")
password = input()

# checks if the user name and password matches with the registered users
if not users.get(name) == password:
    print("unregistered user, terminating the program..")
    exit
print("----------------------------------------")
print("Welcome to the app,", name)
print("We have 3 texts to be analyzed.")
print("----------------------------------------")
print("Enter a number btw. 1 and 3 to select:")
text = input()
print("----------------------------------------")

# here we check if the chosen text is valid
if not text.isnumeric():
    print("Wrong input. Terminating program.")
    exit
elif int(text) != 1 and int(text) != 2 and int(text) != 3:
    print("Invalid text chosen. Terminating program.")
    exit

chosen_text = words_list(TEXTS[int(text) - 1])
words = 0
titlecase = 0
uppercase = 0
lowercase = 0
numbers = 0
sum = 0
length = {}

# here we go through the list of words, word by word and categorize them
# by length and case
for string in chosen_text:
    if len(string) in length:
        length[len(string)] += 1
    else:
        length[len(string)] = 1
    words += 1
    if string.isalpha():
        if string.islower():
            lowercase += 1
        elif string.isupper():
            uppercase += 1
            titlecase += 1
        elif string[0].isupper() and string[1:].islower():
            titlecase += 1
    elif string.isnumeric():
        numbers += 1
        sum += int(string)

my_dict_keys = list(length.keys())
my_dict_keys.sort()

print("There are", words,"words in the selected text.")
print("There are", titlecase,"titlecase words.")
print("There are", uppercase,"uppercase words.")
print("There are", lowercase,"lowercase words.")
print("There are", numbers,"numeric strings.")
print("The sum of all the numbers is", sum)
print("----------------------------------------")
print("LEN|  OCCURENCES  |NR.")
print("----------------------------------------")

# here we formate the length of words and their occurrences
max_value = max(length.values())
for key in my_dict_keys:
    asterisk = ""
    number = length[key]
    while number != 0:
        asterisk += "*"
        number -= 1
    print(str(key).rjust(2), "|", asterisk.ljust(max_value), "|", length[key])
