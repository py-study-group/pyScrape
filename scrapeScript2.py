# The urllib.request module defines functions and classes which help in opening urls
from urllib.request import urlopen

# The url we want to target
my_address = "https://realpython.com/practice/aphrodite.html"
# with urlopen we open the url we want(my_address)
html_page = urlopen(my_address)
# we store the content of the website
html_text = html_page.read().decode('utf-8')

# the start of the tag we want
start_tag = "<title>"
# the end of the tag we want
end_tag = "</title>"

# OK this is little tricky
# we find the start of the tag
# and we add the length of the tag
# so we can print after the tag
# in our case after <title>
start_index = html_text.find(start_tag) + len(start_tag)
# until where we want to print
end_index = html_text.find(end_tag)

# We print after <title> and before </title>
print(html_text[start_index:end_index])
