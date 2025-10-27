import sqlite3

connection = sqlite3.connect('student.db')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS STUDENT (
        NAME VARCHAR(255),
        CLASS VARCHAR(10),
        SELECTION VARCHAR(50),
        MARKS INT
    );
''')

cursor.execute('''INSERT INTO STUDENT (NAME, CLASS, SELECTION, MARKS) VALUES ('Aritra', 'Gen AI', 'A', 90);''')
cursor.execute('''INSERT INTO STUDENT (NAME, CLASS, SELECTION, MARKS) VALUES ('Anupam', 'DGEN', 'B', 100);''')
cursor.execute('''INSERT INTO STUDENT (NAME, CLASS, SELECTION, MARKS) VALUES ('Evan', 'PowerBi', 'A', 35);''')
cursor.execute('''INSERT INTO STUDENT (NAME, CLASS, SELECTION, MARKS) VALUES ('Archis', 'WebDev', 'A', 50);''')
cursor.execute('''INSERT INTO STUDENT (NAME, CLASS, SELECTION, MARKS) VALUES ('Siza', 'PowerBi', 'A', 35);''')

print("The inserted records are:")
data = cursor.execute('''SELECT * FROM STUDENT''')
for row in data:
    print(row)

connection.commit()
connection.close()
