'''
Website URL searcher
                pseudo code
    1) Get the text off the clipboard
    2) Find all URLs in the text.
    3) Paste them into the clipboard

'''
import re , pyperclip
#TODO: URL Regex
#UrlRegex = re.compile(r'(http|ftp|https):\/\/([\w\-_]+(?:(?:\.[\w\-_]+)+))([\w\-\.,@?^=%&:/~\+#]*[\w\-\@?^=%&/~\+#])?',re.VERBOSE)
UrlRegex = re.compile(r'''(
    (http|ftp|https)
    :\/\/
    ([\w\-_]+(?:(?:\.[\w\-_]+)+))
    ([\w\-\.,@?^=%&:/~\+#]*[\w\-\@?^=%&/~\+#])?


)
''',re.VERBOSE)

#TODO: copy

text = str(pyperclip.paste())
matches = []
for groups in UrlRegex.findall(text):
    matches.append(groups[0])

#TODO: PASTE
if len(matches)> 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else: 
    print('There was no URL ')

