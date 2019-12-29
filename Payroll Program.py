#Sabrina Turney
#October 2, 2018
#Payroll Program with Input Validation
#This program validates multiple user inputs in order to run a program that
#will calculate and display the user's gross pay through input of their
#hourly pay and hours worked within reasonable ranges.


#Defining the main function.
def main():
    endProgram = "no" #Declaring local variables as string value, this will
                        #tell the program when to stop or loop again.
    while endProgram == "no": #Here's our repetition structure. The user
                                #will be able to change the var at the end.
        hourlyPay = 0.0
        hoursWorked = 0.0   #Set all variables we'll use to zero if we re-use
        grossPay = 0.0      #the while loop, while initializing them.

        #Nice introduction, as always:
        print("Welcome to my payroll calculator!")
        print("I will take some inputs from your hourly wages to your")
        print("hours worked this week, and then will calculate your gross")
        print("pay for you! Let's get started!\n\n")

        #Call all of our functions. The last one needs no variable assignment,
        #it's just a printing module to make everything tidy.
        hourlyPay = getPay(hourlyPay)
        hoursWorked = getHours(hoursWorked)
        grossPay = calcGross(hourlyPay, hoursWorked, grossPay)
        printData(hourlyPay, hoursWorked, grossPay)
                           
        #Here we ask the user if they want to go again or not. Any input
        #except "no" will terminate the program.
        endProgram = input("Do you want to end the program? yes or no: ")
        while endProgram == "yes" or endProgram != "no":
            return



def getPay(hourlyPay):    #Must be in the range of 7.50 - 18.25
    hourlyPay = float(input("How much money do you make per hour? $"))
    while hourlyPay < 7.50 or hourlyPay > 18.25: #Float for calculations.
        print("Please enter an hourly wage between $7.50 and $18.25 per hour.")
        hourlyPay = float(input("How much money do you make per hour? $"))
    return hourlyPay #If not in range, re-prompt the user. 

def getHours(hoursWorked):  #Must be in the range of 0 - 40
    hoursWorked = float(input("How many hours did you work this week? "))
    while hoursWorked < 0 or hoursWorked > 40: #I use float here so my
        print("Please enter hours between 0 and 40.")#calculations work later.
        hoursWorked = float(input("How many hours did you work this week? "))
    return hoursWorked #If not in the range, re-prompt the user.


def calcGross(hourlyPay, hoursWorked, grossPay):    #Calculate gross pay.
    grossPay = hourlyPay * hoursWorked
    #Keeping all variables as floating point values lets this run without error.
    return grossPay


def printData(hourlyPay, hoursWorked, grossPay): #Print all data for the user.
    print("\nHere's your gross pay check for your data input:")
    print("Hourly wage entered was, $%0.02f" %hourlyPay)
    print("Hours worked was reported as: %0.02f" %hoursWorked)
    print("Your gross pay totals to: $%0.02f" %grossPay)
    #I use the 2 decimal formatting because we're calculating *cash money*.



#Call the main function for the user!
main()
