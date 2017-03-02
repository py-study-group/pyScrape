# The urllib.request module defines functions and classes which help in opening URLs
from urllib.request import urlopen
# The url we want to target
my_address = "https://realpython.com/practice/aphrodite.html"
# with urlopen we open the url we want(my_address)
html_page = urlopen(my_address)
# we store the content of the website
html_text = html_page.read().decode('utf-8')
# print the content of html_text
print(html_text)
