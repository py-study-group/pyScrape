
# I've found out that you can use the
# BeautifulSoup module to get values
# of multiple tags in a web page
# without using regular expressions.

# Antergos 64bit
# Created a virutal environment
# For Python 3 I had to install BeautifulSoup4
# pip install beautifulsoup4
# Also had to install requests
# pip install requests

import requests
from bs4 import BeautifulSoup

# Returns a list of all <a> tag
# values as a list
def get_anchor_values(url):

    # get the web page source
    request = requests.get(url)
    source = request.text

    # parse the source into a BeautifulSoup object
    soup = BeautifulSoup(source, 'html.parser')

    # findAll returns a ResultSet object
    anchors = soup.findAll('a')

    ret_list = []

    # Each anchor is a Tag object
    # https://www.crummy.com/software/BeautifulSoup/bs4/doc/#tag
    for anchor in anchors:
        # anchor.contents is a list
        # and we need to get a first element
        ret_list.append(anchor.contents[0])

    return ret_list


def main():

    url = 'https://realpython.com/practice/profiles.html'

    for val in get_anchor_values(url):
        print(val)


if __name__ == '__main__':
    main()
