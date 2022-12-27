import tkinter as tk
from new import *


def auth():
    print(pin_var.get())
    is_auth = authenticate_user(pin_var.get())
    if is_auth == True:
        pin_var.set("")
        return window_transaction()
    else:
        pin_var.set("")
        root11 = tk.Toplevel(root)
        root11.geometry("50x50")
        label = tk.Label(root11, text='Wrong Pin', font=('calibre', 10, 'bold'))
        label.place(x=50, y=25, anchor="center")
        return is_auth


root = tk.Tk()
root.geometry("300x50")
pin_var = tk.StringVar()

pin_label = tk.Label(root, text='Enter Your Pin:  ', font=('calibre', 10, 'bold'))

pin_entry = tk.Entry(root, textvariable=pin_var, font=('calibre', 10, 'normal'))

sub_btn = tk.Button(root, text='Submit', command=auth)

pin_label.grid(row=0, column=0)
pin_entry.grid(row=0, column=1)
sub_btn.grid(row=2, column=1)


def window_transaction():
    root0 = tk.Toplevel(root)
    root0.geometry("200x75")
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
    root4.geometry("350x50")

    def deposit_btn():
        is_deposit = Deposit(d_var.get(), 1).deposit()
        if is_deposit:
            root12 = tk.Toplevel(root0)
            root12.geometry("50x50")
            label = tk.Label(root12, text='Deposited', font=('calibre', 10, 'bold'))
            label.place(x=50, y=25, anchor="center")
            root4.destroy()
        return is_deposit

    d_var = tk.DoubleVar()

    d_label = tk.Label(root4, text='Enter Amount to Deposit:  ', font=('calibre', 10, 'bold'))

    d_entry = tk.Entry(root4, textvariable=d_var, font=('calibre', 10, 'normal'))

    d_btn = tk.Button(root4, text='Deposit', command=deposit_btn)

    d_label.grid(row=0, column=0)
    d_entry.grid(row=0, column=1)
    d_btn.grid(row=2, column=1)


def withdraw_btn_func(root0=None):
    root3 = tk.Toplevel(root0)
    root3.geometry("350x50")

    def withdraw_btn():
        is_withdraw = Withdraw(wd_var.get(), 1).withdraw()
        if is_withdraw:
            root12 = tk.Toplevel(root0)
            root12.geometry("50x50")
            label = tk.Label(root12, text='Withdrawed', font=('calibre', 10, 'bold'))
            label.place(x=50, y=25, anchor="center")
            root3.destroy()
        else:
            root12 = tk.Toplevel(root0)
            root12.geometry("250x50")
            label = tk.Label(root12, text='There is not enough balance', font=('calibre', 10, 'bold'))
            label.place(x=100, y=25, anchor="center")
            root3.destroy()
        return is_withdraw

    wd_var = tk.DoubleVar()

    wd_label = tk.Label(root3, text='Enter amount to Withdraw:  ', font=('calibre', 10, 'bold'))

    wd_entry = tk.Entry(root3, textvariable=wd_var, font=('calibre', 10, 'normal'))

    wd_btn = tk.Button(root3, text='Withdraw', command=withdraw_btn)

    wd_label.grid(row=0, column=0)
    wd_entry.grid(row=0, column=1)
    wd_btn.grid(row=2, column=1)


def transfer_btn_func(root0=None):
    root2 = tk.Toplevel(root0)
    root2.geometry("400x75")

    def transfer_btn():
        is_transferred= Transfer(amount_var.get(), 1, trans_var.get()).transfer()
        if is_transferred:
            root13 = tk.Toplevel(root0)
            root13.geometry("50x50")
            label = tk.Label(root13, text='Transferred', font=('calibre', 10, 'bold'))
            label.place(x=50, y=25, anchor="center")
            root2.destroy()
        else:
            root12 = tk.Toplevel(root0)
            root12.geometry("450x50")
            label = tk.Label(root12, text='Either there is no balance or there is no such account', font=('calibre', 10, 'bold'))
            label.place(x=200, y=25, anchor="center")
            root2.destroy()
        return is_transferred

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
    root1.geometry("50x50")
    label = tk.Label(root1, text=balance, font=('calibre', 10, 'bold'))
    label.grid(row=0, column=0)


root.mainloop()
