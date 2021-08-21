import os , shutil

def selCopy(folder,extension):
    
    folder = os.path.relpath(folder)

    number = 1 

    while True:
        try:
            newFolder = '%s_files_' % (extension.upper() + str(number))
            os.makedirs('.\\%s' % (newFolder))
            break
        except: 
            number += 1

    print("Creating %s..." % (os.path.relpath(newFolder)))

    for foldername, subfolder, filenames in os.walk(folder):
        if os.path.basename(foldername) == newFolder:
            continue
        print("Searchin for %s " %(extension.upper()) + "files in %s..." % (foldername))

        for filename in filenames:
            if filename.endswith('.%s'% (extension)):
                shutil.copy(os.path.join(foldername, filename), newFolder)
    return newFolder


print('Enter the file extension that you wish to copy')
extension = input()
newFolder = selCopy('.', extension.lower())
try:
	os.rmdir(newFolder)
	print("No %s files found." % (extension.upper()))
except:
	print("Done! Folder created!")


'''
while selCopy == True :
    os.rmdir(newFolder)
    print('No %s files were found.' % (extension.upper()))
else:
    print('Done! Folder has been created')
'''