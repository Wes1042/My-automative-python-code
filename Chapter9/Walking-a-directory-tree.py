'''You can rename a folder and folders inside  '''
#You can use the fucntion walk to see all folders inside the folder
import os 
# setting path to read 
for folderName, subfolders, filenames in os.walk('C:\\delicious'):    

    print('The current folder is ' + folderName)
    # prints out the folder of the path it is in
# loops and print all files and folders inside the folder
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)
    print('')