import mysql.connector

conn= mysql.connector.connect(
    host= '127.0.0.1',
    port = '3306',
    user= 'root',
    password = 'RituMunu@123',
    database= 'AT18'
)
'''if conn.is_connected():
    print('Connected')
else:
    print('Not connected')'''
cursor = conn.cursor()


# Query Inserting
'''query_insert = 'insert into emp(empID,empName,empDept,empManager) values(%s,%s,%s,%s)'
values = (9,'Rekha','Dev','Sinu')
cursor.execute(query_insert,values)
conn.commit()'''


# Fetching Data
'''query_select = 'select * from emp'
cursor.execute(query_select)
result = cursor.fetchall()

for i in result:
    print(i)'''

# Question Query
'''
query = 'select * from emp where empName="Ragav"'
cursor.execute(query)
result = cursor.fetchall()
print(result)
'''

'''var= open('practice.txt','r+')
read_data = var.read()
read_lines = var.readlines()
print(read_data)
print(read_lines)
print(type(read_data))
print(type(read_lines))'''

