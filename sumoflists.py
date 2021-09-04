list = [2,5,3,6,4,9,8,6,7,4,5,2,16,56,6]                #define list          

def sum():                                              #function declaration
    
    x = 0
    i=0                                                 #finding sum
    while (i<15):  
         x = x + list[i]
         i = i+1
    return x


a = sum()
print("The sum of the elements of the list =",a)
