import csv

input_file = "dwarf_stars.csv"
output_file = "cleaned_data.csv"

cleaned_data = []

with open(input_file, 'r', newline='') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        if all(value is not None and value != '' for value in row.values()):
            if row["Mass"]:
                row["Mass"] = float(row["Mass"]) * 0.000954588
            if row["Radius"]:
                row["Radius"] = float(row["Radius"]) * 0.102763
            cleaned_data.append(row)

with open(output_file, 'w', newline='') as csv_file:
    fieldnames = cleaned_data[0].keys()
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(cleaned_data)

print("Data cleaned and saved to", output_file)
