import sys
import pdb
class Accounts:
    def __init__(self,balance):
        self.balance=balance
    def withdrawel(self,amt):
        if amt>balance:
            print "withdrawel amount should be less than balance"
        elif (balance-amt)<=500:
            print"Minimum balance should be 500"
        else:
            balance=balance-amount
            print "withdrawel successful"
    def balancecheck():
        print "Your current balance is{}".format(balance)
    def deposit(amt):
        balance+=amt
        print "amount deposited successfully"
class BusinessAccount(Accounts):
        list1=["kel1","kel2"]
        def BusinessWithdraw(name,amt):
            if name in list1:
                withdrawel(amt)
            else:
                print "wrong Account Type"
        def Businessdeposit(name,amt):
            if name in list1:
                deposit(amt)
            else:
                print "wrong Account Type"
class PersonalAccount(Accounts):
        list2=["kei1","kei2"]
        def PersonalWithdraw(name,amt):
            if name in list1:
                withdrawel(amt)
            else:
                print "wrong Account Type"
        def Personaldeposit(name,amt):
            if name in list1:
                deposit(amt)
            else:
                print "wrong Account Type"
class customer:
    def openaccount():
        per1=PersonalAccount()
        per2=BusinessAccount()
        while True:
            choice=input("do you want to start an account y/n")
            if choice=="yes":
                acctype=raw_input("Enter the accocunt type business or personel")
                if acctype=="business":
                           per1.list1.append()
                           break
                elif acctype=="personel":
                            per2.list2.append()
                            break
                else:
                    print "provide correct account type"
                    continue
            else:
                break
class services:
    while True:
        print "choose your services"
        n=input("1-deposit,2-withdraw 3-exit" )
        if n==1:
            cusd1=raw_input("Enter customer name")
            cusd2=input("enter your amount")
            acctype2=raw_input("Enter the accocunt type business or personel")
            while True:
                if acctype2=="business":
                    pers1=BusinessAccount(1000)
                    pers1.BusinessWithdraw(cusd1,cusd2)
                    break
                elif acctype2=="personel":
                    pers1=PersonalAccount()
                    pers1.PersonalWithdraw(cusd1,cusd2)
                    break
                else:
                    print "provide correct accounttype"
                    continue
        elif n==1:
                    cusd1=raw_input("Enter customer name")
                    cusd2=input("enter your amount")
                    acctype2=raw_input("Enter the accocunt type business or personel")
                    while True:
                        if acctype2=="business":
                            pers1=BusinessAccount()
                            pers1.Businessdeposit(cusd1,cusd2)
                            break
                        elif acctype2=="personel":
                            pers1=Personaldeposit()
                            pers1.person(cusd1,cusd2)
                            break
                        else:
                            print "provide correct accounttype"
                            continue
        elif n==3:
               sys.exit()
        cho=raw_input("do you want to continue")

        if cho=="yes":
            continue
        elif cho=="no":
            sys.exit()
