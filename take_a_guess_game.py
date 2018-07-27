from random import randint
import os
k= (randint(100, 999))
ls1=[]
list1=[]
list2=[]
ls1= map(int, str(k))
for i in ls1:
    list1.append(i)
def guessstatus(n):

    if list1[0]==list2[0] or list1[1]==list2[1] or list1[2]==list2[2]:
        return "match"
    if list1[0]==list2[1] or list1[0]==list2[2] :
        return "close"

    if list1[1]==list2[0] or list1[1]==list2[2]:
        return "close"

    if list1[2]==list2[0] or list1[2]==list2[1]:
        return "close"
    else:

        return "missed"

print ("welcome to the guess game")
while True:
    n=input("Enter your guess !!!")
    ls2=map(int,str(n))
    for j in ls2:
        list2.append(j)

    str1=guessstatus(n)
    for i in ls2:
        print (i)
    print (str1)
    if list1[0]==list2[0] and list1[1]==list2[1] and list1[2]==list2[2]:

        print ("congratulation you won the game")
        break
    else:
        del list2[:]
