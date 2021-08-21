'''Deleting any file with the extension given in the directory set '''
import os 

for filename in os.listdir():
    if filename.endswith('.rxt'):
       # os.unlink(filename)
       if True:
           print('The file you want to delete is ' + filename)
       if False:
            print('This file does not exist')

''' Safe delete by sending to trash instead of delting forever  '''
# You have to install the module with pip install send2trash
import send2trash
baconFile = open('bacon.txt', 'a') # creates the file 
baconFile.write('Bacon is not a vegetable')
baconFile.close()
send2trash.send2trash('bacon.txt')