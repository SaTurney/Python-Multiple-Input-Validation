#Sabrina Turney
#September 30, 2018
#Cell Phone Minute Calculator
#This program validates multiple user inputs in order to run a program that
#assesses a cell phone bill's minutes usage and prints a bill. It doesn't give
#an error and crash the program if an invalid input is given by the user, but
#instead prompts them gently to fix it and continues running. How kind!


#Defining the main function.
def main():
    endProgram = "no"   #Declaring local variables as string value - Here is our
                        #repetition structure starter!
    while endProgram == "no": #This structure runs at least once, since we have
                                #set the variable to "no" for now.
        minutesAllowed = 0 #While in this loop, all local variables are set
                            #to 0 so they can be called and returned in our
                            #subsequent funnctions.
        minutesUsed = 0
        totalDue = 0
        minutesOver = 0



        #Here, we have all these beautiful functions being called and returned
        #to our while loop. Each gets their own turn at catching an invalid
        #input- Maybe we can call these "nested defensive maneuvers"?
        minutesAllowed = getAllowed(minutesAllowed)
        minutesUsed = getUsed(minutesUsed)
        totalDue, minutesOver = calcTotal(minutesAllowed, minutesUsed, totalDue, minutesOver)
        printData(minutesAllowed, minutesUsed, totalDue, minutesOver)

        #And here's where the user gets to change that while loop with input!
        endProgram = input("Do you want to end program? yes or no: ")
        #I super changed this part of the code- Essentially, the pseudocode
        #left us in a loop where no matter what we answered, our program
        #would continue asking for a new input. This way, if we answer
        #"no", we loop the program again, and if not, it ends.
        while endProgram == "yes" or endProgram != "no":
            return


#Here's where we get our allowance on our phone minutes. I'd rather be measuring
#my data cap, but I'll take what I can get!
def getAllowed(minutesAllowed):
    minutesAllowed = int(input("How many minutes are allowed? "))
    #Input as an int here so we can use these variables to calc later!
    while minutesAllowed < 200 or minutesAllowed > 800:
        print("Please enter minutes between 200 and 800.")
    #This particular phone plan is picky about their minutes.
        minutesAllowed = int(input("How many minutes are allowed? "))
        #Our first catch here- Enter between the values or you will be
        #prompted again. 
    return minutesAllowed

#Here, we get another chance for the user to screw up an input with a variable
#asking how many of those minutes in their phone plan they used. 
def getUsed(minutesUsed):
    #Again, an int value is essential to later calculations.
    minutesUsed = int(input("How many minutes were used? "))
    while minutesUsed <0:
        print("Please enter minutes of at least 0.")
        #Now, stop being silly. Enter a real number ya goon.
        minutesUsed = int(input("How many minutes were used? "))
    return minutesUsed

#Here's the big calculation module! Yay! We finally bring together all those
#int variables to a cohesive structure.
def calcTotal(minutesAllowed, minutesUsed, totalDue, minutesOver):
    extra = 0 #Quick local variable for those big spenders

    #This If Else structure makes it nice and clear for the end user and other
    #programmers how the math is being done! I'm a fan of separate print
    #statements for each if-else. 
    if minutesUsed <= minutesAllowed:
        totalDue = 74.99
        minutesOver = 0
        print("You were not over your minutes for the month.")
    else:
        minutesOver = minutesUsed - minutesAllowed
        extra = minutesOver * .20 #If you were naughty here, you pay the price.
        #This calculation is added only in this else obviously, and you pay
        #a whopping .20 cents each minute of overage! Absolute gouging.
        totalDue = 74.99 + extra
        print("You were over your minutes by ", minutesOver)
    return totalDue, minutesOver


#A lovely print module. It prints a big, noticable bill header, and then goes
#straight into the breakdowns and specifics. How can you not love your bill!
def printData(minutesAllowed, minutesUsed, totalDue, minutesOver):
    print("----------------MONTHLY USE REPORT----------------------")
    print("Minutes allowed were ", minutesAllowed)
    print("Minutes used were ", minutesUsed)
    print("Minutes over were ", minutesOver)
    print("Total due is $", totalDue)


    
#Last but not least, we call the main function for the end user.
main()
