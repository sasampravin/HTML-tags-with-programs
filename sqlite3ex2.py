def create_db():
    import sqlite3
    con=sqlite3.connect('course.db')
    return con
co=create_db()
def create_table(co):
    curobj=co.cursor()
    curobj.execute('create table course (id int primary key, cname text, name text)')
    co.commit()
    print('table created successfully')
#create_table(co)
def insert_data(co):
    curobj=co.cursor()
    curobj.execute('insert into course values(555,"physics","tswamy")')
    co.commit()
    print('Record inserted successfully')
##insert_data(co)
def review_data(co):
    curobj=co.cursor()
    q=curobj.execute('select * from course')
    co.commit()
    for i in q:
        print(i)
#review_data(co)
def update_data(co):
    curobj=co.cursor()
    curobj.execute('update course set name="rajesh" where id=222')
    co.commit()
    print('Record updated successfully')
##update_data(co)
##review_data(co)
def delete_data(co):
    curobj=co.cursor()
    curobj.execute('delete from course where id=444')
    co.commit()
    print('Record deleted successfully')
##delete_data(co)
##review_data(co)
def alter_data(co):
    curobj=co.cursor()
    curobj.execute('alter table course add amount int')
    co.commit()
    print('table is altered successfully')
##alter_data(co)
##review_data(co)
def update_data(co):
    curobj=co.cursor()
    curobj.execute('update course set amount=14000 where id=555')
    co.commit()
    print('Record updated successfully')
##update_data(co)
##review_data(co)

def alter_table(co):
    curobj=co.cursor()
    curobj.execute('alter table course drop amount')
    print('Record deleted successfully')
##alter_table(co)
##review_data(co)
'''
def rollback_data(co):
    curobj=co.cursor()
    curobj.rollback()
    print('Records rolebacked successfully')
rollback_data(co)
review_data(co)
'''


