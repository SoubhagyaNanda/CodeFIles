import mysql.connector
import json

conn= mysql.connector.connect(
    host= '127.0.0.1',
    port = '3306',
    user= 'root',
    password = 'RituMunu@123',
    database= 'AT18'
)
cursor = conn.cursor()

json_file = open('data.json', 'r')
data= json_file.read()
json_data = json.loads(data)

create_table = '''
create table jsonTable(
    id int,
    name varchar(30),
    email varchar(50),
    role varchar(50),
    enrolled_courses int
    );
'''

'''cursor.execute(create_table)
conn.commit()'''

insert_query = 'insert into jsonTable(id, name, email, role, enrolled_courses) values(%s,%s,%s,%s,%s)'

for i in json_data:
    values = (i['id'],i['name'],i['email'],i['role'],i['enrolled_courses'])
    cursor.execute(insert_query,values)
conn.commit()

cursor.close()
conn.close()