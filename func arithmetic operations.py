def sum(a,b):                                           #define sum function
    i = a+b
    return i
def product(a,b):                                       #define product function
    i = a*b
    return i
def diff(a,b):                                          #define differece function
    i = a-b
    return i

x = int(input("Enter 1st number:"))                     #input 2 numbers
y = int(input("Enter 2nd number:"))

c = sum(x,y)                                            #function calling
d = product(x,y)
e = diff(c,d)

print("The sum of the 2 numbers:",c)                    #print result
print("The product of the 2 numbers",d)
print("The difference of the results",e)
