###
#
#
#

import disney.txt
import ta
import tarzan.txt
import disney.txt

filename= input('\nInput file name: ')
with open(filename) as f:
    lines = f.readlines()
    for line in lines:
        #call function to handel tokens
if filename not disney.txt :
    print(input('File not found try again: '))
    elif filename not tarzan.txt :
        print(input('File not found try again: '))
        elif filename not tarzan.txt or disney.txt:
            print(input('File not found try again: '))
            else:
                print('thanks but you cannot play MadLibs')
Output = print(input('Output file name: '))

def handlesFiles():
    read input file
    write output file
def handlesUserimputs(line):




main()

print('Welcome to the game of MadLibs')
print('I will ask you to provide several words and phrases to fill in a mad lib story.')
print('The result will be written to an output file. ')

Welcome_text = """
Welcome to the game of Mad Libs.
I will ask you to provide various words and phrases to fill in a story.
The result will be written to an output file.
"""

valid_options = "cCvVqQ"

# Helper functions

def get_option():
    """ returns a valid option """
    print()
    op = input("(C)reate mad-lib, (V)iew mad-lib, (Q)uit? ")
    while op not in valid_options:
        op = input("(C)reate mad-lib, (V)iew mad-lib, (Q)uit? ")

return op

def get_file(create=True):
    """ returns input and output filenames that are taken from the user """
    in_file = input("Input file name: ").strip()
    while not os.path.exists(in_file):
        in_file = input("File not found. Try again: ")

    if create:
        out_file = input("Output file name: ").strip()
    if not out_file.endswith('.txt'):
        out_file += ".txt"
    return in_file, out_file

    return in_file

def is_placeholder(word):
    """ returns true if the given word is a placeholder, else, returns false """
    return word.startswith('<') and word.endswith('>')

def read_file(filename):
    """ reads the content from a file and returns words and placeholders """
    words = []
    placeholders = []

    with open(filename, 'r') as f:
    for line in f:
    for word in line.split(' '):
    if is_placeholder(word):
    placeholders.append(word)
    words.append(word)

return words, placeholders

def get_placeholders(placeholders):
    """ returns placeholder texts given by the user """
    print()
    for i, item in enumerate(placeholders):
    response = input(f"Please type any {item[1:-1].replace('-', ' ')}: ")
    placeholders[i] = response

return placeholders

def write_to(out_file, words_list, placeholders):
    """ writes the text with filled placeholders to output file """
    words = words_list.copy()
    i = 0

    for n, word in enumerate(words):
    if is_placeholder(word):
    words[n] = placeholders[i]
    i += 1

    with open(out_file, 'w') as f:
    f.write(" ".join(words))

print("Your mad-lib has been created!\n")

def view_mad_lib(filename):
    """ to view a mad-lib file """
    with open(filename, 'r') as f:
    print('- '*40)
    print(f.read())
    print('- '*40)

def main():

    # print the welcome text
    print(Welcome_text)

    while True:
        # get option
        op = get_option()

    # create option selected
    if op in 'cC':
        # read input and output file names from the user
        in_file, out_file = get_file()
        # read contents and placeholders from the input file
        words, placeholders = read_file(in_file)
        # get text for placeholders from the user
        placeholders = get_placeholders(placeholders)
        # write to output file with those placeholder texts given by the user
        write_to(out_file, words, placeholders)

    # view option selected
    elif op in 'vV':
        # get the file name to be viewed
        in_file = get_file(create=False)
        view_mad_lib(in_file)

    # quit option selected
    else:
    # exit the loop and program
        break

    if __name__ == "__main__":
main()
