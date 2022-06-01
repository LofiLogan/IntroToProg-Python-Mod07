# Module07 Website

Johnathan Luu
Intro to Python
Assignment 7
5/24/2022
https://github.com/LofiLogan/


Pickling and Structured Error Handling

Intro
	Pickling and structured error handling were the main focus of this week’s module. Simply put, pickling is the process of converting information into byte or binary form. Exception handling can be used in many ways. At the simplest level, the Python language has some exceptions implemented into the system by default to pick out specific errors the script may run across. However, exception handling also becomes more customized when the script writer creates custom exceptions if the script performs a certain way outside the parameters of what is expected.

Pickling in Python
	As defined by many online sources, pickling “serializes” the intended object first before writing it to a file. It is the method used to convert a python object such as a list or dictionary into a character stream, which will contain all the information needed to put the object or information back together in another python script.

Source: https://www.geeksforgeeks.org/understanding-python-pickling-example/

Structured Error Handling
	Structured error handling is a great way to define and identify errors as objects. Python by default as some set up. These errors can assist in identifying reasons a script is not running as expected. In addition, this also allows the script writer to define their own error types. For example, in the script created in this assignment, a range of numbers was used. When the person running the script inputs a number outside the defined range, however, an error will show, telling the user to input a number inside that range. 

Source: https://docs.progress.com/bundle/openedge-abl-error-handling-117/page/What-is-structured-error-handling.html#:~:text=Structured%20error%20handling%20is%20an,your%20own%20error%20types%20(classes)



Creating the Program

Pickling: 
	The example of pickling in this script is shown by a function created to write to a file in binary, as well as a second function used to read the information from the file.




Exception Error Handling:
	Exception Error Handling is show in this script, first with a custom exception called ‘RangeError’, which will show if the user. Inputs a number outside the given range. 

















	It is followed later in the script by a try except that defines the situation in which a RangeError() will be activated. After the conditions are defined, the errors also have to be decided how they will appear on the screen in the situation that they are raised. 














Results





![image](https://user-images.githubusercontent.com/104462632/171405822-68d893b1-83d6-489c-bbfe-e3c6d223f9ba.png)