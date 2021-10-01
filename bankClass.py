import pickle
import datetime
#simer123
#this is a good project 
class bank:
    def __init__(self) -> None:
        self.name=""
        self.ph=""
        self.money=0
        self.pin=0
        self.trans=[]     
    def create(self):
        self.Acc={}
        print("please enter the details properly")
        name=input("enter the name\n")
        ph=input("enter the phone number\n")
        money=input("enter the initial money ammount\n")
        if len(ph)<10 or len(ph)>10:
            ph=input("last chance to enter the correct ph no format\n")
        else:
            self.name=name
            self.ph=ph
            self.money=money
            
        f=open("Acc_holder_counter.txt","r")
        c=f.readlines()
        f.close()
        f2=open("Acc_holder_counter.txt","a")
        c2=len(c)
        count=c2+1
        f2.write(str(count)+"\n")
        f2.close()
        print(f"your Account number is : {count}\n")
        p=input("enter a pin for your Account(4 digit)\n")
        if len(p)<4 or len(p)>4:
            print("please enter a correct pin(4 digits)\n")
        else:
            self.pin=p
        l=[count,self.name,self.ph,self.money]
        self.Acc[count]=l
        self.Acc["Pin"]=self.pin
        self.Acc["transfer details"]=[]
        print("Account was created sucessfully\nYou can check your details by going on option 2 from the menu\n")
        f.close()
    
    def write(self):
        f=open("AccountDetails.dat","ab")
        pickle.dump(self.Acc,f)
        f.close()
    
    def get(self,acc_no,p):
        f=open("AccountDetails.dat","rb") 
        while True:
            try:
                self.Acc=pickle.load(f)
                if acc_no in self.Acc.keys():
                    if p in self.Acc.values():
                        print(f"Account  : {self.Acc[acc_no][0]}")
                        print(f"Name     : {self.Acc[acc_no][1]}")
                        print(f"Phone No : {self.Acc[acc_no][2]}")
                        print(f"Balance  : {self.Acc[acc_no][3]}")
                        break
                    else:
                        print("....pin not correct.....")
            except EOFError:
                print("no record found")
                break
        f.close()

    def update(self,acc_no,p):
        f=open("AccountDetails.dat","rb")
        l2=[]
        while True:
            try:
                self.Acc=pickle.load(f)
                if acc_no in self.Acc.keys():
                    if p in self.Acc.values():
                        print("what do you want to update\n1.Name\n2.Phone No\3.both")
                        ch=int(input())
                        if ch==1:
                            n=input("enter the new name\n")
                            l3=[self.Acc[acc_no][0],n,self.Acc[acc_no][2],self.Acc[acc_no][3]]
                        elif ch ==2:
                            newph=input("enter the new Phone No\n")
                            l3=[self.Acc[acc_no][0],self.Acc[acc_no][1],newph,self.Acc[acc_no][3]]
                        elif ch==3:
                            n=input("enter the new name\n")
                            newph=input("enter the new Phone No\n")
                            l3=[self.Acc[acc_no][0],n,newph,self.Acc[acc_no][3]]
                        else:
                            print("non of the above was selected")
                        flag=1
            except EOFError:
                # print("no record found")
                break
        f.close()
        #for putting all records in list
        if flag==1:
            f=open("AccountDetails.dat","rb")
            while True:
                try:
                    self.Acc=pickle.load(f)
                    l2.append(self.Acc)
                except EOFError:
                    break
            f.close()
        #putiiing the collected data into file back from list
            f=open("AccountDetails.dat","wb")
            for i in l2:
                if acc_no in i:
                   i[acc_no]=l3
            for i in l2:
                pickle.dump(i,f)
            f.close()
        else:
            print("record was not found")

    def transfer(self,acc_no,p,tacc_no):
        f=open("AccountDetails.dat","rb")
        l2=[]
        flag1=0
        flag2=0
        flag3=0
        flag4=0
        #this for validating user's acc_details
        while True:
            try:
                self.Acc=pickle.load(f)
                if acc_no in self.Acc.keys():
                    if p in self.Acc.values():
                        flag1=1
                        break       
            except EOFError:
                print("record was not found") 
                break
        f.close()
        #this is for validating other's details
        f=open("AccountDetails.dat","rb")
        while True:
            try:
                self.Acc=pickle.load(f)
                if tacc_no in self.Acc.keys():
                        flag2=1
                        break     
            except EOFError:
                print("record was not found") 
                break
        f.close()
        if flag1==1 and flag2==1:
            f=open("AccountDetails.dat","rb")
            m=int(input("enter the amount to be transfered\n"))
            while True:
                try:
                    self.Acc=pickle.load(f)
                    if acc_no in self.Acc.keys():
                        if p in self.Acc.values():
                            if m<=int(self.Acc[acc_no][3]):
                                money=int(self.Acc[acc_no][3])-m
                                l3=[self.Acc[acc_no][0],self.Acc[acc_no][1],self.Acc[acc_no][2],money]
                                x = datetime.datetime.now()
                                a= str(x)+" "+str(x.strftime("%A"))
                                t1=(f"transferred {m} to Account No-{tacc_no}   {a}") 
                                t3=[]
                                for i in self.Acc["transfer details"]:
                                    t3.append(i)
                                t3.append(t1)
                                flag3=1
                            else:
                                print("not enough money in account to be transferred")
                except EOFError:
                    break
            f.close()
        else:
            print("some error occured")    
        
        if flag3==1:
            f=open("AccountDetails.dat","rb")
            while True:
                try:
                    self.Acc=pickle.load(f)
                    if tacc_no in self.Acc.keys():
                        money2=int(self.Acc[tacc_no][3])+m
                        l4=[self.Acc[tacc_no][0],self.Acc[tacc_no][1],self.Acc[tacc_no][2],money2]
                        t2=(f"recived {m} from Account No-{acc_no}   {a}")  
                        t4=[]
                        for i in self.Acc["transfer details"]:
                            t4.append(i)
                        t4.append(t2)
                        flag4=1
                except EOFError:
                    break
            f.close()
        
        if flag4==1:
            f=open("AccountDetails.dat","rb")
            while True:
                try:
                    self.Acc=pickle.load(f)
                    l2.append(self.Acc)
                except EOFError:
                    break
            f.close()
            f=open("AccountDetails.dat","wb")
            for i in l2:
                if acc_no in i:
                   i[acc_no]=l3
                   i["transfer details"]=t3  
                elif tacc_no in i:
                    i[tacc_no]=l4
                    i["transfer details"]=t4  
            for i in l2:
                pickle.dump(i,f)
            f.close()
    
    def getTransferDetails(self,acc_no,p):      #trasnfer detasils
        f=open("AccountDetails.dat","rb")
        while True:
            try:
                self.Acc=pickle.load(f)
                if acc_no in self.Acc.keys():
                    if p in self.Acc.values():
                        print("\033[1;36;40m .................................Account Information.................................")
                        print(f"\033[1;37;40mAccount  : {self.Acc[acc_no][0]}")
                        print(f"Name     : {self.Acc[acc_no][1]}")
                        print(f"Phone No : {self.Acc[acc_no][2]}")
                        print(f"Balance  : {self.Acc[acc_no][3]}")
                        print("\033[1;36;40m .................................Transfer Details....................................")
                        for i in self.Acc["transfer details"]:
                            if i[0]=="t":
                                print(f"\033[1;31;40m {i}\n")
                            elif i[0]=="r":
                                print(f"\033[1;32;40m {i}\n")
                        break
                    else:
                        print("\033[1;32;40m .........pin not correct........")
            except EOFError:
                print("no record found")
                break
        f.close()


        


