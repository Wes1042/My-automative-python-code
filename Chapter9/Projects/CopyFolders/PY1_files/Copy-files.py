import os ,shutil 

print('This program will search for file extension you input. The "." is not neccesary')
print('You can search for what ever extention , some common extenstions are')
print('.pdf .js .py .cvs .doc .java ')
def selCopy(folder,extension):
    folder = os.path.relpath(folder)        # relative path to where this program is run
    N = 1 

    #TODO: Creating the folder name
    while True:
        try:
            newFolder = '%s_files'  % (extension.upper() + str(N)) # creating name with number of file
            os.makedirs('.\\%s'%(newFolder))        # creating the folder 
            break
        except:
            N += 1      # if the file all ready exist break , if not then add a new number for file 
    
    print('Creating %s...' % (os.path.relpath(newFolder)))

    #TODO: Saving the folders and files using the os.walk
    # for the folders , subfolder and files , find the file that ends with . userinput
    for foldername,subfolder,filenames in os.walk(folder):
        if os.path.basename(foldername) == newFolder:
            continue
        print('Searching for %s '% (extension.upper())+ 'files in %s...' % (foldername))

        for filename in filenames :
            if filename.endswith('.%s'%(extension)):
                shutil.copy(os.path.join(foldername,filename), newFolder)
    return newFolder

print('Enter the file extension that you wish to copy: ')
extension = input()
newFolder = selCopy('.', extension.lower())
try:
    os.rmdir(newFolder)
    print('No %s file were found.' % (extension.upper()))
except:
    print('Done Folder Created')


# Things that can be extended :
    # 1. Ask the user how many extensions they wish to look for and save them inside an oganized folder
    # 2. Make a module that can be used in other programs
    