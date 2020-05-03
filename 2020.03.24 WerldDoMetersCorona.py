# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 13:24:28 2020

@author: user
"""

import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import date, timedelta 
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

url='https://www.worldometers.info/coronavirus/#countries'
r=requests.get(url)
soup = BeautifulSoup(r.text,'html.parser')

#class="wikitable plainrowheaders sortable jquery-tablesorter"
table=soup.find('table',{'id':'main_table_countries_today'})
rows=table.find_all('tr')[1:]

rows[1]

aantalen=[]
yesterday = date.today() - timedelta(days=1)
yesterday=yesterday.strftime("%m/%d/%Y")
aantalen.append(str(yesterday))
#country_names=['Italy','USA','Spain','Germany','France','Switzerland','UK','Netherlands']
for row in rows:   
    country=row.find_all('td')[0].text.strip()
    #print(country)
    aantal=row.find_all('td')[1].text.strip()
    #print(aantal)
    #!!!!!! IMPORTANT: Aşağıdaki Sıralamayı değiştirmeyin
    if country == 'Italy':
        aantalen.append(aantal.replace(",", ""))
    if country == 'USA':
        aantalen.append(aantal.replace(",", ""))
    if country == 'Spain':
        aantalen.append(aantal.replace(",", ""))
    if country == 'Germany':
        aantalen.append(aantal.replace(",", ""))
    if country == 'France':
        aantalen.append(aantal.replace(",", ""))
    if country == 'Switzerland':
        aantalen.append(aantal.replace(",", ""))
    if country == 'UK':
        aantalen.append(aantal.replace(",", ""))
    if country == 'Netherlands':
        aantalen.append(aantal.replace(",", ""))
    
  
#print(countries)
print(aantalen)
# load the data from csv
df = pd.read_csv('output/corona.csv',index_col=0)
df = df.drop_duplicates()