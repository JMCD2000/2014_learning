#######################################################################
# Author: Jonathan McDonald
# CST 100 Fall B
# ID: 1208311061
# Section:
# Date: 10/21/2014
#######################################################################

#PROGRAM DESCRIPTION
#		This is Part 2 of Assignment 1. This program asks for user input
#		in hight, side 1 and side 2 inorder to compute the area of a 
#		trapezoid. It returns to the user the area of the trapezoid.
#
#   DESCRIPTION OF VARIABLES
#   NAME           | TYPE   | DESCRIPTION
#   -------------------------------------------------------------------
#   ans_rtn          | str       | the message to the user with answer
#   side_1           | int        | the user input variable for the first side
#   side_2           | int        | the user input variable for the second side
#   hight              | int        | the user input variable for the hight of trapezoid
#   trap_area       | int        | the computed area of trapezoid and output to user 
#   -------------------------------------------------------------------
#######################################################################

##*  MAIN PROGRAM  *##

#*  Declare and initialize variables  *#

ans_rtn = "The area of the trapezoid is:" ##program return message##

#*  Request input from user  *#

print("This program computes the area of a trapezoid from user input")
side_1 = int(input("Please provide lenght of side one: ")) ##taking input and assigning to variable int##
side_2 = int(input("Please provide lenght of side two: ")) ##taking input and assigning to variable int##
hight = int(input("Please provide the hight of the trapezoid: ")) ##taking input and assigning to variable int##

#*  Run math formula  *#

trap_area = (1.0/2.0)*(side_1 + side_2)*(hight) ##using input in formula to get output ans##

#*  Print output and return results  *#

print(ans_rtn, trap_area) ##print output message and answer##

##* END OF MAIN PROGRAM *##

##*  Exit the program  *##

#######################################################################
##* END OF LINE *##
