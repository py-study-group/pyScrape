# Scrape and Parse Text From Websites

Collecting data from websites using an automated process is known as web scraping.
Some websites explicity forbid users from scraping their data with automated tools.

### This is happening for two possible reasons:

* The site has to protect its data, Google maps will not allow you to request too many results too quickly
* Making many repeated requests to a website's server may use up bandwidth, slowing down the website and potentially overloading the server.

### You need to be familiar with the basics of HTML

* [Incase you are not familiar](https://www.sitepoint.com/web-foundations/basic-structure-of-a-web-page/)
* [Webpage we grab HTML](https://realpython.com/practice/aphrodite.html)
* [The script](scrapeScript.py)

# Scrape specific information from webpage

We can scrape specific information from the webpage using text parsing. For instance, if we wanted to get the title of the webpage, we could use the string find() method to seatch through the text of the HTML for the title tags and parse out the actual title.

* [Scrape specific information script](scrapeScript2.py)

# Errors

* If you call urlopen() without internet connection you get this error

```
$ URLError: <urlopen error [Errno 11001] getaddrinfo failed>
```
* If you provide an invalid web address that can't be found

```
$ HTTPError: HTTP Error 404: Not Found
```
#

The previous scripts will work on a very simple website, but won't work on a complicated or far less predictable website.


For example, try to run the previous scripts by changing the address

```python
my_address = "https://realpython.com/practice/poseidon.html"
```
Because the tag is \<title > and not \<title> our find() method returned -1 (because the exact string \<title> wasn't found anywhere)


# Scrape specific table from webpage

Scraping HTML tables can be difficult for various reasons:

* The table HTML element is composite. It typically has several inner elements used to describe table structure. As a simple example:

```html
<table>
  <tr>
    <th>Name</th>
    <th>Age</th>
  </tr>
  <tr>
    <td>Alice</td>
    <td>24</td>
  </tr>
  <tr>
    <td>Bob</td>
    <td>26</td>
  </tr>
</table>
```

The `table` tag has three child levels:

 * `<tr>` (table rows) elements. Each table has a series of row elements.
 * `<th>` (table headers) or `<td>` (table data) elements. Each row in turn has a series of `<th>` and `<tr>` elements.
 * The actual table data (`Alice`, `24`, `Bob`, `26`). This is the actual table data that you want to 'scrape', or transform into a Python list.


* Table headers are optional. For example, this is also a valid HTML table:

```html
<table>
  <tr>
    <td>Alice</td>
    <td>24</td>
  </tr>
  <tr>
    <td>Bob</td>
    <td>26</td>
  </tr>
</table>
```

* Each table row can have a different number `<td>` elements. Here is another valid table:

```html
<table>
  <tr>
    <th>Name</th>
    <th>Age</th>
  </tr>
  <tr>
    <td>Alice</td>
    <td>24</td>
    <td>$15.60</td>
  </tr>
  <tr>
    <td>Bob</td>
    <td>26</td>
  </tr>
</table>
```

* There is nothing in the HTML standard that helps you determine a table data point type, or to enforce that a column in a table has consistent data:

```html
<table>
  <tr>
    <td>24</td>
    <td>Alice</td>
  </tr>
  <tr>
    <td>Bob</td>
    <td>26</td>
  </tr>
</table>
```

* Web browser will forgivingly display HTML tables that are not properly formed:

```html
<table>
  <tr>
    <td>24
    <td>Alice</td>
  <tr>
    <td>Bob</td>
    <td>26
  </tr>
</table>
```

* The `table` HTML element is (ab)used for purposes other than representing tabular data, like web page layout:

```html
<table style="width:100%;">
  <tr>
    <td colspan="2">
      Alice
    </td>
  </tr>
  <tr style="height:170px;">
    <td style="width:20%;">
      24
    </td>
    <td style="width:80%;">
      Bob
    </td>
  </tr>
  <tr>
    <td colspan="2">
      26
    </td>
  </tr>
</table>
```

This is only a portion of the problems you will encounter when trying to pase HTML tables. Here is one really messed up table (and it gets worse):

```html
<table border='1'>
  <tr>
    <th><a href='#'>Name</a></th>
    <th><h3><b>Age</b></h3>
  <tr>
    <td><p><small>Alice</small></p></td>
    <td><ul><li>24</li><li>$15.60</li></ul></td>
  </tr>
  <tr>
    <td><pre><i><q>26</q></i></pre></td>
    <td>Bob
  </tr>
</table>
```

That said, people can (and do) succesfully scrape data from HTML tables. You have two options when creating a script that parses HTML tables: you either need to know in advance the table structure, or you need to take into account the most common possible edge cases of table structure.

As with any other web scraping script the steps to write a script that scrapes a HTML table are:

* Get the raw source of the HTML page that contains your table. You can use two Python libraries for this purpose: `urllib` and `requests`. You can use either to get a blob of unstructured text from a HTML page, including meta data, tags and JavaScript functions.

```
from urllib.request import urlopen
my_address = "https://realpython.com/practice/aphrodite.html"
html_page = urlopen(my_address)
html_text = html_page.read().decode('utf-8')
```
or
```
import requests
url = 'https://pypi.python.org/pypi'
request = requests.get(url)
source = request.text
```
* Convert the page source into something you can traverse and extract the data you need. The most commonly used Python libraries are `BeautifulSoup` and `lxml`. 
```
soup = BeautifulSoup(source, 'html.parser')
```
* Access the table and extract its data. In BeautifulSoup you do this using its find_all() method.
```
...
tables = soup.find_all('table')
table = tables[0]
...
for row in table.find_all('tr'):
    cells = row.find_all('td')
...
```
* Print the data or convert it to a relevant Python data structure.

Here is a small example that uses `requests` and `beautifulSoup` to get the list of recently updated Python packages from the PyPI front page:

* [Scrape specific table from webpage](scrape_table.py)

# Scrape multiple tags from webpage

We can scrape multiple tags from a web page using bs4 --- Joe help again plz!!!

* [Scrape multiple tags from webpage](scrape_multiple_tags.py)
