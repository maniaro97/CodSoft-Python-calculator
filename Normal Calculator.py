#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math


# In[81]:


# Take Input from the User
Number= int(input('Please Select The Operator-;\n 1.Add(+)\n 2.Subtract(-)\n 3.Multiply(*)\n 4.Divide(/)\n 5.Modulus gives Remainder(%)\n 6.Exponential gives Power(**)\n' ))
print('Thank You For choosing the Operator')
#You can enter simple digit and float digit
n1=eval(input("Enter First Number"))
#You can enter simple digit and float digit
n2= eval(input("Enter Second Number"))
print('ThankYou for choosing the Number ')

#FUNCTION
#Function for addition
def add(n1,n2):
    return n1+n2
#Function for subtraction
def subtract(n1,n2):
    return n1-n2
#Function for multiplication
def multiply(n1,n2):
    return n1*n2
#Function for divide
def divide(n1,n2):
    return n1/n2
def modulus(n1,n2):
    return n1%n2
def exponential(n1,n2):
    return n1**n2

#Conditons For Calculator
if Number==1:
    print(n1,'+',n2,'=',add(n1,n2))
elif Number==2:
    print(n1,'-',n2,'=',subtract(n1,n2))
elif Number==3:
    print(n1,'*',n2,'=',multiply(n1,n2))
elif Number==4:
    print(n1,'/',n2,'=',divide(n1,n2))
elif Number==5:
    print(n1,'%',n2,'=', modulus(n1,n2))
elif Number==6:
    print(n1,'**',n2,'=',exponential(n1,n2))
else:
    print('Sorry, there is some Mistake')


# In[ ]:




