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


# In[2]:


def extract_item(html):
    soup = BeautifulSoup(html, "html.parser")
    return {'title': soup.find('h5', class_='card-title').find('b').text, 'href': soup.find('a', class_='card-body')['href']}
    

def extract_items (elements):
    return list(map(lambda x: extract_item(x.get_attribute('innerHTML')), elements))
    


# In[3]:


#r = requests.get('https://www.packtpub.com/all-products?released=Available&sortBy=store_prod_us_products_date_of_publication_desc', verify=False)


# In[4]:


#soup = BeautifulSoup(r.content, "html.parser")


# In[5]:


#soup.find_all('div', class_='tombstone')


# In[6]:


url = 'https://www.packtpub.com/all-products?released=Available&sortBy=store_prod_us_products_date_of_publication_desc'


# In[7]:


wd = webdriver.Chrome()
wait = WebDriverWait(wd, 10)
page_index = 1


# In[8]:


# init link
wd.get(url)


# In[9]:


while(True):
    wd.get(url)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.ais-hits--item')))
    # extract data
    #
    elements = wd.find_elements_by_css_selector('.ais-hits--item')
    books = extract_items(elements)
    pd.DataFrame(books).to_excel('packt_pages/page{0}.xlsx'.format(page_index))
    wait.until(EC.visibility_of_element_located((By.ID, 'instant-search-pagination-container')))
    #next_link = wd.find_element_by_css_selector('.ais-pagination--item__next')
    next_link = wd.find_element_by_id('instant-search-pagination-container').find_element_by_css_selector('.ais-pagination--item__next').find_element_by_css_selector('.ais-pagination--link')
    #print(page_index)
    page_index = page_index + 1
    url = next_link.get_attribute('href')
    
return


# In[ ]:


wd.get(url)


# In[ ]:


wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.ais-hits--item')))


# In[ ]:


elements = wd.find_elements_by_css_selector('.ais-hits--item')


# In[ ]:


sample_element_text = elements[0].get_attribute('innerHTML')


# In[ ]:


len(elements)


# In[ ]:


next_link = wd.find_element_by_css_selector('.ais-pagination--item__next')


# In[ ]:


next_link.get_attribute('innerHTML')


# In[ ]:


books = extract_items(elements)


# In[ ]:


wd.quit()


# In[ ]:


books


# In[ ]:


#sample_element_text


# In[ ]:


#soup = BeautifulSoup(sample_element_text, "html.parser")
#soup


# In[ ]:


#soup.find('h5', class_='card-title').find('b').text


# In[ ]:


#soup.find('a', class_='card-body')['href']


# In[ ]:


df = pd.DataFrame(books)


# In[ ]:


df


# In[ ]:


df.append(books, ignore_index=True)


# In[ ]:




