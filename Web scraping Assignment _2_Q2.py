#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip install selenium')


# In[3]:


import selenium
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
import time


# In[4]:


#Connecting to the driver
driver=webdriver.Chrome(r"chromedriver.exe")


# In[5]:


driver.get("https://www.naukri.com/")


# In[6]:


designation = driver.find_element(By.CLASS_NAME,"suggestor-input")
designation.send_keys('Data Scientist”')


# In[7]:


Location = driver.find_element(By.XPATH,"/html/body/div[1]/div[6]/div/div/div[5]/div/div/div/input")
Location.send_keys('Bangalore')


# In[8]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[9]:


Job_Title=[]
Job_Location=[]
Company_Name=[]
Experience_Required=[]


# In[10]:


Title_Tags=driver.find_elements(By.XPATH,'//a[@class="title fw500 ellipsis"]')
for i in Title_Tags[0:10]:
    Title=i.text
    Job_Title.append(Title)

Location_Tags=driver.find_elements(By.XPATH,"//li[@class='fleft grey-text br2 placeHolderLi location']")
for i in Location_Tags[0:10]:
    Location=i.text
    Job_Location.append(Location)

Company_Tags=driver.find_elements(By.XPATH,"//a[@class='subTitle ellipsis fleft']")
for i in Company_Tags[0:10]:
    Company=i.text
    Company_Name.append(Company)

Experience_Tag=driver.find_elements(By.XPATH,"//li[@class='fleft grey-text br2 placeHolderLi experience']//span")
for i in Experience_Tag[0:10]:
    Experience=i.text
    Experience_Required.append(Experience)



# In[11]:


print(len(Job_Title),len(Job_Location),len(Company_Name),len(Experience_Required))


# In[12]:


df=pd.DataFrame({'JOB_TITLE':Job_Title,'LOCATION':Job_Location,'COMPANY_NAME':Company_Name,'EXPERIENCE':Experience_Required})
df


# In[ ]:




