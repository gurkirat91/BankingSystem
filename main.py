import bankClass

print(".........................................Hello Welcom To Bank........................................")
print("selct any one of the following :\n1.Create new Account\n2.Get the Account details\n3.Transfer money\n4.Change your Account Info\n5.Get transfer details")
c=int(input())
choice="yes"
b=bankClass.bank()
while choice=="yes":
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

    choice=input("Do you want to continue(Yes/No)\n")
    c=int(input("Selct any one of the following :\n1.Create new Account\n2.Get the Account details\n3.Transfer money\n4.Change your Account Info\n5.Get transfer details\n"))