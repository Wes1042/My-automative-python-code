print('This program will delete files based on how file big the files are')  
print('If they are larger than 100MB then they can be deleted')

import os 

def delFiles(folder,size):          # it will delete the file size the user inputs
    folder = os.path.abspath(folder)
    while True:
        
        for foldername,subfolder,filenames in os.walk(folder):
            for filename in filenames:

                full_path = os.path.join(foldername,filename)
                print('Deleting %s'% (foldername))
                if os.path.getsize(full_path) > size:
                    os.unlink(full_path)
                    print('File Removed')
                else:
                    print('File was not removed')
        return folder

        # if folder is bigger thatn size : 
        #          


size = int(input('Enter the size in MB: ')) * 10**6
folder = delFiles('.\\.', size)
print('Done')


