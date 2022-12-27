from pymongo import MongoClient
from enum import Enum
import tkinter as tk


def get_database():
    CONNECTION_STRING = "mongodb+srv://atm:atm@cluster0.ektwfcg.mongodb.net/?retryWrites=true&w=majority"

    client = MongoClient(CONNECTION_STRING)

    return client["atm"]


def create_customer(name, email, phone, address, status, card_number, card_expiry, pin, account_number):
    # Manuel for creating customer
    # CardNumber, Card Expiry, Pin, Account Number will be Random

    dbname = get_database()

    customer_collection = dbname["customer"]
    card_collection = dbname["card"]
    account_collection = dbname["account"]

    Card = {
        "cardNumber": card_number,
        "customerName": name,
        "cardExpiry": card_expiry,
        "pin": pin
    }

    Account = {
        "accountNumber": 1,
        "totalBalance": 14.0,
        "availableBalance": 0.0
    }

    account_id = account_collection.insert_one(Account).inserted_id
    print(account_id)

    card_id = card_collection.insert_one(Card).inserted_id
    print(card_id)

    Customer = {
        "name": name,
        "email": email,
        "phone": phone,
        "address": address,  # address more data
        "status": status,  # status enum
        "card": card_id,
        "account": account_id

    }

    customer_collection.insert_one(Customer)


# create_customer("Armagan", "test@gmail.com", "0530", "address", "status", "card_num", "card_exp", "pin", "account_num")


def authenticate_user(pin):
    # Param is the pin_number
    # Returns bool (also return id of the card so we can search customer with that card)

    dbname = get_database()
    col = dbname["card"]
    doc = col.find_one({"pin": pin})

    if doc is None:
        status = False
    else:
        status = True

    print(status)
    return status


# authenticate_user("pin")

def balance_inquiry(account_number):
    # Account Number will come from auth-customer-account

    dbname = get_database()
    collection = dbname["account"]
    doc = collection.find_one({"accountNumber": account_number})
    if doc is None:
        status = False
    else:
        status = doc["totalBalance"]

    print(status)
    return status


# balance_inquiry(333361)

def withdraw(amount, account_number):
    # Param amount will come from money selection also same as BInq

    dbname = get_database()
    collection = dbname["account"]
    doc = collection.find_one({"accountNumber": account_number})

    if doc is None:
        status = False
    else:
        balance = doc["totalBalance"]
        if balance < amount:
            status = False
        else:
            balance -= amount
            print(balance)
            collection.update_one({"accountNumber": account_number}, {"$set": {"totalBalance": balance}})
            # Print Reciept
            status = True

    print(status)
    return status


# withdraw(2, 33333)

def deposit(amount, account_number):
    dbname = get_database()
    collection = dbname["account"]
    doc = collection.find_one({"accountNumber": account_number})

    if doc is None:
        status = False
    else:
        balance = doc["totalBalance"]
        balance += amount
        print(balance)
        collection.update_one({"accountNumber": account_number}, {"$set": {"totalBalance": balance}})
        # Print Reciept
        status = True

    print(status)
    return status


# deposit(20, 33336)

def transfer(amount, account_number, transfer_account):
    dbname = get_database()
    collection = dbname["account"]
    doc = collection.find_one({"accountNumber": account_number})

    if doc is None:
        status = False
    else:
        balance = doc["totalBalance"]
        if balance < amount:
            status = False
        else:
            trans_doc = collection.find_one({"accountNumber": transfer_account})
            if trans_doc is None:
                status = False
            else:
                trans_balance = trans_doc["totalBalance"]
                balance -= amount
                trans_balance += amount
                print(balance)
                print(amount)

                collection.update_one({"accountNumber": account_number}, {"$set": {"totalBalance": balance}})
                collection.update_one({"accountNumber": transfer_account}, {"$set": {"totalBalance": trans_balance}})

                # Print Reciept
                status = True

    print(status)
    return status


# transfer(29 ,33336, 1)



# # # Tkinter # # #

""""

root = tk.Tk()
root.geometry("400x400")
pin_var = tk.StringVar()

pin_label = tk.Label(root, text='Enter Your Pin:  ', font=('calibre', 10, 'bold'))

pin_entry = tk.Entry(root, textvariable=pin_var, font=('calibre', 10, 'normal'))


def call():
    return authenticate_user(pin_var.get())


sub_btn = tk.Button(root, text='Submit', command=call)

pin_label.grid(row=0, column=0)
pin_entry.grid(row=0, column=1)
sub_btn.grid(row=2, column=1)

root.mainloop()

"""
