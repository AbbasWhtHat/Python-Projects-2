from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

star_table = soup.find_all('table', {"class", "wikitable sortable"})

temp_list = []

table_rows = star_table[2].find_all('tr')

for i in table_rows:
    td = i.find_all('td')

    rows = []
    for j in td:
        rows.append(j.text.rstrip())

    temp_list.append(rows)

star_names = []
distance = []
mass = []
radius = []

for i in range(1, len(temp_list)):

    star_names.append(temp_list[i][0])
    distance.append(temp_list[i][5])
    mass.append(temp_list[i][7])
    radius.append(temp_list[i][8])

headers = ['Star_name', 'Distance', 'Mass', 'Radius']

star_df_2 = pd.DataFrame(
    list(zip(star_names, distance, mass, radius,)), columns=headers)

print(star_df_2)

star_df_2.to_csv('dwarf_stars.csv', index=True, index_label="id")
