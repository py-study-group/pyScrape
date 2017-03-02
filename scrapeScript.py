# The urllib.request module defines functions and classes which help in opening URLs
from urllib.request import urlopen

my_address = "https://realpython.com/practice/aphrodite.html"
html_page = urlopen(my_address)

html_text = html_page.read().decode('utf-8')

print(html_text)
