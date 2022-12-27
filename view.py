import tkinter as tk
from new import *


def auth():
    print(pin_var.get())
    is_auth = authenticate_user(pin_var.get())
    if is_auth == True:
        return window_transaction()
    else:
        return is_auth


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
    root0 = tk.Toplevel(root)
    root0.geometry("400x400")
    deposit_btn = tk.Button(root0, text='Deposit', command=deposit_btn_func)
    withdraw_btn = tk.Button(root0, text='Withdraw', command=withdraw_btn_func)
    transfer_btn = tk.Button(root0, text='Transfer', command=transfer_btn_func)
    balance_btn = tk.Button(root0, text='Balance Inquiry', command=balance_btn_func)

    deposit_btn.grid(row=1, column=0)
    withdraw_btn.grid(row=1, column=1)
    transfer_btn.grid(row=2, column=0)
    balance_btn.grid(row=2, column=1)


def deposit_btn_func(root0=None):
    root4 = tk.Toplevel(root0)
    root4.geometry("400x400")

    def deposit_btn():
        print(d_var.get())
        return Deposit(d_var.get(), 1).deposit()

    d_var = tk.DoubleVar()

    d_label = tk.Label(root4, text='Enter Amount to Deposit:  ', font=('calibre', 10, 'bold'))

    d_entry = tk.Entry(root4, textvariable=d_var, font=('calibre', 10, 'normal'))

    d_btn = tk.Button(root4, text='Deposit', command=deposit_btn)

    d_label.grid(row=0, column=0)
    d_entry.grid(row=0, column=1)
    d_btn.grid(row=2, column=1)


def withdraw_btn_func(root0=None):
    root3 = tk.Toplevel(root0)
    root3.geometry("400x400")

    def withdraw_btn():
        print(wd_var.get())
        return Withdraw(wd_var.get(), 1).withdraw()

    wd_var = tk.DoubleVar()

    wd_label = tk.Label(root3, text='Enter amount to Withdraw:  ', font=('calibre', 10, 'bold'))

    wd_entry = tk.Entry(root3, textvariable=wd_var, font=('calibre', 10, 'normal'))

    wd_btn = tk.Button(root3, text='Withdraw', command=withdraw_btn)

    wd_label.grid(row=0, column=0)
    wd_entry.grid(row=0, column=1)
    wd_btn.grid(row=2, column=1)


def transfer_btn_func(root0=None):
    root2 = tk.Toplevel(root0)
    root2.geometry("400x400")

    def transfer_btn():
        print(trans_var.get())  ##boş dönüolar
        print(amount_var.get())
        return Transfer(amount_var.get(), 1, trans_var.get()).transfer()

    amount_var = tk.DoubleVar()
    amount_label = tk.Label(root2, text='Enter Your Amount  :  ', font=('calibre', 10, 'bold'))
    amount_entry = tk.Entry(root2, textvariable=amount_var, font=('calibre', 10, 'normal'))

    trans_var = tk.IntVar()
    trans_label = tk.Label(root2, text='Enter Transfer Account Number  :  ', font=('calibre', 10, 'bold'))
    trans_entry = tk.Entry(root2, textvariable=trans_var, font=('calibre', 10, 'normal'))

    sub_btn2 = tk.Button(root2, text='Transfer', command=transfer_btn)

    amount_label.grid(row=0, column=0)
    amount_entry.grid(row=0, column=1)

    trans_label.grid(row=1, column=0)
    trans_entry.grid(row=1, column=1)
    sub_btn2.grid(row=3, column=1)


def balance_btn_func(root0=None):
    # 1 yerine otomatik
    balance = BalanceInquiry(1).get_balance()

    root1 = tk.Toplevel(root0)
    root1.geometry("400x400")
    label = tk.Label(root1, text=balance, font=('calibre', 10, 'bold'))
    label.grid(row=0, column=0)


root.mainloop()
