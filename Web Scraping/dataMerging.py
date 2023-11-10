import csv
import pandas as pd

file1 = 'scrapped_data.csv'
file2 = 'cleaned_data.csv'

temp_list1 = []
temp_list2 = []

with open(file1, 'r') as f:
    csv_reader = csv.reader(f)

    for i in csv_reader:
        temp_list1.append(i)

with open(file2, 'r') as f:
    csv_reader = csv.reader(f)

    for i in csv_reader:
        temp_list2.append(i)

header1 = temp_list1[0]
header2 = temp_list2[0]

star_data1 = temp_list1[1:]
star_data2 = temp_list2[1:]

header = header1+header2

star_data = []

for i in star_data1:
    star_data.append(i)

for j in star_data2:
    star_data.append(j)

with open("final_data.csv", 'w', newline='') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(header)
    csvwriter.writerows(star_data)
