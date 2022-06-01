# ------------------------------------------------- #
# Title: Assignment 07
# Description: An example of Pickling and Structurred error handling
# ChangeLog: (Who, When, What)
# <Johnathan Luu>,<5.30.2022>,Created Script
# ------------------------------------------------- #

import pickle  # Importing pickle converts data into binary
import random # Importing random allows the usage of random number generator

# Data -------------------------------------------- #

File = 'guess.dat'
TheNumber = int
High =  int
Low = int
Counter = int
Guess = int
GuessesLst = []
Results = str
vTry = str


# Processing -------------------------------------- #
#Save data to binary file
def SaveData(FileName, DataLst): 
    pFile = open(FileName, "wb")
    pickle.dump(DataLst, pFile)
    pFile.close()

#Read data from binary file
def ReadData(FileName): 
    pFile = open(FileName, "rb")
    DataLst = pickle.load(pFile)
    pFile.close()
    return DataLst

#If user guesses a number outside of range, RangeError exception will occur
class RangeError(Exception): 
    """ Number must be between Minimum and Maximum"""
    def __str__(self):
        return "Number is not in range"

class Numbers: 
    #If the user enters a number larger than the current maximum, the maximum will decrease
    def Higher(rGuess, rHigh, rNumber):
        if rGuess >= rNumber:
            rHigh = rGuess
            return rHigh
        else:
            rHigh = rHigh
            return rHigh

    #If the user enters a number smaller than the current minimum, the minimum will increase
    def Lower(rGuess, rLow, rNumber):
        if rGuess <= rNumber:
            rLow = rGuess
            return rLow
        else:
            rLow = rLow
            return rLow

#If user guesses number in 1 try, text will be singular
def sTry(stry, count):
    if count == 1:
        stry = " try "
    else:
        stry = " tries "
    return stry


# Presentation ------------------------------------ #

#Default range is 0-100, a random number in that range will be generated.
TheNumber = random.randint(1, 99)
High = int(100)
Low = int(0)
Counter = 0


        
while Guess != TheNumber:
    try:
        Guess = int(input("Guess a number between " + str(Low) + " and " + str(High) + ": ")) #Print statement asking for input of number
        if Guess >= High or Guess <= Low: #Reference to RangeError exception class
            raise RangeError()

    #Determines how RangeError exception is to be displayed
    except RangeError as e: 
        print()
        print(e, e.__doc__, type(e), sep="\n")
        print()

    #Determines how ValueError exception is displayed if user does not type in an integer
    except ValueError as e: 
        print()
        print("A whole number was not inputed")
        print(e, e.__doc__, type(e), sep="\n")
        print()

    #To catch any other errors by default Python system
    except Exception as e: 
        print()
        print("There was a non-specific error!")
        print("Built-in Python error info: ")
        print(e, e.__doc__, type(e), sep="\n")
        print()

    #If no exceptions, proceed with decreasing range until user guess the number
    else: 
        High = Numbers.Higher(rGuess=Guess, rHigh=High, rNumber=TheNumber)
        Low = Numbers.Lower(rGuess=Guess, rLow=Low, rNumber=TheNumber)
        Counter += 1
        GuessesLst.append(Guess)

#Singular or plural (try/tries)
vTry = sTry(vTry, Counter)

#When user guesses number correctly
print()
print("Nice!")

Results = ("The correct number was: " + str(TheNumber) + "\n" + "It took you " + str(Counter) + vTry + ":)" + "\n" + "Your guesses: " + str(GuessesLst))

#Save data defined as the variable 'Results'
SaveData(File, Results)

#Read data from file and print on screen
print(ReadData(File))

print("Your data has been saved!")
print()
