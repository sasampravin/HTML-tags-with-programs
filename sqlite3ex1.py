def create_co():
    import sqlite3
    co=sqlite3.connect('pravin.db')
    return co
co=create_co()
def create_table(co):
    curobj=co.cursor()
    curobj.execute('create table Employee(id integer primary key,name text)')
    co.commit()
    print('table created successfully')
##create_table(co)
def insert_data(co):
    curobj=co.cursor()
    curobj.execute('insert into Employee values(5,"pkumars")')
    co.commit()
    print('data inserted into table')
##insert_data(co)
def review_data(co):
    curobj=co.cursor()
    querry=curobj.execute('select * from Employee')
    co.commit()
    print('Employee data')
    for i in querry:
        print(i)
##review_data(co)
def update_data(co):
    curobj=co.cursor()
    curobj.execute('update Employee set name="mahesh" where id=5')
    co.commit()
    print('record updated successfully')
##update_data(co)
##review_data(co)
def delete_data(co):
    curobj=co.cursor()
    curobj.execute('delete from Employee where id=5')
    co.commit()
    print('record deleted successfully')
delete_data(co)
review_data(co)

