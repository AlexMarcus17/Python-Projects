'''
Ex. 5
This program calculates the number in an array at a given index
The array is [1,2,2,3,3,3,,4,4,4,4,...]
'''
index = int(input("Enter a number: "))
number = 1
step = 0
while step<index:
    step+=number
    number+=1
number-=1
print("The element at index ",index," is ",number)
