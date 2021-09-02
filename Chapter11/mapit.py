#mapIt.py - Launches a map in the browser using an address from the 
#command line or clipboard

import sys, webbrowser,pyperclip

if len(sys.argv) > 1:  # if there is one argument in the command line , do the following
    #Get address from command line.
    address = ' '.join(sys.argv[1:])    # all data will be placed in one string for argument
else:                                        # [1:] chops of the first array off data
#TODO: Get address from clipboard
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)