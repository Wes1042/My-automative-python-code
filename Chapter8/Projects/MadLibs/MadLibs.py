'''Reads the text filesand lets the user add their own text replacing
ADJECTIVE |NOUN|ADVERB| VERB 
'''
import re , os

text_file = open('madlib.txt')                          # Open file madlibs.txt
content = text_file.read()                              # read the file 

locate = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')      # locate the following 

while True:                                             # while locate is working do the folllowing 
    results = locate.search(content)                    # locate the words in the context
    if results == None:                                 # if nothing was foound , breal
        break

    if results.group() == 'ADJECTIVE' or results.group() == 'ADVERB':       # if found the word print the found word
        print('Enter an %s:' % (results.group().lower()))
    elif results.group() == 'NOUN' or results.group() == 'VERB':
        print('Enter an %s:' % (results.group().lower()))

    word = input()                                                          # when a word is found the user will input
    content = locate.sub(word,content,1)                                    # subtitute the input with the word from our content block
print(content)                                                              # print the new content

print('Creating a new file name: ')                                         
name = input()                                                              # creating a new file to store the new content
newFile = open('%s.txt' % (name), 'w') 
newFile.write(content)
newFile.close()