import requests
import json
import urllib
import sqlite3

lst = []



# ------------- Wrapper ------------------------

lookup_url = "http://dev.markitondemand.com/Api/v2/Lookup/json?input="
quote_url = "http://dev.markitondemand.com/Api/v2/Quote/json?symbol="



def company_search(string):
    new_url = lookup_url + string
    req = requests.get(new_url)
    object = (req.json())
    ticker_symbol = object[0]["Symbol"]
    exchange = object[0]["Exchange"]
    print(ticker_symbol)
    print(exchange)
    return get_quote(ticker_symbol)
def get_quote(string):
    new_url = quote_url+ string
    req = requests.get(new_url)
    object_ = (req.json())
    lst.append(object_["Symbol"])
    lst.append(object_["Name"])
    lst.append(object_["LastPrice"])
    lst.append(object_["High"])
    lst.append(object_["Low"])
    lst.append(object_["Open"])
    print (lst)
    return stockinsertion(lst)

    
    #return retriveMarketData()
def stockinsertion(lst):
    conn = sqlite3.connect('project1.db')
    cur = conn.cursor()
    
    cur.execute("INSERT INTO STOCKS3 (Ticker, NAME, Last_Price, High, Low, Volume )\
    VALUES (?, ?, ?, ?, ?, ?)", lst)
    print("Inserted in stock successfully!!!!!")
    conn.commit()
    conn.close()  
company_search(input())


def userInsertion(user_row):
    conn = sqlite3.connect('project1.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO USERS2 (username, password,Balance)\
       VALUES(?,?,?)", [user_row])
    conn.commit()
    conn.close()

