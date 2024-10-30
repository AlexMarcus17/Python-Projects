'''
Ex. 13
This program reads a number from the user and form another number made from the digits
found at odd positions
'''
num = int(input("Enter a number: "))
copy = num
newnum = 0
digits = 0
i = 1
while copy!=0:
    copy=int(copy/10)
    digits+=1
if(digits%2==0):
    while(num!=0):
        newnum = newnum + i*(int((num%100)/10))
        num=int(num/100)
        i *= 10
    print(newnum)
else:
    newnum=int(num%10)
    i *= 10
    num=int(num/10)
    while(num!=0):
        newnum = newnum + i*(int((num%100)/10))
        num=int(num/100)
        i *= 10
    print(newnum)
