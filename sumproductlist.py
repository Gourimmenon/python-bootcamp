lists = [1,8,3,5,7,6,2,4]                                       #define list

x = 0
y = 1
for i in range (0,8):
    x = x + lists[i]                                            #sum
    y = y * lists[i]                                            #product
    
print ('sum of no.s =',x,)
print ('product of the no.s =',y,)
