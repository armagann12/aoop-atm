from methods import *
from random import randint


def register():
    name = input("Please enter Name: ")
    email = input("Please enter Mail: ")
    phone = input("Please enter Phone: ")
    pin = input("Select a pin: ")

    # Manuel for creating customer
    # CardNumber, Card Expiry, Pin, Account Number will be Random

    dbname = get_database()

    customer_collection = dbname["customer"]
    card_collection = dbname["card"]
    account_collection = dbname["account"]

    cardd = randint(10000, 99999)

    Card = {
        "cardNumber": randint(10000, 99999),
        "customerName": name,
        "cardExpiry": randint(100, 999),
        "pin": pin
    }
    acc = randint(10000, 99999)
    Account = {
        "accountNumber": acc,
        "totalBalance": 0.0,
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
        "address": "address",
        "status": True,
        "card": card_id,
        "account": account_id

    }

    customer_collection.insert_one(Customer)

    print("Dont lose your info: Account Number and Card Number:")
    print(acc)
    print(cardd)
register()
