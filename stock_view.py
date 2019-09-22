import sqlite3
    
def Start_view():
    print("Welcome in Stocks Game!")
    print("Would you like to:\n (a) signIn\n (b) signUp\n")

def viewMenu():
    print("Would you like to:\n (a) search company name.\n (b) retrive market data.")

def viewSearchCompany(symbol):
    print("The ticker symbol of the company is:", symbol)

def viewRetriveMarketData(data):
    print("This is the market data:")
    print("Ticker: ", data[0])
    print("Name: ", data[1])
    print("Last Price: ", data[2])
    print("High: ", data[3])
    print("Low: ", data[4])
    print("Open: ", data[5])

def viewLogIn():
    print("Enter the username:")
    print("Enter the password:")

def errorMessage():
    print("Sorry, username or password is incorrect. Please, try again: ")

def successMessage():
    print("Logged In successfully!")

def viewSignUp():
    print("Please enter username and password")

def viewBuy():
    pass

def viewSell():
    pass

def viewPortfolio():
    pass

# --------------------------

def enterUserAgain():
    print("Please, enter username and password again: ")
