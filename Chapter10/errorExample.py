'''
This is the normal traceback in an IDE
def spam():
    bacon()
def bacon():
    raise Exception('This is the Error message.')

spam()
'''
# ----------------------------------------------------
'''using traceback in our code '''

import traceback 
try:
    raise Exception('This is the error message.')
except:             # try the expetion that is delcared with the except
    errorFile = open('errorInfo.txt' , 'w')
    print(errorFile.write(traceback.format_exc()))
    errorFile.close()
    print('The traceback info was written to errorInfo.txt.')