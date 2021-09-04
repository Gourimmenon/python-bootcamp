x = int(input("enter your marks percentage:")) #mark stored as integer in x

if x > 90:                                     #check if x>90. if yes prints A
    print("A")                                 
elif (x > 80) or (x==90):                      #check if x>80 or x=90. if yes prints B
    print("B")
elif (x>=60) or (x==80):                       #check if x greater than or =90. if yes prints C
    print("C")
else :                                         #if above conditions not met, x<60,in that case prints D
    print("D")
