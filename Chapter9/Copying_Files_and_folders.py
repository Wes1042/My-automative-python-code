import shutil, os 

# Basically the unix command cp src dst. 
# this copies the source file to the destination directory
# the destination directory has to exist
os.chdir('C:\\')
shutil.copy('C:\\spam.txt', 'C:\\delicious') #shutil.copy( 'source' ,'destination')
# copies the contents of egg.txt and sends it to destination with new name 
shutil.copy('egg.txt', 'C:\\delicious\\eggs2.txt' )

'''.copytree'''
# shutil.copy will only copy one file while copy tree will copy and entire folder
os.chdir('C:\\')
shutil.copytree('C:\\bacon' , 'C:\\bacon_backup')
