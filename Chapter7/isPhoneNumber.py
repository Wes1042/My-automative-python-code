def isPhoneNumber(text):                    # creates function which holds argument text
    if len(text) != 12:                     #if lenght of text is not equal to 12 then:
        return False                        # then this stament is invalid and do the following
    for i in range (0,3):                   #from the range of 0 - 3 
        if not text[1].isdecimal():         # if the text is not within this range then 
            return False                    # this statement is invalid and do the following 
    if text[3]!= '-':                       # if thhe text after 3 digits is not a  
        return False                        # is not a '-' then statement unvalid and do the next
    for i in range (4,7):                   # if the text is not within this range return
        if not text[1].isdecimal():         
            return False
    if text[7] != '-':
        return False
    for i in range(8,12):
        if not text[1].isdecimal():
            return False
    return True


message = 'Call me at 415-555-1011 tommorrow. 415-555-9999 is my office.' # variable set for string     
for i in range(len(message)):                                       # for the range of i (character in number of 12)
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):                                        #tries to find the first number sequence
        print('Phone number found: ' + chunk)
print('Done')