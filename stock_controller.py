import requests
import json
import sqlite3
from view import viewMenu
from view import successMessage
from view import Start_view
from wrapper import get_quote
from wrapper import company_search
import view



balance = 100000
Start_view()
def start():
   input_ = input()
   if input_ == "a":
        userlogIn()

   if input_ == "b":
        userSignUp()

   if input_ == "c":
   		buyStock()
   if input_ == "d":
   		sellStock()
   if input_ == "e":
   		portfolio()


def userlogIn():
    view.viewLogIn()
    username = input()
    password = input()
    conn = sqlite3.connect('project2.db')
    cur = conn.cursor()
    data = cur.execute("SELECT username FROM USERS WHERE username = ? AND password = ?", (username, password))
    data = cur.fetchone()
    if data is not None:
        successMessage()
        viewMenu()
        input_ = input()
        if input_ == "a":
            searchCompName()
        if input_ == "b":
            retriveMarketData()
        if input_ == "c":
        	buyStock()
        if input_ == "d":
        	sellStock()
        if input_ == "e":
            portfolio()
    else:
        view.errorMessage()
        userlogIn()

def userSignUp():
    view.viewSignUp()
    username = input()
    password = input()
    user_row = []
    user_row.append(username)
    user_row.append(password)
    user_row.append(100000)
    userInsertion(user_row)

def userInsertion(user_row):
    conn = sqlite3.connect('project2.db')
    cur = conn.cursor()
    for i in user_row:
    	cur.execute("INSERT INTO USERS (username, password,Balance)\
       VALUES(?,?,?)", user_row)
    conn.commit()
    conn.close()
    return userSignUp()


def searchCompName():
    input_ = str(input("Enter company name: "))
    data = company_search(input_)
    print(data)
    Start_view()
    start()
    
    



def retriveMarketData():
    input_ = str(input("Enter company name: ")).upper()
    data = get_quote(input_)
    print(data)
    Start_view()
    start()

    



def buyStock():
   	
	view.viewBuy()
  
  	conn = sqlite3.connect('project2.db', timeout=10)
  	cur = conn.cursor()

  	input_= str(input("Enter company name: "))
  	LastPrice = get_quote(input_)
  	LastPrice = LastPrice[5]
  	print("The current Price is" + str(LastPrice))
   	view.enterUserAgain()
   	username = input()
   	password = input()
   	cur.execute("INSERT INTO Portfolio (Balance) VALUES (100000)")
   	conn.commit()
   	wallet = cur.execute("SELECT Balance FROM Portfolio")
   	conn.commit()
   	wallet = cur.fetchone()[0]
   	data = cur.execute("UPDATE Users SET Balance = balance  WHERE username = ? AND password = ?", (username, password))
   	conn.commit()
  	ORDER_TYPE = ("Buy")
   	shares = float(input("enter the amount of shares you would like to buy"))
   	Total_cost = LastPrice * shares
   	print ("Your total cost is" + str(Total_cost))
   	print("you have purchased" + str(shares) + "shares of"+str(input_))
   	if wallet > Total_cost:
    		print("Transaction is successful")
    	else:
    		print("Insufficient Funds")
   	params = ("Buy", shares, Total_cost)
	purchase = cur.execute("INSERT INTO Transactions (ORDER_TYPE, QUANTITY, Total_Cost) VALUES (?,?,?)",(params) )
	conn.commit()
	new_params = (balance, Total_cost)
	new_balance = cur.execute("UPDATE Portfolio Set Balance = ? - ?",(new_params))
	conn.commit()
	cur.execute("UPDATE Portfolio Set Balance = ?-?",(new_params))
	conn.commit()
	Balance_=cur.execute("SELECT Balance FROM Portfolio")
	conn.commit()
	print(Balance_)
	cur.close()
	view.viewMenu()

	# retriveMarketData()
	# view.viewBuy()



def sellStock():
	view.viewSell()
	conn = sqlite3.connect('project2.db', timeout=10)
  	cur = conn.cursor()

  	input_= str(input("Enter company name: "))
  	LastPrice = get_quote(input_)
  	LastPrice = LastPrice[5]
  	print("The current Price is" + str(LastPrice))
   	view.enterUserAgain()
   	username = input()
   	password = input()
   	wallet = cur.execute("SELECT Balance FROM Portfolio")
   	wallet = cur.fetchone()[0]
   	ORDER_TYPE = ("Sell")
   	Total_cost = LastPrice * shares

   	shares = float(input("enter the amount of shares you would like to sell"))
   	print ("Your total cost is" + str(Total_cost))
   	print("you have sold" + str(shares) + "shares of"+str(input_))
   	if wallet > Total_cost:
    		print("Transaction is successful")
    	else:
    		print("Insufficient Funds")
   	params = ("Buy", shares, Total_cost)
	purchase = cur.execute("INSERT INTO Transactions (ORDER_TYPE, QUANTITY, Total_Cost) VALUES (?,?,?)",(params) )
	new_params = (balance, Total_cost)
	new_balance = cur.execute("UPDATE Portfolio Set Balance = ? + ?",(new_params))
	cur.execute("UPDATE Portfolio Set Balance = ?+?",(new_params))
	Balance_=cur.execute("SELECT Balance FROM Portfolio")
	conn.commit()
	print(Balance_)
	cur.close()
	view.viewMenu()


    


def portfolio():
    	

	    conn = sqlite3.connect('project2.db')
	    cur = conn.cursor()
	    view.enterUserAgain()
	    username = input()
	    password = input()    
	    data = cur.execute("SELECT *  FROM Portfolio ")
	    data = cur.fetchall()
	    while data is not None:
	    	print(data)
	    	data = cur.fetchall()
	    conn.commit()
	    return view.viewPortfolio()
	    conn.close()
	    view.viewMenu()

 


if __name__ == "__main__":
    start()
