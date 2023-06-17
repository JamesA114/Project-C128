#from selenium import webdriver
#from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
#import time
import pandas as pd
import requests

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

# Webdriver
#browser = webdriver.Chrome("C:/Users/jimmy/Desktop/CodingClasses/C127/chromedriver.exe")
#browser.get(START_URL)

#make a page request
page = requests.get(START_URL)
#Parse page
soup = bs(page.text,"html.parser")
#get table with class
star_table = soup.find_all("table", {"class":"wikitable sortable"})
total_table = len(star_table)
#finding the tr tags
table_rows = star_table[0].find_all("tr")
#fetch complete data in an empty list
temp_list = []
for tr in table_rows:
    td = tr.find_all("td")
    #fetch row and remove spaces
    #for i in td:
    #    row = [i.text.rstrip()]
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)
star_names = []
distance = []
mass = []
radius = []
l = len(temp_list)
for i in range(1,l):
    star_names.append(temp_list[i][0])
    distance.append(temp_list[i][5])
    mass.append(temp_list[i][8])
    radius.append(temp_list[i][9])
headers = ["Star_names","Distance","Mass","Radius"]
df2 = pd.DataFrame(list(zip(star_names,distance,mass,radius)), columns=[["Star_names","Distance","Mass","Radius"]])
df2.to_csv('dwarf_stars.csv', index=True, index_label="id")