Tranform American style dates to European style dates
American style : (MM-DD-YYYY)
European styLE : (DD-MM-YYYY)

Steps on how to do this :

Create a REGEX that can identify the text pattern of American-Style dates.
Call os.listdir() to find all the files in the working directory
loop over each file name, using regex to check whether it has a date.
If it has a date, rename the file with the shutil.move()



The regular expression string begins with ^(.*?) to match any text at the
beginning of the filename that might come before the date.

The group for the day is
((0|1|2|3)?\d) and follows similar logic; 3, 03, and 31 are all valid
numbers for days.



The (.*?)$ part of the regex will match any text that comes after the date.