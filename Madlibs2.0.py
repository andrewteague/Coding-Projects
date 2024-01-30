#########################
#Andrew Teague
# 9/26/22
#Madlibs story
############################

Welcome_text = """
Welcome to the game of Mad Libs.
I will ask you to provide various words and phrases to fill in a story.
The result will be written to an output file.
"""
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


def handlesUserimputs(line):
    newline = ''
    start = 0
    end = 0
    for idx in range(len(line)):
        if line[idx] == "<":
            start = idx
        elif line[idx] == '>':
            end = idx + 1
            token = line [start + \: end]
            if token [0] in vowels:
                new_word= input('gimme an {token}')
            eliuf token [0] in vowels:\
                new_word = input('gimme an {token}')
        return  newline











def main():
    print(Welcome_text)



