

import sqlite3 as sql

con=sql.connect('labdb')
cur=con.cursor()
def createTable():
    cur.execute('''
create table emp(employee_id int,first_name varchar2(20),last_name varchar2(30), email text,phone_number int,hire_date text,job_id int,salary int,commision_pct real,manager_id text, department_id text)
''')

def insertData(eid,fname,lname, email,pn,hiredata, jid,salary,com,managerid,deptid):
    cur.execute('''
    insert into emp (employee_id ,first_name ,last_name , email ,phone_number,hire_date ,job_id ,salary ,commision_pct ,manager_id , department_id ) values (?,?,?,?,?,?,?,?,?,?,?)
    ''',(eid,fname,lname, email,pn,hiredata, jid,salary,com,managerid,deptid))
    con.commit()
    print('data inserted successfully')


#createTable()

