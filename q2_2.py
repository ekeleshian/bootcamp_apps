import sqlite3
from pdb import set_trace



conn = sqlite3.connect('datag_galls.db')
cursor = conn.cursor()


cursor.execute("""create table salespersons
    (id, name, age, salary)""")


cursor.execute("""create table orders (
num ,
order_date ,
cust_id ,
salesperson_id,
amount 
)""")




query_one = 'insert into salespersons (id, name, age, salary) values (8, "Abe", 61, 140000)'
query_two = 'insert into salespersons (id, name, age, salary) values (2, "Bob", 34, 44000)'
query_three = 'insert into salespersons (id, name, age, salary) values (5, "Chris", 34, 40000)'
query_four = 'insert into salespersons (id, name, age, salary) values (7, "Dan", 41, 52000)'
query_five = 'insert into orders (num, order_date, cust_id, salesperson_id, amount) values (10, 8/2/96, 4, 2, 540)'
query_six = 'insert into orders (num, order_date, cust_id, salesperson_id, amount) values (20, 1/30/99, 4, 8, 1800)'
query_seven = 'insert into orders (num, order_date, cust_id, salesperson_id, amount) values (30, 7/14/95, 9, 5, 2400)'


cursor.execute(query_one)
cursor.execute(query_two)
cursor.execute(query_three)
cursor.execute(query_four)
cursor.execute(query_five)
cursor.execute(query_six)
cursor.execute(query_seven)

cursor.execute('''select name from salespersons left join orders on salespersons.id = orders.salesperson_id
	where orders.amount >1300''')
ans = cursor.fetchall()
print(ans)

conn.close()