import sqlite3
from sqlite3 import Error
from random import randint

def create_conn(db_file):
     try:
         conn = sqlite3.connect(db_file)
     except Error as e:
         print(e)
     finally:
         conn.close()

conn = sqlite3.connect('db\\sqlite\\db\\pythonsqlite.db')

c = conn.cursor()
c.execute("PRAGMA foreign_keys = ON")


def create_tables(c):
    try:

        c.execute('CREATE TABLE IF NOT EXISTS LOGIN'
                  '(id integer PRIMARY KEY NOT NULL, '
                  'email text, '
                  'pswd text)');

        c.execute('CREATE TABLE IF NOT EXISTS STUD_INFO'
                  '(id integer PRIMARY KEY NOT NULL, '
                  'fname text, '
                  'lname text, '
                  'sem_id integer, '
                  'FOREIGN KEY(id) REFERENCES LOGIN(id) ON DELETE CASCADE)');

        c.execute('CREATE TABLE IF NOT EXISTS GPA_DETAILS'
                  '(id integer, '
                  'sem1 real, '
                  'sem2 real, '
                  'sem3 real, '
                  'sem4 real, '
                  'sem5 real, '
                  'sem6 real, '
                  'sem7 real, '
                  'sem8 real, '
                  'FOREIGN KEY(id) REFERENCES STUD_INFO(id) ON DELETE CASCADE)');

    except Error as e:
        print(e)


create_tables(c)
conn.commit()


def populate(c):
    try:
        # id, email, pswd


        LOGIN_INFO = [(1, 'test1@demo.com', 'test1234'),
                       (2, 'test2@demo.com', 'test1234'),
                       (3, 'test3@demo.com', 'test1234'),
                       (4, 'test4@demo.com', 'test1234'),
                      (5, 'test5@demo.com', 'test1234'),
                      (6, 'test6@demo.com', 'test1234'),
                      (7, 'test7@demo.com', 'test1234'),
                      (8, 'test8@demo.com', 'test1234'),
                      (9, 'test9@demo.com', 'test1234'),
                      (10, 'test10@demo.com', 'test1234'),
                      (11, 'test11@demo.com', 'test1234'),
                      (12, 'test12@demo.com', 'test1234')]

        c.executemany('INSERT INTO LOGIN VALUES (?,?,?)', LOGIN_INFO)

        # id, fname, lname, sem_id


        STUD_DETAILS = [(1, 'Test1', 'User1', 6),
                         (2, 'Test2', 'User2', 7),
                         (3, 'Test3', 'User3', 8),
                         (4, 'Test4', 'User4', 6),
                        (5, 'Test5', 'User5', 7),
                        (6, 'Test6', 'User6', 8),
                        (7, 'Test7', 'User7', 8),
                        (8, 'Test8', 'User8', 3),
                        (9, 'Test9', 'User9', 2),
                        (10, 'Test10', 'User10', 3),
                        (11, 'Test11', 'User11', 5),
                        (12, 'Test12', 'User12', 6)]

        c.executemany('INSERT INTO STUD_INFO VALUES (?,?,?,?)', STUD_DETAILS)

        # id, sem(1 to 8)


        GPA_DETAILS = [(1, 8.9 , 8.3 , 8.6 , 8.5 , 8.4 , 0.0 , 0.0 , 0.0),
                       (2, 8.9 , 8.3 , 8.6 , 8.5 , 8.4 , 8.9 , 0.0 , 0.0),
                       (3, 8.9 , 8.3 , 8.6 , 8.5 , 8.4 , 8.5 , 9.2 , 0.0),
                       (4, 8.9, 8.3, 8.6, 8.5, 8.4, 0.0, 0.0, 0.0),
                       (5, 8.6, 8.3, 9.0, 8.5, 8.4, 8.9, 0.0, 0.0),
                       (6, 8.4, 8.3, 9.4, 8.9, 8.8, 9.5, 9.2, 0.0),
                       (7, 8.4, 8.3, 7.9, 8.5, 8.4, 8.9, 9.0, 0.0),
                       (8, 8.0, 8.3, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0),
                       (9, 8.8, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0),
                       (10, 8.1, 8.4, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0),
                       (11, 8.7, 8.7, 8.6, 8.5, 0.0, 0.0, 0.0, 0.0),
                       (12, 8.9, 8.7, 8.6, 8.5, 8.1, 0.0, 0.0, 0.0)
                       ]

        c.executemany('INSERT INTO GPA_DETAILS VALUES (?,?,?,?,?,?,?,?,?)', GPA_DETAILS);

    except Error as e:
        print(e)


populate(c)
conn.commit()


def bulkDataIns():

     for num in range(13, 201):
         if (num % 2) == 0:
    
              c.execute("INSERT INTO LOGIN VALUES(?,?,?)", (num, 'abc' + str(num) + '@demo.com', 'abc' + str(num)))
              c.execute( "INSERT INTO STUD_INFO VALUES(?,?,?,?)", (num, 'ABC' , 'DEF' , 8) )
              c.execute("INSERT INTO GPA_DETAILS VALUES(?,?,?,?,?,?,?,?,?)", (num, 8.4, 8.3, 9.4, 8.9, 8.8, 9.5, 9.2, 0.0))
         else:
              c.execute("INSERT INTO LOGIN VALUES(?,?,?)", (num, 'xyz' + str(num) + '@demo.com', 'xyz' + str(num)))
              c.execute("INSERT INTO STUD_INFO VALUES(?,?,?,?)", (num, 'PQR', 'XYZ', 7))
    
              c.execute("INSERT INTO GPA_DETAILS VALUES(?,?,?,?,?,?,?,?,?)", (num, 8.6, 8.3, 9.0, 8.5, 8.4, 8.9, 0.0, 0.0))


bulkDataIns()
conn.commit()


for num in range(13,15):
         print(num,'abc'+str(num)+'@demo.com','abc'+str(num))
