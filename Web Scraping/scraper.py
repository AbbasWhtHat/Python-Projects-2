from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

browser = webdriver.Chrome("chromedriver.exe")
browser.get(url)

time.sleep(10)

scrapped_data = []


def scrape():
    soup = BeautifulSoup(browser.page_source, "html.parser")

    star_table = soup.find("table", attrs={"class", "wikitable"})
    table_body = star_table.find("tbody")
    table_rows = table_body.find_all("tr")

    for row in table_rows:
        table_cols = row.find_all("td")

        temp_list = []

        for columns in table_cols:
            data = columns.text.strip()
            temp_list.append(data)

        scrapped_data.append(temp_list)


scrape()

stars_data = []

for i in range(0, len(scrapped_data)):

    star_names = scrapped_data[i][1]
    distance = scrapped_data[i][3]
    mass = scrapped_data[i][5]
    radius = scrapped_data[i][6]
    lum = scrapped_data[i][7]

    data = [star_names, distance, mass, radius, lum]
    stars_data.append(data)

print(stars_data)

headers = ['Star_name', 'Distance', 'Mass', 'Radius', 'Luminosity']

star_df_1 = pd.DataFrame(stars_data, columns=headers)

star_df_1.to_csv('scrapped_data.csv', index=True, index_label="id")
