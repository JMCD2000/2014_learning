#######################################################################
# Author: Jonathan McDonald
# CST 100 Fall B
# ID: 1208311061
# Section:
# Date: 10/21/2014
#######################################################################

#PROGRAM DESCRIPTION
#		This is Part I of Assignment 1. This program asks for user input
#		in degrees Fahrenheit computes temperature conversion and then
#		returns to user degrees Celsius
#
#   DESCRIPTION OF VARIABLES
#   NAME           | TYPE   | DESCRIPTION
#   -------------------------------------------------------------------
#   ans_rtn          | str       | the message to the user with answer
#   DEG_F          | int        | the user input variable reassigned to int
#   DEG_C          | float     | the computed output variable in Celsius
#   -------------------------------------------------------------------
#######################################################################

##*  MAIN PROGRAM  *##

#*  Declare and initialize variables  *#

ans_rtn = "The answer in degrees Celsius is" ##program return message##

#*  Request input from user  *#

print("This program Converts degrees Fahrenheit to degrees Celsius")
DEG_F = int(input("Please provide a degree in Fahrenheit. ")) ##taking input and assigning to variable int##

#*  Run math conversion  *#

DEG_C = (5.0/9.0)*(DEG_F - 32) ##using input in formula to get output ans##

#*  Print output and return results  *#

print(ans_rtn, DEG_C) ##print message and answer##

##* END OF MAIN PROGRAM *##

##*  Exit the program  *##

#######################################################################
##* END OF LINE *##
