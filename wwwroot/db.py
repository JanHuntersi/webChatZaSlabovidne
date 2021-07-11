import sqlite3

conn = sqlite3.connect('userdb.db')
print ("Opened database successfully")
curs = conn.cursor()
#conn.execute('CREATE TABLE users (id INT , username TEXT NOT NULL , email TEXT NOT NULL UNIQUE)')
name = input("ime")
email =input("email")
#print('Opened Database succesfully')
#conn.execute('CREATE TABLE users ( username TEXT NOT NULL,email TEXT NOT NULL)')
#print ("Table created succesfully")

#name = input('Vnesite ime ')
#email = input('Vnesite mail ')
#conn.execute("INSERT INTO users (username,email) VALUES (?,?)",(name,email) )
#conn.commit()
#conn.execute("INSERT INTO users (username,email) VALUES (?,?)",(name,email) )
#conn.commit()
#try:
#    conn.execute("UPDATE users SET username = 'Simp' WHERE email ='jan.sernec@gmail.com' ")#(name,email)
#conn.execute("INSERT INTO users VALUES(?,?,?)",(name+"_"+email,name, email))
#conn.commit()
#curs.execute("INSERT INTO users VALUES('dfdf','dsfdsfsdf')")
#    print("Uporabnike je šlo vstaviti")
#except:
#    print("Napaka pri vstavljanju uporabnikov")
#"""
email='jan.sernec@gmail.com'

    
curs.execute("DELETE  FROM users ")
#rows= curs.fetchall()
#for x in rows:
#    print(x)

conn.close()
#print('Opened Database succesfully')
#conn.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT NOT NULL,email TEXT NOT NULL)')
#print ("Table created succesfully")