'''Saving Variables with the shelve Module '''
# Pyhton can program to binary shelf files 
# can be used to restore data to variables from the hdd
# can be used for automation as in saving shelf files and when they run , use the same variables

import shelve
shelFile = shelve.open('mydata')        # create a file called mydata
cats = ['Zophie', 'Pooka', 'Simon']     # add data to that file that has been open and made
shelFile['cats'] = cats                 # create a specification/list for that data stream
shelFile.close()                        # close the file to prevent any more data 


shelFile = shelve.open('mydata')        # open file mydata which are .bak , .dat , .dir
print(type(shelFile))                   # identify the file type 
print(shelFile['cats'])                 # print the content specification
shelFile.close()                        # close the file 

# We can use keys and values to return list like values 
shelFile = shelve.open('mydata')        # open mydata file
print(list(shelFile.keys()))            # print the catagory/ key
print(list(shelFile.values()))          # print the list/ values insode that catagory/key
shelFile.close()                        # close the file 