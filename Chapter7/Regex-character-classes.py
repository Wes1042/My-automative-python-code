import re
import _sre
'''
            Characters classes
\d Any numeric digit from 0 to 9.
\D Any character that is not a numeric digit from 0 to 9.
\w Any letter, numeric digit, or the underscore character. (Think of this as
matching “word” characters.)
\W Any character that is not a letter, numeric digit, or the underscore character.
\s Any space, tab, or newline character. (Think of this as matching “space”
characters.)
\S Any character that is not a space, tab, or newline
'''
xmasRegex = re.compile(r'\d+\s\w+') # Finds all digits , space , and words 
so = xmasRegex.findall('12 drummers, 11 pippers , 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 patridge')
print(so)

vowelRegex = re.compile(r'[aeiouAEIOU]') # Find all characters / vowels from this data
so1 = vowelRegex.findall('Robocop eats baby food. BABY FOOD.')
print(so1)

'''The Caret and Dollar Sign Characters'''
'''These are used to identify the first and last arguments in the raw data'''
# carrot ^
beginWithHello = re.compile(r'^Hello')
so2 = beginWithHello.search('hello World!')
print(so2)
#_sre.SRE_Match object; span=(0, 5), match='Hello'
so3 = beginWithHello.search('He said hello.') == None 
print(so3)

###############
# $ dollar sign 
endswithNumber = re.compile(r'\d$') #compile the raw data from this digit notation
endswithNumber.search('Your number is 42')
#_sre.SRE_MATCH object; span=(16, 17), match='2'
so4 = endswithNumber.search('Your number is forty two.') == None
print(so4)

# This will combine both 
# Tis claims that it found a match for the digits
wholestringIsNum = re.compile(r'^\d+$')
wholestringIsNum.search('1234567890')
#_sre.SRE_MATCH object; span=(0,10), match='123456789'
so5 = wholestringIsNum.search('1234xyz67890') == None
print(so5)
so6 = wholestringIsNum.search('12 34567890') == None
print(so6)

'''The Wildcard Character'''
#finds words that have the letters from raw data
#from first letter to where the raw data says to find
#This method uses the greedy mode aka will try to match any and all text 
atRegex =re.compile(r'.at')
so7 = atRegex.findall('The cat in the hat sat on the flat mat.')
print(so7)
'''Match everything with Dot-Star'''
nameRegex=re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group(1))
print(mo.group(2))
print(mo.groups())

# To make non-greedy
nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve a man> for dinner.')
print(mo.group())

nongreedyRegex = re.compile(r'<.*>')
mo = nongreedyRegex.search('<To serve a man> for dinner.>')
print(mo.group())

'''Matching Newlines with the Dot character '''
# You can match everything except a new line by using re.DOTALL

noNewLineRegex = re.compile('.*')
mo3 = noNewLineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')
print(mo3.group())


newlineRegex = re.compile(r'.*', re.DOTALL)
mo4 = newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')
print(mo4.group())