'''
Ex. 9
This program prints all numbers with maximum 2 digits of form xy
with the property that the last digit of (xy)^2 is y
'''
for x in range(0,10):
    for y in range(0,10):
        if (((x*10+y)**2)%10)==y:
            print(x*10+y, end= " ")
        
