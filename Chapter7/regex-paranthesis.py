import re
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)') #set pattern in groups
mo = phoneNumRegex.search('My number is 415-555-4242.')   # search for groups 
print(mo.group(1)) #first group '415'
print(mo.group(2))  #seccond group '555-4242'
print(mo.group(0))  #All together 
print(mo.group())   #All together
print(mo.groups())  # print all groups (non clean)

areaCode , mainNumber = mo.groups() # sets variables to groups
print(areaCode)
print(mainNumber)
#This is used for paranthesis Regex
phoneNumRegexParanthesis = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo1 = phoneNumRegexParanthesis.search('My phone number is (415) 555-4242.')
print(mo1.group(1))