import zipfile
newZIP = zipfile.ZipFile('new.zip', 'w')
newZIP.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
newZIP.close()
# it is similar to opening a file using the OS module