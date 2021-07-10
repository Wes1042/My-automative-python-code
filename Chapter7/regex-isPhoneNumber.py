import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # identification pattern that will be used
mo = phoneNumRegex.search('My number is 415-555-4242.') # search this string with regex
print('Phone number found: ' + mo.group()) #print the output of mo 

# since we know we can get a match instead of a null , then mo.group to retun the match
#1. Import the regex module with import re.
#2. Create a Regex object with the re.compile() function. (Remember to use a raw string.)
#3. Pass the string you want to search into the Regex object’s search() method. This returns a Match object.
#4. Call the Match object’s group() method to return a string of the actual matched text.