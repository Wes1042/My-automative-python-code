# backupToZip.py - copies an entire folder and its contetns into
# a ZIP file whose filename increments.
# This will save the zip files in the folder this program is located in
# You can change where the zip file is located by specifing the path in folder
import zipfile , os 

def backupToZip(folder):      # we are creating a function that will store all of out calls
    # Backup the entire contents of "folder" inot a ZIP file.

    folder = os.path.abspath(folder) # make sure folder is absolute

    # Figure out the filename this code should based on 
    # What files already exist

    number = 1
    while True:             #while the fucntion is called do the following 
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip' # grab the file name and create a number extension
        if not os.path.exists(zipFilename): # if the file exitst , break 
            break
        number = number + 1     # everytime a new file is made , increase the file name
    

    # TODO: Create the ZIP file.
    print('Creating %s...' % (zipFilename))         # creating a string to display new file
    backupZip = zipfile.ZipFile(zipFilename, 'w') # updating and creating the new zip

    # TODO: Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        # Add the current folder to the ZIP file.
        backupZip.write(foldername)
        # Adding all the files in this folder to the ZIP file.  
        for filename in filenames:
            if filename.endswith('.py') and filename.endswith('.txt'):
                continue # Don't backup the backup zip files.
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done.')

backupToZip('C:\\delicious')

