'''
Strong Password Detection
Write a function that uses regular expressions to make sure the password
string it is passed is strong. A strong password is defined as one that is at
least eight characters long, contains both uppercase and lowercase
characters, and has at least one digit. You may need to test the string against
multiple regex patterns to validate its strength.

            psedo code 
        1) create a regex that defines the password 
        2) create variable with string input or variable placement
        3)create an if statement that if the password matches 
        it is strong , if else not strongg
'''
import re
#password = '123'                                   
password = 'K#cFt78@1'      # random password i took from the internet
passwordRegex = re.compile(r'^(?=.*[A-Z](?=.*[a-z])(?=.*[0-9])(?=.*[!@#$%^&*-_?]).{7,}$)',re.VERBOSE) # create a regex with specification
                                                        
passwordd = passwordRegex.search(password)
 
if (not passwordd):                        
    print(password)              
    print('Your password is weak ' )

else: 
    print(password)
    print('your password is strong ')