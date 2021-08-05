'''
The program will do:
    The command line argument for the keyword is checked.
    If the argument is save, then the clipboard contents are saved to the
    keyword.
    If the argument is list, then all the keywords are copied to the clipboard.
    Otherwise, the text for the keyword is copied to the keyboard.
    This means the code will need to do the following:
    Read the command line arguments from sys.argv.
    Read and write to the clipboard.
    Save and load to a shelf file.
'''

# mcb.pyw - Saves and load pieces of the text to the clipboard
# Usage: py.exe mcb.pyw save <keyword> - saves clipboard to keyword
#        py.exe mcb.pyw <keyword> - loads keywords to clipboard
#        py.exe mcb.pyw list - Loads all keywords to clipboard
#        py.exe mcb.pyw delete <keyword> - Deletes keyword from shelf
#        py.exe mcb.pyw deleteall - Deletes all keywords from shelve

# This creates arguments that the code can follow , it is like flags that set code in place
# can be used for programs with multiple uses
'''This program will save all set valuables to a shell file and when prompted
combine them and copy them to the clipbaord '''
import shelve, pyperclip, sys
# 3 = (argument 3)set keyword
# 2 = (argument 2)load kwyword
# 1 = (argument 1)save keyword
# mcb.pyw _____ ______ _____     <--- the underscores are considered arguemnts and we can use up to 3 
mcbShelf = shelve.open('mcb')               # Create a shell file called mcb

# TODO: Save clipboard content.                     argv = argument vector (array of strings)
if len(sys.argv) == 3 and sys.argv[1].lower()== 'save':    # if the ammount/len of arugments is 3 and argument 1 is == save do the following
    mcbShelf[sys.argv[2]] = pyperclip.paste()              # paste keyword (argument 2) to the shell file   
# TODO: Create a delete keyword
elif len(sys.argv) == 3 and sys.argv[1].lower()== 'delete': # if the ammount of arguments is 3 and argument 1 is == delete do the following
    del mcbShelf[sys.argv[2]]                               # delete the keyword in argument 2 from mcbshelf
elif len(sys.argv) == 2:                                   # else if argument 2 aka keyword is used do:
# TODO: List Keyword and load content                    # The following is conditions used only when we are using 2 keywords like list and delete
    if sys.argv[1].lower() == 'list':                      # if using argument 1 aka keyword list do :  
        pyperclip.copy(str(list(mcbShelf.keys())))         # copy the keys/values of the list and make it into a string
    # TODO: Create a delete all in content
    elif sys.argv[1].lower() == 'deleteall':                # else if arguemnt 1 is deleteall do:
        for keyword in list(mcbShelf.keys()):               # keywords is = to mcbshelf keys
            del mcbShelf[keyword]                           # delete keywords
    
    elif sys.argv[1] in mcbShelf:                           # else if argument 1 in file mcbshelf do :
        pyperclip.copy(mcbShelf[sys.argv[1]])               # copy the contents of argument 1 to clipboard


mcbShelf.close()