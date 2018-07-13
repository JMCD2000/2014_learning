#######################################################################
# Author: Jonathan McDonald
# CST 100 Fall B
# ID: 1208311061
# Section:
# Date: 11/11/2014
#######################################################################
#   PROGRAM DESCRIPTION
#   This program uses nested looping structures to print strings.
#   1) counts from 0 to 9 in each row for ten rows.
#   2) counts ascending from 0 to 9 starting with one position in the first row and
#       increases positions by one for each of the ten total rows.
#   3) counts ascending from 0 to 9 starting with ten positions in the first row and
#       decreases positions by one for each of the ten total rows. This also adds one
#       leading space incremental to center justify the inverted pyramid.
#   4) counts sequentially ascending from 10 to 54 starting with one position in the first row and
#       increases positions by one for each of the nine total rows.
#
#
#   DESCRIPTION OF VARIABLES
#   NAME	| TYPE	| DESCRIPTION
#   -------------------------------------------------------------------
#              	|  	|  
#   -------------------------------------------------------------------
#######################################################################

##*  MAIN PROGRAM  *##

#*  Run pyramid formatting  *#

#segment 1#
#this counts from 0 to 9#
print('\nSegment 1\nThis counts from 0 to 9')
for rows in range(10): #number of rows#
    for col in range(0,10,1): #number of columns#
        print(col,  end = " ") #the end = " " inserts a space between each number#
    print() #this advances to the next line#

#segment 2#
#this counts from 0 to 9 in increments of one by each row#
print('\nSegment 2\nThis counts from 0 to 9 in row increments from 1 position increminting by 1 each row')
inc = 0 #this is the column range that increments to make the stair step pyramid#
for rows in range(11): #number of rows#
    for col in range(inc): #number of columns#
        print(col,  end = " ") #the end = " " inserts a space between each number#
    inc = inc + 1 #this increases the range by one with each pass#
    print() #this advances to the next line#

#segment 3#
#this counts from 0 to 9 in deprecated increments of one by each row and justifies center#
print('\nSegment 3\nThis counts from 0 to 9 in depricated row increments of 1 and adding 1 leading space increment each row')
inc = 10 #this is the depreciation column cell counter#
space = 0 #this is the increasing increment counter for the leading spaces used to center justify#
for rows in range(11): #number of rows#
    print(' '*space, end = "") #the end = " " inserts a space between each number#
    for col in range(inc): #number of columns#
        print(col, end = " ") #the end = " " inserts a space between each number#
    inc = inc - 1 #this decreases the range by one with each pass#
    space = space + 1 #this increases the range by one with each pass#
    print() #this advances to the next line#

#segment 4#
#this counts from 10 to 54 in ascending increments of one by each row and column#
print('\nSegment 4\nThis sequentialy counts from 10 to 54 in increasing row and colunm increments')
start = 10 #starting range number that is incremented by each row#
start_inc = 0 #this increments the starting range by row#
stop = 11 #upper bounded range number that is incremented by each row#
stop_inc = 1 #this increments the upper bounded range by row#
for rows in range(9): #number of rows#
    for col in range(start, stop): #number of columns range with start number and upper bounded number#
        print(col,  end = " ") #the end = " " inserts a space between each number#
    start_inc = start_inc + 1 #this increases the increment by 1 with each pass#
    stop_inc = stop_inc + 1 #this increases the increment by 1 with each pass#
    start = start + start_inc #this increases the starting range by the start_inc with each pass#
    stop = stop + stop_inc #this increases the upper bound range by the stop_inc with each pass#
    print() #this advances to the next line#

##* END OF MAIN PROGRAM *##

print('\n\nEnd of program')

##*  Exit the program  *##

#######################################################################
##* END OF LINE *##
