import sqlite3

try:
    db = sqlite3.connect('python_ddb')

    cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS 
                python_programming(id INTEGER PRIMARY KEY, name TEXT, grade
    INTEGER)''')

    db.commit()

except Exception as e:
    db.rollback()
    raise e

finally:
    db.close()

# Information to put in table
id1 = 55
name1 = 'Carl Davis'
grade1 = 61

id2 = 66
name2 = 'Dennis Fredrickson'
grade2 = 88

id3 = 77
name3 = 'Jane Richards'
grade3 = 78

id4 = 12
name4 = 'Peyton Sawyer'
grade4 = 45

id5 = 2
name5 = 'Lucas Brooke'
grade5 = 99

# Putting all the info into a list to put in the table
python_programming_list = [(id1, name1, grade1), (id2, name2, grade2),
                           (id3, name3, grade3), (id4, name4, grade4),
                           (id5, name5, grade5)]

# Putting the info from the list to the table
cursor.executemany('''INSERT INTO python_programming(id, name, grade)
               VALUES(?,?,?)''', python_programming_list)

db.commit()

cursor.execute('''SELECT id, name, grade FROM python_programming WHERE
               grade > 60 AND grade < 80''')
python_programming = cursor.fetchall()

print(python_programming)

db.commit()

new_grade = 65

cursor.execute('''UPDATE python_programming SET grade = ? WHERE id = ? ''',
               (new_grade, id1))

db.commit()

cursor.execute('''DELETE FROM python_programming  WHERE id = ?''', (id2,))

db.commit()

new_grade2 = 90
new_grade3 = 60

cursor.execute('''SELECT id, name, grade FROM python_programming WHERE
               id > 55 AND id <= 80''')
python_ids = cursor.fetchall()
cursor.execute('''UPDATE python_programming SET grade = ? WHERE id = ? ''',
               (new_grade2, python_ids))

db.commit()

db.close()
