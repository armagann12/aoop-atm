import tkinter as tk
from main import *
from new import *

def auth():
    bool = authenticate_user(pin_var.get())
    if bool == True:
        return window_transaction()
    else:
        return bool

root = tk.Tk()
root.geometry("400x400")
pin_var = tk.StringVar()

pin_label = tk.Label(root, text='Enter Your Pin:  ', font=('calibre', 10, 'bold'))

pin_entry = tk.Entry(root, textvariable=pin_var, font=('calibre', 10, 'normal'))

sub_btn = tk.Button(root, text='Submit', command=auth)

pin_label.grid(row=0, column=0)
pin_entry.grid(row=0, column=1)
sub_btn.grid(row=2, column=1)


def window_transaction():
    root = tk.Tk()
    root.geometry("400x400")
    deposit_btn = tk.Button(root, text='Deposit', command=deposit_btn_func)
    withdraw_btn = tk.Button(root, text='Withdraw', command=withdraw_btn_func)
    transfer_btn = tk.Button(root, text='Transfer', command=transfer_btn_func)
    balance_btn = tk.Button(root, text='Balance Inquiry', command=balance_btn_func)

    deposit_btn.grid(row=1, column=0)
    withdraw_btn.grid(row=1, column=1)
    transfer_btn.grid(row=2, column=0)
    balance_btn.grid(row=2, column=1)

def deposit_btn_func():
    root = tk.Tk()
    root.geometry("400x400")

def withdraw_btn_func():
    root = tk.Tk()
    root.geometry("400x400")

def transfer_btn_func():
    root = tk.Tk()
    root.geometry("400x400")

    def transfer_btn():
        print(trans_var.get()) ##boş dönüolar
        print(amount_var.get())
        return Transfer(int(amount_var.get()), 1, int(trans_var.get())).transfer()


    amount_var = tk.StringVar()
    amount_label = tk.Label(root, text='Enter Your Amount:  ', font=('calibre', 10, 'bold'))
    amount_entry = tk.Entry(root, textvariable=amount_var, font=('calibre', 10, 'normal'))

    trans_var = tk.StringVar()
    trans_label = tk.Label(root, text='Enter Transfer Account Number  :  ', font=('calibre', 10, 'bold'))
    trans_entry = tk.Entry(root, textvariable=trans_var, font=('calibre', 10, 'normal'))

    sub_btn = tk.Button(root, text='Transfer', command=transfer_btn)

    amount_label.grid(row=0, column=0)
    amount_entry.grid(row=0, column=1)

    trans_label.grid(row=1, column=0)
    trans_entry.grid(row=1, column=1)
    sub_btn.grid(row=3, column=1)

    


def balance_btn_func():
    # 1 yerine otomatik
    balance = BalanceInquiry(1).get_balance()

    root = tk.Tk()
    root.geometry("400x400")
    label = tk.Label(root, text= balance, font=('calibre', 10, 'bold'))
    label.grid(row=0, column=0)



root.mainloop()

