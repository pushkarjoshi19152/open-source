import mysql.connector

# creating connection with mysql
conn = mysql.connector.connect(
    host='localhost', user='root', passwd='', database='telephonedir')

# creating cursor to execute queries
cur = conn.cursor()


def show_result():
    for x in cur:
        print(x)


# showing all avialabel databases
def show_databases():
    cur.execute('show databases')
    show_result()


# showing tables
def show_tables():
    cur.execute('show tables')
    show_result()


# creating new database
def create_database():
    cur.execute('create database TelephoneDir')
    show_databases()


# creating table
def create_table():
    cur.execute('use telephonedir')
    cur.execute(
        'create table customer ( cust_id int(5) , cust_name varchar(40), tele_no varchar(15) , date_of_reg date ) '
    )
    show_tables()


# use of 'desc' to view table structure
def use_desc():
    cur.execute('desc customer')
    show_result()


# inserting data into table customer
def insert_data():
    cur.execute(
        'insert into customer values("T101", "Mr. C.P. Gupta", 9812343131, "2018/01/21")')
    cur.execute('select * from customer')
    show_result()


# inserting records by taking its input from user
def insert_data_by_user_input():
    cust_id = input('Enter Customer id: ')
    cust_name = input('Entere Name of Customer: ')
    tele_no = input('Enter telephone number: ')
    date_of_reg = input('Enter date of registration (yyyy/mm/dd): ')
    qry = 'insert into customer (cust_id,cust_name,tele_no,date_of_reg) values (%s,%s,%s,%s)'
    val = (cust_id, cust_name, tele_no, date_of_reg)

    cur.execute(qry, val)
    conn.commit()

    cur.execute('select * from customer')
    show_result()


# inserting multiple records
def insert_multiple_records():
    qry = 'insert into customer (cust_id,cust_name,tele_no,date_of_reg) values (%s,%s,%s,%s)'
    val = [(1002, 'pradip', '9421400345', '2021/02/02'), (1003, 'tejas', '94214003455', '2021/02/02'),
           (1004, 'prem', '9431400345', '2021/02/06'), (1005, 'rahul', '9421500345', '2021/04/02')]

    cur.executemany(qry, val)
    conn.commit()

    cur.execute('select * from customer')
    show_result()

# updating data


def update_data():
    cust_id = input('Enter customer id for which name is to be updated: ')
    cust_name = input('Enter Name of Customer')
    qry = 'update customer set cust_name=%s where cust_id=%s'
    val = (cust_name, cust_id)
    cur.execute(qry, val)
    cur.execute('select * from customer')
    show_result()


update_data()

# closing connection
conn.close()
