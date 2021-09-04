input("Enter name:")                                                                            #NAME

age = int (input("Enter age:"))                                                                 #AGE

input("Enter DOB:")                                                                             #DOB,Nativity
input("Enter Nativity:")                                                                       

print("Admission open for classes: LKG, UKG, I, II, III, IV, V, VI, VII, VIII, IX and XI")      #Class
Class = input("Class applying for(Enter in the above format):")


if Class is "LKG" or "UKG":                                                           #check eligibility for kg
    if 3<=age<=5:
        print("The candidate is eligible for further admission procedures.")
    else:
        print("The candidate is not eligible for admission to the corresponding class.")
        
elif Class is 'I' or 'II':                                                            #check eligibility for I&II
    if 6<=age<=8:
        print("The candidate is eligible for further admission procedures.")
    else:
        print("The candidate is not eligible for admission to the corresponding class.")   

elif Class is 'III' or 'IV':                                                          #check eligibility for III&IV
    if 8<=age<=9:
        print("The candidate is eligible for further admission procedures.")
    else:
        print("The candidate is not eligible for admission to the corresponding class.")       
        
elif Class is 'V' or 'VI':                                                             #check eligibility for V&VI
    if 10<=age<=11:
        print("The candidate is eligible for further admission procedures.")
    else:
        print("The candidate is not eligible for admission to the corresponding class.")         
    
elif Class is 'VII' or 'VIII':                                                         #check eligibility for VII&VIII      
    if 12<=age<=13:
        print("The candidate is eligible for further admission procedures.")
    else:
        print("The candidate is not eligible for admission to the corresponding class.") 

elif Class is 'IX':                                                                    #check eligibility for IX
    if 14<=age<=15:
        print("The candidate is eligible for further admission procedures.")
    else:
        print("The candidate is not eligible for admission to the corresponding class.") 

elif Class is 'XI':                                                                    #check eligibility for XI
    if 16<=age<=17:
        print("The candidate is eligible for further admission procedures.")
    else:
        print("The candidate is not eligible for admission to the corresponding class.") 
        
else :
    print("Invalid input!")
