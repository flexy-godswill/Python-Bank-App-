# CREATED A VARIABLE TO GET THE USERS INPUT ######################
userInput = int(input("Enter Your Room Temperature(degree celsius) To Check Whether It's High, Normal Or Low \n"))
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::")


# CREATED AN IF STATEMENT TELLING THE SYSTEM THAT IF THE INPUT FROM THE USER IS GREATER THAN ZERO BUT LESS THAN 20(i.e temperature from 0 to 19 is LOW TEMPERATURE VALUE)
if (userInput > 0) and (userInput < 20):
    print("%s degrees - Your Room Temperature Is Low \n " %userInput)

#CREATED AN ELIF STATEMENT TELLING THE SYSTEM THAT IF THE INPUT FROM THE USER IS GREATER THAN 19 BUT LESS THAN 26(20-25 = NORMAL TEMPERATURE)
elif(userInput >19) and (userInput < 26):
    print("%s degrees - Your Room Temperature Is Normal \n" % userInput)

#CREATED ANOTHER ELIF STATEMENT TELLING THE SYSTEM THAT IF THE INPUT FROM THE USER IS GREATER THAN 26 (26 AND ABOVE = HIGH TEMPERATURE)
elif(userInput > 25):
    print("%s degrees - Your Room Temperature Is High \n" % userInput)

else:
    print("%s degrees - You Have Selected An Invalid Option \n" % userInput)
    