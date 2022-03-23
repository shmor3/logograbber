import csv
list_cities_id = []

with open('lists/cities+id.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    included_cols = [0, 1]
    for row in spamreader:
        content = list(row[i] for i in included_cols)
        list_cities_id.append(content)

with open('lists/cities.csv', 'w') as csvfile:
    fieldnames = ['id', 'city']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for row in list_cities_id:
        included_cols = [0, 1]
        content = list(row[i] for i in included_cols)
        writer.writerow({fieldnames[0]: content[0], fieldnames[1]: content[1]})
