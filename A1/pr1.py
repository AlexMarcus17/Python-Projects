'''
Ex. 1
This program iteratively calculates the sum of the digits of a given number,
until the sum has a single digit,
this number being the control digit of the given number
'''
num = int(input("Enter a number: "))
sum1 = 0
while num>9:
    while num!=0:
        sum1+=num%10
        num = int(num/10)
    num=sum1
    sum1=0
print("The control digit is: ",num)
