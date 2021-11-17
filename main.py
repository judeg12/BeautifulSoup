from typing import Text
from bs4 import BeautifulSoup
import requests

# fetch data from site
html_text = requests.get(
    'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
# convert text to lxml
soup = BeautifulSoup(html_text, 'lxml')
# look for match from list elements <li> with this class name
jobs = soup.findAll('li', class_='clearfix job-bx wht-shd-bx')

counter = 1
for job in jobs:
    company_name = job.find('h3', class_='joblist-comp-name').text
    company_name = company_name.replace(
        ' ', '').replace("\n", '').replace("\r", '')
    required_skills = job.find(
        'span', class_='srp-skills').text.replace(' ', '').replace("\n", '')
    published_date = job.find(
        'span', class_='sim-posted').text.replace("\n", '')
    print('\n' + str(counter) + ' job info:')
    print('comapy name: ' + company_name)
    print('skills: ' + required_skills)
    print('published date: ' + published_date)
    counter += 1

print('')
