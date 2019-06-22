import sqlite3


def createTable():
    connection = sqlite3.connect("login.db")

    connection.execute("CREATE TABLE USERS(USERNAME TEXT NOT NULL, EMAIL TEXT, PASSWORD TEXT)")

    connection.execute("INSERT INTO USERS VALUES(?,?,?)", ('mohsen', 'mohsen@mail.com', '1234'))

    connection.commit()
    result = connection.execute("SELECT * FROM USERS")

    print('User             Pass')
    for user in result:
        print(user[0], '         ', user[2])

    connection.close()


try:
    createTable()
except:
    connection = sqlite3.connect("login.db")
    result = connection.execute("SELECT * FROM USERS")

    for user in result:
        print("USERNAME:" , user[0], "  PASSWORD: ", user[2], "  EMAIL: ", user[1])


