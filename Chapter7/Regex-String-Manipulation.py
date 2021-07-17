import re
'''Case-Insesitive Matching '''
# You can use re.IGNORECASE or re.I to ignore case sensitive searches
robocop = re.compile(r'robocop', re.I)
ro = robocop.search('Robocop is part man, part machine, all cop.')
print(ro.group())
ro = robocop.search('ROBOCOP protects the innocent.')
print(ro.group())
ro = robocop.search('Al, why does the programming book talk about robocop so much?')
print(ro.group())

'''Subsituting strings with eht sub()method '''
# REGEX can match patterns and words , and they can be used to subsitude strings
nameRegex = re.compile('Agent \w+')
sub = nameRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
print(sub)
# This will replace all words that have been specified 
agentNameRegex = re.compile(r'Agent (\w)\w*') # Match "Agent " with their other name
# replace all other charcters but the first 
agent = agentNameRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent')
print(agent)

'''Managing Complex Regexes'''
# Regex can get complicated , you can specify it to ignore white spaces and comments
# it is called Verbose Mode , use dby re.verbose as the secconds argument in re.compile

# Normally you would write regex expression as : 
phoneRegex= re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')

# This is troublesome and can get really messy to understand 
# There is an easier eye appealing way

phoneRegex = re.compile(r'''(
    (\d{3}|\(d{3}\))?           # area code
    (\s|-|\.)?                  # seperator
    \d{3}                       # First 3 digits 
    (\s|-|\.)                   #seperator
    \d{4}                       #Last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?
)''', re.VERBOSE)
# We use ''' instead of one ' . This can help us organize and make it clearer to read

'''Combining re.IGNOREXASE, re.DOTALL, and re.VERBOSE'''
