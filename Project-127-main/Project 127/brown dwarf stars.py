from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
page = requests.get(url)
soup = BeautifulSoup(page.text,'html.parser')

all_tables = soup.find_all('table', {"class":"wikitable sortable"})
brown_stars= []

trs = all_tables[2].find_all('tr')

for tr in trs:
    td = tr.find_all('td')
    r = [i.text.rstrip() for i in td]
    brown_stars.append(r)

Star_names = []
Distance =[]
Mass = []
Radius =[]

print(brown_stars)

for i in range(1,len(brown_stars)):
    Star_names.append(brown_stars[i][0])
    Distance.append(brown_stars[i][5])
    Mass.append(brown_stars[i][7])
    Radius.append(brown_stars[i][8])

bstars_df = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius,)),columns=['Star Name','Distance','Mass','Radius'])
bstars_df.to_csv('Brown Stars Data.csv', index=True, index_label="id")