def create_db():
    import sqlite3
    co = sqlite3.Connection('ComapnyData.db')
    return co


co = create_db()


def create_table(co):
    cur = co.cursor()
    cur.execute(
        'create table company (id number primary key,cname text,loc text)')
    co.commit()
    print('table structure is created successfully')
