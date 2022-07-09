Open Several links in diffrent tabs automatically of the top search topics.

This is what your program does:
   - Gets search keywords from the command line arguments.
   - Retrieves the search results page.
   - Opens a browser tab for each result.
This means your code will need to do the following:
   - Read the command line arguments from sys.argv.
   - Fetch the search result page with the requests module.
   - Find the links to each search result.
   - Call the webbrowser.open() function to open the web browser.