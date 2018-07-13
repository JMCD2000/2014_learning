#######################################################################
# Author: Jonathan McDonald
# CST 100 Fall B
# ID: 1208311061
# Section:
# Date: 11/25/2014
#######################################################################
#   PROGRAM DESCRIPTION
#   
#   This program asks the user to enter some words separated by space 
#   (all in one line). The program then creates a list with the words entered 
#   into a list with string length. The words are checked for length with the 
#   first longest word returned along with the original list.
#
#   DESCRIPTION OF VARIABLES
#   NAME	| TYPE	| DESCRIPTION
#   -------------------------------------------------------------------
#      word        	|  str	|  used to iterate and pass value from list_phrase
#      in_word        	|  str	|  local varible used in build_str_and_len function
#      out_len        	|  int	|  local varible passed from build_str_and_len function
#      in_string       	|  str	|  local varible used in count_length function
#      out_count     	|  int	|  local varible passed from count_length function
#   -------------------------------------------------------------------
#######################################################################

##*  MAIN PROGRAM  *##

#*  Declare and initialize variables  *#

instruct = 'Enter a few words and I will return the longest word.'
user_list = '\nThe list of words entered is:\n'
comp_results = '\nThe longest word in the list is: '

#*  Set initial conditions  *#

ent_phrase = () #entered phrase of words#
list_phrase = [] #ent_phrase split into list of words#
pword = () #phrase word from list_phrase#
len_pword = (0) #length of phrase word#
long_word = () #longest word found#
long_len = (0) #length of longest word#

#*  Define functions  *#

def build_str_and_len(in_word): #take a word from list_phrase and get the length#
    out_len = count_length(in_word) #pass in_word to count_length function and assign#
    return(in_word,out_len) #return the list_phrase word and the length of word#

def count_length(in_string): #take string and count the num of char in string#
    out_count = len(in_string) #get length of in_string and assign#
    return out_count #return the length of the string#

#*  Run program  *#

ent_phrase = input(print(instruct)) #get user phrase and assign to entered_phrase#

list_phrase = ent_phrase.split() #parse phrase string to a list and assign#

print(user_list,list_phrase) #print the entered_phrase as a list#

for word in list_phrase: #step through each word in the list#
                   (pword,len_pword) = build_str_and_len(word) #pass word to function and assign passed word and length of passed word#
                   if (len_pword) > (long_len) : #check if passed word is longer than current longest word#
                       long_len = len_pword #if true reassign longest to passed#
                       long_word = pword #if true reassign longest to passed#
                    #else do nothing you have the first longest word#

print(comp_results, long_word)
                           
##* END OF MAIN PROGRAM *##

print('\n\nend of program')

##*  Exit the program  *##

#######################################################################
##* END OF LINE *##
