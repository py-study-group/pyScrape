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

# Scrape specific table from webpage

We can scrape specific table from the webpage using beautiful soup 4-- Joe Help me plzz!!

here is the file

* [Scrape specific table from webpage](scrape_table.py)

# Scrape multiple tags from webpage

We can scrape multiple tags from a web page using bs4 --- Joe help again plz!!!

* [Scrape multiple tags from webpage](scrape_multiple_tags.py)
