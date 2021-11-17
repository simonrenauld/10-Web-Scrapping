# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 16:59:29 2021

@author: Simon Renauld
"""

"""
Download and sources
https://chromedriver.chromium.org/downloads
https://www.guru99.com/xpath-selenium.html#1
https://maoviola.medium.com/a-complete-guide-to-web-scraping-linkedin-job-postings-ad290fcaa97f
"""


from selenium import webdriver
import time
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import signal
import sys






driver = webdriver.Chrome(executable_path=r'C:/Users/bin/chromedriver')



# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')



# locate email form by_class_name
username = driver.find_element_by_xpath('//input[@id="username"]')
username.send_keys('testemai378@gmail.com')

username = driver.find_element_by_xpath('//input[@id="password"]')
username.send_keys('testemai378123')

#click login
find = driver.find_element_by_xpath("//button[contains(text(),'Sign in')]")
find.click()



url = 'https://www.linkedin.com/jobs/search/?geoId=91000014&keywords=data&location=Southeast%20Asia'
driver.get(url)


"""
Get Number of jobs per link search and location
"""

time.sleep(1)

# find Highest number in data-test-pagination-page-btn
parent = driver.find_element_by_id('ember334')
children = parent.find_elements_by_tag_name("li")  # note the plural

for child in children:
    last_page = children[-1].get_attribute("data-test-pagination-btn")
s = last_page

print(s)


         
         
"""        
         
              
############# Break lope if no new results 

    try:
        wd.find_elements_by_xpath("//*[@class='jobs-search-results__list list-style-none']")
    except NoSuchElementException:
        break

job_lists = wd.find_elements_by_xpath("//*[@class='jobs-search-results__list list-style-none']")
jobs = job_lists.find_elements_by_tag_name('li') # return a list

print(len(jobs))


#Get the job search card elements

job_id= []
job_title = []
company_name = []
location = []
date = []
job_link = []
for job in jobs:
 job_id0 = job.find_element_by_css_selector('div').get_attribute('data-control-id')
 job_id.append(job_id0)
  
 job_title0 = job.find_element_by_css_selector('h3').get_attribute('innerText')
 job_title.append(job_title0)
 
 company_name0 = job.find_element_by_css_selector('h4').get_attribute('innerText')
 company_name.append(company_name0)
 
 location0 = job.find_element_by_css_selector('[class="job-search-card__location"]').get_attribute('innerText')
 location.append(location0)
 
 date0 = job.find_element_by_css_selector('div>div>time').get_attribute('datetime')
 date.append(date0)
 
 job_link0 = job.find_element_by_css_selector('a').get_attribute('href')
 job_link.append(job_link0)
 
time.sleep(5)




job_data = pd.DataFrame({'ID': job_id,
'Date': date,
'Company': company_name,
'Title': job_title,
'Location': location,
'Link': job_link
})
# cleaning description column

job_data.to_csv('.\outputs\dataremoteworldwide.csv',encoding='utf-8-sig')       

"""


