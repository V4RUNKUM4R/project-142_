from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

STAR_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

page = requests.get(STAR_URL)

soup = bs(page.text, 'html.parser')

Stars_table = soup.find_all('table')
temp_list = []
table_rows = Stars_table[7].find_all('tr')

Star_names = []
Distance =[]
Mass = []
Radius =[]

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

for i in range(1,len(temp_list)):
    Star_names.append(temp_list[i][1])
    Distance.append(temp_list[i][3])
    Mass.append(temp_list[i][5])
    Radius.append(temp_list[i][6])

df2 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius)),columns=['Star_name','Distance','Mass','Radius'])
print(df2)

df2.to_csv('bright_stars2.csv')