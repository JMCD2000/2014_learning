#######################################################################
# Author: Jonathan McDonald
# CST 100 Fall B
# ID: 1208311061
# Section:
# Date: 11/25/2014
#######################################################################
#   PROGRAM DESCRIPTION
#   This program takes a list of integers entered by the user and returns a dictionary
#   of the averages broken out by All numbers, Positive numbers and Negative numbers.
#
#   DESCRIPTION OF VARIABLES
#   NAME	| TYPE	| DESCRIPTION
#   -------------------------------------------------------------------
#   num_list_r	| list	| passed list used to find the average of the list range
#   num_mun_r	| int	| number of numbers in num_list_r, used to divide total_r
#   total_r		| int	| running total of num_list_r as iterated
#   r		| var	| range iteration variable
#   avg_range	| int	| average of all the numbers in the complete list
#   num_list_p	| list	| passed list used to find the average of the list positive numbers
#   num_mun_p	| int	| number of numbers in num_list_p, used to divide total_p
#   total_p	| int	| running total of num_list_p as iterated
#   p		| var	| positive iteration variable
#   avg_pos	| int	| average of all the positive numbers in the list including zero(s)
#   num_list_n	| list	| passed list used to find the average of the list negative numbers
#   num_mun_n	| int	| number of numbers in num_list_n, used to divide total_n
#   total_n	| int	| running total of num_list_n as iterated
#   n		| var	| negative iteration variable
#   avg_neg	| int	| average of all the negative numbers in the list excluding zero
#   -------------------------------------------------------------------
#######################################################################

##*  MAIN PROGRAM  *##

#*  Declare and initialize variables  *#

instruct = 'Enter any number of intigers,\nsome positive and negative\nalong with some zeros: '
while_collect = 'Enter another number or -9999 to finish entering: '

#*  Set initial conditions  *#

ent_num = int() #entered number value#
list_ent_num = [ ] #list of entered numbers#
dict_avg = {'Avg_All_Num':'NULL', 'Avg_Pos_Num':'NULL', 'Avg_Neg_Num':'NULL'}

#*  Define functions  *#

def find_avg_range(num_list_r): #find the average number of passed list range#
    num_num_r = len(num_list_r) #number of numbers equals length of list#
    total_r = 0 #set total of numbers equal to zero#
    for r in num_list_r: #for number in range of list#
        total_r = total_r + r #accumulate the total through each step#
    avg_range = total_r//num_num_r #average of all entered numbers divided by number of numbers#
    return avg_range #average of all entered numbers#
	
def find_avg_pos(num_list_p): #find the average positive number of passed list#
    num_num_p = 0 #set number of numbers equal to zero#
    total_p = 0 #set total of numbers equal to zero#
    for p in num_list_p: #for number in range of list#
        if p >= 0: #if number is greater than or equal to zero#
            num_num_p += 1 #number of numbers when true#
            total_p = total_p + p #accumulate the total through each step#
        #else: pass if false do nothing#
    if num_num_p == 0: #check for no positive numbers provided before division#
        return('N/A') #dictionary value remains N/A#
    else:
        avg_pos = total_p//num_num_p #average of all entered numbers divided by number of numbers#
    return avg_pos #average of all positive numbers including zero#

def find_avg_neg(num_list_n): #find the average negative number of passed list#
    num_num_n = 0 #set number of numbers equal to zero#
    total_n = 0 #set total of numbers equal to zero#
    for n in num_list_n: #for number in range of list#
        if n < 0: #if number is less than zero#
            num_num_n += 1 #number of numbers when true#
            total_n = total_n + n #accumulate the total through each step#
        #else: pass if false do nothing#
    if num_num_n == 0: #check for no negative numbers provided before division#
        return ('N/A') #dictionary value remains N/A#
    else:
        avg_neg = total_n//num_num_n #average of all entered numbers divided by number of numbers#
    return avg_neg #average of all negative numbers entered#
	
#*  Run program  *#

#* Collect user input *#

print('This program will take your numbers and return an average breakdown\n')
print(instruct,'\n')
while ent_num != '-9999': #while the user keeps entering numbers not equal to sentinel value#
    ent_num = input(print(while_collect)) #recast input as integer#
    if ent_num =='-9999': #this checks for sentinel value#
        break #if true, break out and don't add sentinel value to user list#
    while (ent_num .isalpha()): #this is checking for valid entry#
        ent_num = input( print( "Please enter a correct selection.")) #reassigns reselection#
        if ent_num == '-9999': #this checks for sentinel value#
            break #if true, break out and don't add sentinel value to user list#
    list_ent_num.append(int(ent_num)) #re-class from string to integer and append to list#

#* Check for NULL list else find averages and update dictionary of averages *#

if len(list_ent_num) == 0: #if user enters sentinel value there is nothing to do#
    print("You didn't enter any values") #jump to end of main to exit#
else:
    dict_avg['Avg_All_Num'] = find_avg_range(list_ent_num) #find the average number of passed list range#
    dict_avg['Avg_Pos_Num'] = find_avg_pos(list_ent_num) #find the average positive number of passed list#
    dict_avg['Avg_Neg_Num'] = find_avg_neg(list_ent_num) #find the average negative number of passed list#
    
    #* Print completed user list *#

    print('\nThe list of all numbers entered is:\n',list_ent_num)

    #* Print dictionary *#

    print('\nThe dictionary with averages is:\n',dict_avg)
    
##* END OF MAIN PROGRAM *##

print('\n\nend of program')

##*  Exit the program  *##

#######################################################################
##* END OF LINE *##
