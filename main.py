import bankClass
import pandas as pd
print("\033[1;36;40m.........................................Hello Welcom To Bank........................................")
print("pls accept")
choice="yes"
b=bankClass.bank()
while choice == "yes" or "y":       
    c=int(input("\033[1;37;40m Selct any one of the following :\n1.Create new Account\n2.Get the Account details\n3.Transfer money\n4.Change your Account Info\n5.Get transfer details\n"))

    if c==1:
        b.create()
        b.write()
    elif c==2:
        acc_no=int(input("Please Enter your Account Number\n"))
        p=input("Please Enter your pin\n")
        b.get(acc_no,p)
    elif c==3:
        acc_no=int(input("Please Enter your Account Number\n"))
        p=input("Please Enter your pin\n")
        tacc_no=int(input("Enter the Account no where money is to be transferred"))
        b.transfer(acc_no,p,tacc_no)
    elif c==4:
        acc_no=int(input("Please Enter your Account Number\n"))
        p=input("Please Enter your pin\n")
        b.update(acc_no,p)
    elif c==5:
        acc_no=int(input("Please Enter your Account Number\n"))
        p=input("Please Enter your pin\n")
        b.getTransferDetails(acc_no,p)
    else:
        print("non correct option was selected\n")

    choice=input("\033[1;37;40m Do you want to continue(Yes/No)\n")
    if choice=="No"or "n":
        break
