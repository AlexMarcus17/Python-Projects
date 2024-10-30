'''
Ex. 17
This program calculates if a given number is special
A number n is special if there is a number m such that n=m+S(m)
S(m) is the sum of the digits of m
'''
n = int(input("Enter a number: "))
isSpecial = False
if(n==0):
    isSpecial = True
else:
    for i in range(1,n):
        sum1 = 0
        copy = i
        while(copy!=0):
            sum1+=copy%10
            copy=int(copy/10)
        if(sum1+i==n):
            isSpecial = True
            break
if(isSpecial):
    print("The number is special")
else:
    print("The number isn't special")
