import mysql.connector
import json
import csv

conn= mysql.connector.connect(
    host= '127.0.0.1',
    port = '3306',
    user= 'root',
    password = 'RituMunu@123',
    database= 'AT18'
)
cursor = conn.cursor()

with open('json_data.json', 'r') as file:
    json_reader = file.read()
    json_convo = json.loads(json_reader)


json_clms = (list(json_convo['data'][0]))

json_rows = []
for i in json_convo['data']:
    json_rows.append(i.values())

with open('csv_convo.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(json_clms)
    writer.writerows(json_rows)

with open('csv_convo.csv', 'r') as csv_reader:
    reader = csv.reader(csv_reader)
    for i in reader:
        print(i)