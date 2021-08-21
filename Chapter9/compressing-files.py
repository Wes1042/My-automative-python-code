'''Compressing files with the zipfile Module '''
# The module doesnt unzip but it read the contents inside
import zipfile,os

os.chdir('C:\\') # moves to the folder with example.zip
exampleZip= zipfile.ZipFile('example.zip')
print(exampleZip.namelist())

spamInfo = exampleZip.getinfo('spam.txt')
print(spamInfo.file_size)

(spamInfo.compress_size)
#Giving information about the file and finding the diffrence between the compressed and non compressed
print('compressed file is %sx smaller!' % (round(spamInfo.file_size / spamInfo.compress_size,2 )))

exampleZip.close()

'''Extracting from ZIP Files '''
''' use your basic setup''' 
#import zipfile,os
os.chdir('C:\\') # moves to the folder with example.zip
exampleZip= zipfile.ZipFile('example.zip')
exampleZip.extractall()         # will extract within the directory
exampleZip.close()

#----------------------------
exampleZip.extract('spam.txt')

exampleZip.extract('spam.txt', 'C:\\some\\new\\folders')

exampleZip.close()
