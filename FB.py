#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os
from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import json

## Heavy load on ram, use data transfer rate above 10,00,00,00/s and close other apps if needed

from secrets import username, password  # in script username = [username for username in list of mail addresses], password = [list of passwords] 

class FaceBookBot(): # Use login once and get time untill search complete.

    def __init__(self):
        options = webdriver.ChromeOptions() # Do not go Headless
        options.add_argument('--disable-notifications')
        self.driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"), options=options)

    def login(self,username, password):
        self.driver.get("https://www.facebook.com/login")

        sleep(2)

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)

        password_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        password_in.send_keys(password)

        login_btn = self.driver.find_element_by_xpath('//*[@id="loginbutton"]')
        login_btn.click()

        sleep(10)
        
Fbot = FaceBookBot()
        
Fbot.login(username, password)

data = []

with open("keywords.txt", 'r', encoding="utf-8") as keywords_file:
    keywords = keywords_file.readlines()
    for keyword in keywords:
        Fbot.driver.get(f"https://www.facebook.com/search/posts/?q={keyword}&epa=SERP_TAB&tbs='qdr:h'")
        page = Fbot.driver.page_source
        data.append(page)
        sleep(5)

   

        for dddd in data:
            fb_soup = BeautifulSoup(dddd, "html.parser")
            news_all = fb_soup.find_all(class_='_3-8y')


## Comment out prints read data from details.json          

details = []

for t in news_all:
    w = t.find_all(class_='_401d')#links
    x = t.find_all(class_='_7gyi')#name
    z = t.find_all(class_='_6-cp')#Description
    for awd in w:
            links = awd.find_all('a')
            for i in links:
                for afg in x:
                    name = afg.text
                    #print('Name: ', name)
                    details.append({'Name': name })
                    for isi in z:
                        brief = isi.text[10:] #
                        #print('Brief: ', brief)
                        date = isi.text[0:6]
                        #print('Date: ', date)
                        details.append({'Date': date})
                        details.append({'Brief': brief})
                        p = i.get('href')
                        if p.startswith('https://'):
                            #print('Facebook link ', p)
                            details.append({'Facebook link': p})
                        if p.startswith('https://www.facebook.com/profile.php/'):
                            #print('profile ', p)
                            details.append({'profile': p})
                        if p.startswith('https://www.facebook.com/photo.php?'):
                            #print('photo ', p)
                            details.append({'photo': p})
                        if p.startswith('https://www.facebook.com/groups/'):
                            #print('Groups ', p)
                            details.append({'Groups': p}) 
               
              
                

    
       
       
        
with open('scraper.json', 'w') as json_outfile:
    json.dump(details, json_outfile)
    
jsonread = json.dumps(details, ensure_ascii=False, indent=4)
print(jsonread)


            

bot.driver.close() 


# In[4]:


with open('scraper.json', 'w') as json_outfile:
    json.dump(details, json_outfile) 


# In[5]:


jstr = json.dumps(details, ensure_ascii=False, indent=4)
print(jstr)


# In[ ]:




