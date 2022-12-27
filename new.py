from enum import Enum
from pymongo import MongoClient
from abc import ABC
# Classes:


def get_database():
    CONNECTION_STRING = "mongodb+srv://atm:atm@cluster0.ektwfcg.mongodb.net/?retryWrites=true&w=majority"

    client = MongoClient(CONNECTION_STRING)

    return client["atm"]


class TransactionType(Enum):
    BALANCE_INQUIRY, DEPOSIT, WITHDRAW, TRANSFER = 1, 2, 3, 4


class Customer:
    def __init__(self, name, address, email, phone, status):
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone
        self.__status = status
        self.__card = Card()
        self.__account = Account


class Card:
    def __init__(self, number, customer_name, expiry, pin):
        self.__card_number = number
        self.__customer_name = customer_name
        self.__card_expiry = expiry
        self.__pin = pin


class Account:
    def __init__(self, account_number):
        self.__account_number = account_number
        self.__total_balance = 0.0
        self.__available_balance = 0.0


# Transactions:

class BalanceInquiry():
    def __init__(self, account_number):
        self.__account_number = account_number

    def get_balance(self):
        # Account Number will come from auth-customer-account

        dbname = get_database()
        collection = dbname["account"]
        doc = collection.find_one({"accountNumber": self.__account_number})
        if doc is None:
            status = False
        else:
            status = doc["totalBalance"]

        print(status)
        return status


class Deposit():
    def __init__(self, amount, account_number):
        self.__amount = amount
        self.__account_number = account_number


    def deposit(self):
        dbname = get_database()
        collection = dbname["account"]
        doc = collection.find_one({"accountNumber": self.__account_number})

        if doc is None:
            status = False
        else:
            balance = doc["totalBalance"]
            balance += self.__amount
            print(balance)
            collection.update_one({"accountNumber": self.__account_number}, {"$set": {"totalBalance": balance}})
            # Print Reciept
            status = True

        print(status)
        return status


class Withdraw():
    def __init__(self, amount, account_number):
        self.__amount = amount
        self.__account_number = account_number

    def withdraw(self):
        dbname = get_database()
        collection = dbname["account"]
        doc = collection.find_one({"accountNumber": self.__account_number})

        if doc is None:
            status = False
        else:
            balance = doc["totalBalance"]
            if balance < self.__amount:
                status = False
            else:
                balance -= self.__amount
                print(balance)
                collection.update_one({"accountNumber": self.__account_number}, {"$set": {"totalBalance": balance}})
                # Print Reciept
                status = True

        print(status)
        return status


class Transfer():
    def __init__(self, amount, account_number, destination_account_number):
        self.__amount = amount
        self.__destination_account_number = destination_account_number
        self.__account_number = account_number


    def transfer(self):
        dbname = get_database()
        collection = dbname["account"]
        doc = collection.find_one({"accountNumber": self.__account_number})

        if doc is None:
            status = False
        else:
            balance = doc["totalBalance"]
            if balance < self.__amount:
                status = False
            else:
                trans_doc = collection.find_one({"accountNumber": self.__destination_account_number})
                if trans_doc is None:
                    status = False
                else:
                    trans_balance = trans_doc["totalBalance"]
                    balance -= self.__amount
                    trans_balance += self.__amount
                    print(balance)
                    print(trans_balance)

                    collection.update_one({"accountNumber": self.__account_number}, {"$set": {"totalBalance": balance}})
                    collection.update_one({"accountNumber": self.__destination_account_number}, {"$set": {"totalBalance": trans_balance}})

                    # Print Reciept
                    status = True

        print(status)
        return status


#BalanceInquiry(33336).get_balance()
#Withdraw(3, 1).withdraw()
# Deposit(7, 1).deposit()
#Transfer(7, 1, 33336).transfer()

