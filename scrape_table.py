
import requests
from bs4 import BeautifulSoup, Tag
from bs4.element import ResultSet
from unidecode import unidecode

# Print the list of the recently updated
# packages from Python Package Index main page.


# Return web page source
# as a BeautifulSoup object
def get_soup(url):

    # get the web page source
    request = requests.get(url)
    source = request.text

    # parse the source into a BeautifulSoup object
    return BeautifulSoup(source, 'html.parser')


# Return a two dimensional list
# containing table cells
# This only works if I know table dimensions
# and contents in advance
def get_table(url, index):

    table = None
    ret_value = list()

    soup = get_soup(url)
    tables = soup.find_all('table')

    if isinstance(tables, ResultSet):
        if 0 <= index <= len(tables) - 1:
            table = tables[index]

    if not table is None:
        for row in table.find_all('tr'):
            cell_list = list()
            cells = row.find_all('td')
            # I know that each row has 3 cells
            # and that the second cell contains
            # an ancor tag with Unicode characters
            if len(cells) == 3:
                cell_list.append(cells[0].contents[0])
                anchor = cells[1].contents[0]
                cell_list.append(unidecode(anchor.contents[0]))
                cell_list.append(cells[2].contents[0])
            ret_value.append(cell_list)
    
    return ret_value


def main():

    url = 'https://pypi.python.org/pypi'
    table = get_table(url, 0)

    if not table is None:
        for row in table:
            print(row)


if __name__ ==  '__main__':
    main()
    
