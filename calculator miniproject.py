a=float(input("enter first number:"))
b=float(input("enter second number:"))
operation= input("enter operation:")
if operation is "+" :                         #add
    x=a+b
elif operation is "-" :                       #subtract
    x=a-b
elif operation is "*" :                       #multiply
    x=a*b
elif operation is "/" :                       #divide
    if b!=0:
        x=a/b
    else:
        print("Invalid input!")               #division by 0 not defined
else:
    print("Invalid operation!")
    
print(x)                                      #print final answer
