x = int(input("enter the year:"))             #stores integer value into x

if x%400==0 :                             #check if x is divisible by 400
    print("it is a leap year")            
elif x%100==0:                            #check if x is divisible by 100
    print("it is not a leap year")
elif x%4==0:                              #check if x is divisible by 4
    print("it is a leap year")
else :
    print("it is not a leap year")
