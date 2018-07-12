import sys
class tax:
    def __init__(self,income):
        self.income=income
    def calculate(self):
        if self.income <=100000:
            return self.income*.1
        if 100000<self.income <=1000000:
            return self.income*.2
        if self.income >1000000:
            return self.income*.25
while True:
    income=input( "Enter your income")
    t1=tax(income)
    print t1.calculate()
    choice=raw_input("do you want to calculate another tax y/n")
    if choice=="yes":
        continue
    elif choice=="no":
        sys.exit()
