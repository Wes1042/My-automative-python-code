This chapter cover web scraping 
we will be using multiple modules 

webrowser being one of them

mapit.py project
writing a simple script to automatically launch the map in your browser using the contents of your clipboard. This way, you only have to copy the address to a clipboard and run the script, and the map will be loaded for you.

This is what your program does:
Gets a street address from the command line arguments or clipboard.
Opens the web browser to the Google Maps page for the address.



This means your code will need to do the following:
Read the command line arguments from sys.argv.
Read the clipboard contents.
Call the webbrowser.open() function to open the web browser.