import bs4
import requests


# BeautifulSoup can be used to make more specific
# matches on html tags by specifying css classes
# or html attributes
def attribute_match(zipcode=80922):
    base_url = "https://www.wunderground.com/cgi-bin/findweather/getForecast?query="
    url = "{}{}".format(base_url, zipcode)
    print(url)
    page = requests.get(url)  # Download our html to memory
    soup = bs4.BeautifulSoup(page.text, 'html.parser')  # Create BeautifulSoup object

    # The second argument to find_all is optional
    # however if provided, must be a dictionary
    # containing html attributes and their values.

    # In this practical example I am going to pull
    # weather data from www.wunderground.com

    # Here I start by matching a 'div' tag with an id of 'curTemp'
    temp_field = soup.find('div', {'id': 'curTemp'})
    # Because this span is nested with dir, I will run a new find
    # on the result of the last and use .text to obtain it's value
    temp_value = temp_field.find('span', {'class': 'wx-value'}).text
    # I've done the same thing here only instead of the dictionary,
    # I used the 'class_' kwarg which is predefined by bs4 to
    # match a tag's class. This should be equivalent to using the
    # dictionary method above.
    temp_unit = temp_field.find('span', class_='wx-unit').text

    # Again using a kwarg rather than dict to match id
    cond_field = soup.find('div', id='curCond')
    current_condition = cond_field.find('span', class_='wx-value').text

    # Now for some nice output:
    print("Current Weather:")
    print("Temperature: {}{}\nConditions:  {}".format(
        temp_value,
        temp_unit,
        current_condition,
    ))


if __name__ == "__main__":
    attribute_match()