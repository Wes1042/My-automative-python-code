''' Notes in how it should work 
                Pseudo code
    1) Get the text off the clipboard
    2) Find all phone numbers and email addresses in the text.
    3) Paste them into the clipboard
'''
import re, pyperclip
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))               # area code
    (\s|-|\.)?                      # seperator
    (\d{3})                         # First 3 digits 
    (\s|-|\.)                       # seperator 
    (\d{4})                         # Last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
)''',re.VERBOSE)

# TODO: create email regex.
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+               # username ( a -z & A -Z & 0 - 9 special symbols : . _ % + -)
    @                               # @ symbol
    [a-zA-Z0-9.-]+                  # domain name 
    (\.[a-zA-Z]{2,4})               # dot something   
# example@exampledomain.something
)''',re.VERBOSE)



# TODO: Find matches in clipboard text.
text = str(pyperclip.paste())                               # create text variable that paste data
matches = []                                                # create variable where final ouput will be stored
for groups in phoneRegex.findall(text):                     # for the groups/index of the text do the following
    phoneNum = '-'.join([groups[1],groups[3],groups[5]])    # combine area code , first 3 digits , last 4 digits and extension
    if groups[8] != '':                                     # if group 8 does not have a empty string do 
        phoneNum += ' x' + groups[8]                        # add x/ extention to group 8
    matches.append(phoneNum)                                # combine group 1 ,3 , 5 ,8
for groups in emailRegex.findall(text):
    matches.append(groups[0])                               # show the whole email 


# TODO: Copy results to the clipboard 

if len(matches) > 0:                                        # if matches has more than 1 do:
    pyperclip.copy('\n'.join(matches))                      
    print('Copied to Clipboard:')
    print('\n'.join(matches))                               # paste what is in the matches in a new line
else:
    print('No phone number or email addresses found.')