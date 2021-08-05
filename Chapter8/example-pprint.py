'''Saving Variables with the pprint.pformat()Function '''

#It is a function to make data/strings prettier and easy to read 
import pprint                   #importing pretty print
cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc':'fluffy'}] # setting a array/ variables
print(pprint.pformat(cats))         #allows us to keep the list in cats available even after closing 
fileObj = open('myCats.py', 'w')     #Create myCats.py and write
print(fileObj.write('cats = ' + pprint.pformat(cats)+'\n')) # write whats in cats to new file 

fileObj.close()
# this will create a cache module/ folder. This is where the data is being
# pulled from 