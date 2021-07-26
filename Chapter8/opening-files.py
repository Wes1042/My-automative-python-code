import os
# to open a text file and read its content use open
hellofile = open('C:\\Users\\Wesley\\Documents\\GitHub\\My-automative-python-code\\Chapter8\\hello.txt')
print(hellofile)
# The default open does the read option , you can specify it or do other things
print(open('.\\hello.txt ', 'r'))

# Reading the Contents of FIles 
# this is used to print a single line
helloContent = hellofile.read()
print(helloContent)

# to print for multiple lines use readlines
helloContent = hellofile.readline()
print(helloContent)

sonnetFile = open('.\\sonnet29.txt')
print(sonnetFile.readlines())

# Writing to Files
# Append adds on to the text while write overwrites the existing contents 
# You chould always close the file using close() before opening it again

baconfile = open('baconfile.txt' , 'w') # open and overwrite / create the following
baconfile.write('Hello World!\n')  
print(baconfile)
baconfile.close()
baconfile = open('baconfile.txt' , 'a')     # open and append the following 
baconfile.write('Bacon is not a vegetable.')
baconfile.close()
baconfile = open('baconfile.txt')               # open and read the content
content = baconfile.read()
baconfile.close()
print(content)


