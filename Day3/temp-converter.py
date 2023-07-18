#Temperature converter

#Menu Section for project
print("----- Temperature Converter ------")
print(" ")
print("Menu")
print(" ")
print("1) Convert from Fahrenheit to Celsius ")
print("2) Convert from Celsius to Fahrenheit")


#Prompt for user option
user_option = input("Enter Option: ")

#Perform option check 
if(int(user_option) == 1): 
    #Formula = 5/9 x (F-32)
    
    #Getting temperature from user
    temp_F = input("Enter Temperature in Fahrenheit: ")
    
    #Computing the temperature in C
    result_F = (5/9) * (int(temp_F) - 32)
    #Modifications made
    #Modifications made 2
    
    #Printing Result
    print(temp_F + " F " + " is equivalent to " + str(result_F) + " C ")
    
elif(int(user_option) == 2):
    #Formula = (C *(9/5)) + 32
    
    #getting Temperature from user
    temp_C = input("Enter Temperature in Celsius: ")
    
    #Computing Temperature in F
    result_C = (int(temp_C) * (9/5)) + 32
    
    #Display results
    print(temp_C + " C " + "is equivalent to " + str(result_C) + " F")
    
else:
    print("Error: Enter a valid option")


