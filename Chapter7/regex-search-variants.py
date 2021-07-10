import re
heroRegex = re.compile (r'Batman|Tina Fey.')
mo1 = heroRegex.search('Batman and Tina Fey.')
print(mo1.group())

mo2 = heroRegex.search('Tina Fey and Batman')
print(mo2.group())

#It outputs the first name that it finds 


#Using Regex to find one prefix for all 
# ex : batman | batmobile etc
# we want the prefix bat

batRegex = re.compile(r'Bat(man|mobile|copter|bat)') #If the search finds a match of either one 
mo = batRegex.search('Batmobile lost a wheel')       # print 
print(mo.group())
print(mo.group(1))


# optional matching 
batRegex = re.compile(r'Bat(wo)?man')
mo3 = batRegex.search('The Adventures of Batman')
print(mo3.group())

mo3 = batRegex.search('The Adventures of Batwoman')
print(mo3.group())

#The (wo)? part of the regular expression means that the pattern wo is an optional group


# Using phoneregex example to look for phone numbers that may or may not have are code
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo4 = phoneRegex.search('My number is 415-555-4242')
print(mo4.group())                                  #optional matches 
mo4 = phoneRegex.search("My number is 555-4242")
print(mo4.group())


#Matching zero or more with the star/multiplier
#The * (called the star or asterisk) means “match zero or more” — the group
#that precedes the star can occur any number of times in the text.

batRegex = re.compile(r'Bat(wo)*man')
mo5 = batRegex.search('The Adventures of Batman')
print(mo5.group())

mo6 = batRegex.search('The Adventures of Batwoman')
print(mo6.group())

mo7 = batRegex.search('The Adventures of Batwowowowoman')
print(mo7.group())

# matches the optional multiple times to be acceptable 

#Matching one or more with the Plus 
#While * means “match zero or more,” the + (or plus) means “match one or
#more.” Unlike the star, which does not require its group to appear in the
#matched string, the group preceding a plus must appear at least once.

batRegex = re.compile(r'Bat(wo)+man')
mo8 = batRegex.search('The Adventures of Batwoman')
print(mo8.group())

mo9 = batRegex.search('The Adventures of Batwowowoman')
print(mo9.group())

mo10 = batRegex.search('The Adventures of Batman')
print(mo10 == None)


# Matching Specific Repetition with curly Brackets 
#Instead of one number, you can specify a range by writing a minimum, a comma
#For example, (Ha){3,} will match three or more instances of the (Ha) group, while (Ha){,5} will match zero to five instances
haRegex = re.compile(r'(Ha){3}')
mo11 = haRegex.search('HaHaHa')
print(mo11.group())
mo12 = haRegex.search('Ha')
print(mo12 == None)

#Search matches of 3 + 
hahRegex = re.compile(r'(ha){3,}')
mo13 = hahRegex.search("hahahahahah")
print(mo13.group())
# Search mathces of 0 -5
hahaRegex = re.compile(r'(ha){,5}')
mo14 = hahaRegex.search("hahahah")
print(mo14.group())


#Greedy and NonGreedy Matching
#By default it will choose the highest first
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo15 = greedyHaRegex.search('HaHaHaHaHa')
print(mo15.group())
# we had to set the lowest first
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo16 = nongreedyHaRegex.search('HaHaHa')
print(mo16.group())

# Search vs Findall

#Search has been used to find the first match but Find all is used to give all matches
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo17 = phoneNumRegex.search('Cell : 415-555-9999 Work: 212-555-0000')
print(mo17.group())

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') #no groups 
mo18 = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo18)

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') #has groups
mo19 = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo19)