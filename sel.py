from os import sysconf
from selenium import webdriver
import sys

from cookievals import cookies

day = sys.argv[1]

file = open(f'day-{day}/data.txt', '+w')

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(options=options)

driver.get('https://adventofcode.com')

for cookie in cookies:
    driver.add_cookie({'name': cookie['name'], 'value': cookie['value']})

driver.get(f'https://adventofcode.com/2021/day/{day}/input')
element = driver.find_elements_by_tag_name('pre')[0]
data = element.get_attribute('innerHTML').strip()

file.write(data)