import sqlite3

conn = sqlite3.connect("project2.db",1)
print ("Successfully Created Database")


conn.execute('''CREATE TABLE Stocks
		  (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
		  NAME            TEXT	NOT NULL,
		  Exchange			 TEXT   ,
		  Ticker		  VARCHAR   NOT NULL,
		  Last_Price       REAL     ,
		  Change           REAL     ,
		  Volume           REAL     ,
		  High             REAL     ,
		  Low              REAL     );''')

print ("Table Stock Successfully created")


conn.execute('''CREATE TABLE Users
	(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	username 		   TEXT NOT NULL,
	password 			VARCHAR     NOT NULL,
	Balance              REAL       NOT NULL);''')

print("Table User Successfully created")


conn.execute('''CREATE TABLE Portfolio
	(ID INTEGER  PRIMARY KEY AUTOINCREMENT NOT NULL,
	Balance  				REAL     NOT NULL,       
	NAME                    TEXT     ,
	shares                  REAL     ,
	Total_investment        REAL     );''')

print("Table Portfolio Successfully created")

conn.execute('''CREATE TABLE Transactions
	(ID INTEGER   PRIMARY KEY AUTOINCREMENT NOT NULL,
	ORDER_TYPE  					TEXT      NOT NULL,
	QUANTITY                         REAL     NOT NULL,
	TOTAL_COST                       REAL     NOT NULL);''')

print("Table Portfolio Successfully created")