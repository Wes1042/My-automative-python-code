import os
one = os.path.join('usr', 'bin', 'spam')
print(one)

myFiles = ['accounts/txt', 'details.csv' , 'invite.docx']
for filename in myFiles:                # for the new variable of filename from my files
    print(os.path.join('C:\\Users\\wes', filename))

print(os.path.abspath('.'))
print(os.path.abspath('.\\Scripts'))
print(os.path.isabs('.'))


print(os.path.relpath('C:\\Windows' , 'C:\\'))

print(os.getcwd())


'''Creating New Folders with os.makedirs()'''

# os.makedirs('C:\\delicious\\walnut')

''''Os.Path module '''
path = 'C:\\Windows\\System32\\calc.exe'
print(os.path.basename(path))
print(os.path.dirname(path))

# to see a tuple / array list 
calcFilePath = 'C:\\Windows\\System32\\calc.exe'
print(os.path.split(calcFilePath))

# to seperate each directory 
print(calcFilePath.split(os.path.sep))

'''Finding File Sizes and Folder Contetns'''

print(os.path.getsize('C:\\Windows\\System32\\calc.exe'))


print(os.listdir('C:\\Windows\\System32'))

# How to find the total size 
totalSize = 0 
for filename in os.listdir('C:\\Windows\\System32'):
    totalSize = totalSize + os.path.getsize(os.path.join('C:\\Windows\\System32' ,filename)) # combine all file sizes into one and print
print(totalSize)

# checking path validity

print(os.path.exists('C:\\Windows'))
print(os.path.isfile('C:\\some_made_up_folder'))
print(os.path.isdir('C:\\Windows\\System32'))
print(os.path.isfile('C:\\Windows\\System32'))

# to check for the existance of other drives / files do
print(os.path.isdir('D:\\'))
