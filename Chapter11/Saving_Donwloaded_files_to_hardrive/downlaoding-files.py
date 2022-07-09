''' get.request()'''
import requests
res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
print(type(res))

print(res.status_code == requests.codes.ok) # checking if it recieved data

print(len(res.text))

print(res.text[:250])

#-----------------------------
'''Checking for Errors'''
res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
#res.raise_for_status() # This is used to compltly stop the program if an error occurs
# You can combine try exept if the download won't affect you
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' %(exc)) # will paste the exeption log of the file being downloaded.

'''Saving Downloaded Files to the Hard Drive'''
# You have to save in binary formate for encoding
res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
print(res.raise_for_status)
playFile = open('RomeoAndJuliet.txt' , 'wb')
for chunk in res.iter_content(100000): # each iteration through the loop
    playFile.write(chunk)
    playFile.close()

    #  each chunk is in byte data type ,100000 is an example of good data
    