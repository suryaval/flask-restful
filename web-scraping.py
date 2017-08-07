
# coding: utf-8

# In[2]:

from bs4 import BeautifulSoup

import requests

r = requests.get("https://www.facebook.com");

data = r.text;

soup = BeautifulSoup(data);

for link in soup.find_all('a'):
    print(link.get('href'));

