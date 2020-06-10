#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import json
from bs4 import BeautifulSoup
from IPython.core.display import HTML
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd 
import itertools


# In[2]:


def extract_link(wd, link):
    wd.get(link)
    items = BeautifulSoup(wd.find_element_by_css_selector('.table').get_attribute('innerHTML')).find('tbody').find_all('tr')
    return list(map(lambda x: x.find_all('td')[1].find('a'), items))
    


# In[24]:


def extract_report(wd, link, name):
    wd.get('{0}{1}'.format(based_url, link))
    return {'name': name, 'params': wd.find_element_by_id('sppara').get_attribute('value'), 'sql':  wd.find_element_by_id('spsql').get_attribute('value')}


# In[4]:


based_url = 'https://vnhnprod01.vn.msig.com'


# In[5]:


wd = webdriver.Chrome()


# In[6]:


wd.get('https://vnhnprod01.vn.msig.com/centralreporting/Account/Login')


# In[7]:


wd.execute_script("$('#UserName').val('vnhnnqh')")


# In[8]:


wd.execute_script("$('#Password').val('P!ssword5')")


# In[9]:


wd.execute_script("$('form').submit()")


# In[10]:


wd.get('https://vnhnprod01.vn.msig.com/centralreporting/db2sql/')


# In[11]:


pages = wd.find_element_by_css_selector('.pagination')


# In[12]:


soup1 = BeautifulSoup(pages.get_attribute('innerHTML'))
soup1


# In[13]:


page_links = soup1.find_all('a')


# In[14]:


links = list(map(lambda x: '{0}{1}'.format(based_url, x['href']), page_links))
links


# In[15]:


report_items = list(itertools.chain.from_iterable(list(map(lambda x: extract_link(wd, x), links))))


# In[16]:


#clean NONE items
report_items = list(filter(lambda x: x != None, report_items))


# In[17]:


report_items


# In[26]:


pd.DataFrame(list(map(lambda x: extract_report(wd, x['href'], x.text), report_items))).to_excel('webreporting.xlsx')
#list(map(lambda x: extract_report(wd, x, report_items))


# In[ ]:




