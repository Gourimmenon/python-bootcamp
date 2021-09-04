def greater(a,b,c):                                     #function definition
    max = a
    if (b > max):
        max = b 
    if (c > max):     
        max = c
    return max
    
x = int(input("Enter 1st digit: "))                     #input 3 digits
y = int(input("Enter 2nd digit: "))
z = int(input("Enter 3rd digit: "))

i = greater(x,y,z)                                      #function calling

print ("The greatest number is:",i)                     #print the greatest number 
