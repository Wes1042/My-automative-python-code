# renameDates.py - Rename filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY

import shutil, os , re

# TODO: Create a regex that matches files with the Amercian date format.
# The regular expression string begins with ^(.*?) to match any text at the
#beginning of the filename that might come before the date.

datePattern = re.compile(r"""^(.*?)     # All text before the date
    ((0|1)?\d)-                         # one or two digits for the month
    ((0|1|2|3)?\d)-                     # one of two digits for the day        
    ((19|20)\d\d)                       # four digits for the year
    (.*?)$                             # all text after the date

""",re.VERBOSE)
''' 
To understand which group is whihc , this example will help:

datePattern = re.compile(r"""^(1)           # all text before the date
(2 (3) )-                                   # one or two digits for the month
(4 (5) )-                                   # one or two digits for the day
(6 (7) )                                    # four digits for the year
(8)$                                        # all text after the date
""", re.VERBOSE)

'''

# TODO: Loop over the files in the working directory.
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)   # search for the american file 
    # TODO: Skip files without a date.
    if mo == None:      # if the file doesnt match with regex , ignore
        continue
# TODO: Get the diffrent parts of the filename.
beforePart = mo.group(1)    #We will use these groups to manipulate data
monthPart = mo.group(2)
dayPart = mo.group(4)
yearPart = mo.group(6)
afterPart = mo.group(8)

# TODO: Form the European-style filename.  
# manipulating our group data
euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart
# randomTextDD-MM-YYRandomText
# TODO: Get the full, absolute file path.
absWorkingDir = os.path.abspath('.')
amerFilename = os.path.join(absWorkingDir, amerFilename)
euroFilename = os.path.join(absWorkingDir, euroFilename)
# TODO: Rename the files.  
print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
#shutil.move(amerFilename, euroFilename) # uncomment after testing