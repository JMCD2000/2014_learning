#######################################################################
# Author: Jonathan McDonald
# CST 100 Fall B
# ID: 1208311061
# Section:
# Date: 11/05/2014
#######################################################################
#
#   PROGRAM DESCRIPTION
#   This program will referee a two player game of Rock Paper Scissor. 
#   Each player will enter their toss and the program will decide the winner. As a method
#   of logic the default path is always true being player one with false being player two. The
#   user is able to enter upper and lower case and the code converts to lower for comparison.
#   A while loop is used to control the number of games to be played.
#
#   DESCRIPTION OF VARIABLES
#   NAME	| TYPE	| DESCRIPTION
#   -------------------------------------------------------------------
#   instruct	| str	| the opening instructions on how to play
#   intro_name1     | str	| the opening introduction to get player 1 name
#   intro_name2     | str	| the opening introduction to get player 2 name
#   play_toss	| str	| the opening introduction to get player toss
#   winner	| str	| return string for winner
#   user1_win	| int	| the number of wins for player 1
#   user2_win	| int	| the number of wins for player 2
#   tie_tie              | int         | the number of tie games
#   gm_count        | int         | game increment counter
#   num_rds          | int         | total number of rounds to be played
#   user1_name      | str	| the name of player one
#   user2_name	| str	| the name of player two
#   user1_toss	| int	| the toss for player 1
#   user2_toss	| int	| the toss for player 2
#   player_t_f         | str        | return player true or false for winner
#   user_points      | int        | return player points for winner
#   -------------------------------------------------------------------
#######################################################################

##*  MAIN PROGRAM  *##

#*  Declare and initialize variables  *#

instruct = "\nTo play use:\n\t'R' or 'r' for rock\n\t'P' or 'p' for paper\n\t'S' or 's' for scissor"
intro_name1 = "Hello! Player 1 what is your name? "
intro_name2 = "Hello! Player 2 what is your name? "
play_toss = "What is your toss? "
winner = "has won this round."

#*  Set initial conditions  *#

user1_win = 0 #score is zero#
user2_win = 0 #score is zero#
tie_tie = 0 #used to count the number of ties#
gm_count = 0 #used for rounds and loop exit#
num_rds = 5 #used for the number of rounds for the game#

#*  Define functions  *#
            
def get_name (player_num): #this gets the users name#
    user_name = input( print("Hello! ", player_num, " what is your name?")); #loads intro_name by player number#
    print( "Hi, ", user_name)
    return user_name

def get_toss (player_name): #this gets the users toss#
    print (instruct)
    user_toss = input( print( "Hi, ", player_name, play_toss ) ) #assigns play toss#
    user_toss = user_toss.lower(); #user_toss.lower() is to allow both upper and lower case but then converts to lower case to save on logic and lines of code#
    while (user_toss != 'r' and user_toss != 'p' and user_toss != 's'): #this is checking for valid tosses#
        print (instruct)
        user_toss = input( print( "Hi, ", player_name,"Please enter a correct toss.") ) #assigns play toss#
        user_toss = user_toss.lower(); #user_toss.lower() is to allow both upper and lower case but then converts to lower case to save on logic and lines of code#
    return user_toss
		
def win_tree (play1, play2, toss1, toss2): #this is the hard coded win tree#
    if toss1 == toss2: #draw no winner#
        print ("There was a tie, no winner.")
        return "none" #no winner#
    if toss1 == 'r' and toss2 == 's': #rock beats scissors#
        print (play1, winner)
        return "true" #player one won the toss#
    if toss1 == 'p' and toss2 == 'r': #paper beats rock#
        print (play1, winner)
        return "true" #player one won the toss#
    if toss1 == 's' and toss2 == 'p': #scissors beats paper#
        print (play1, winner)
        return "true" #player one won the toss#
    else: #all others are false and player two has won the toss#
        print (play2, winner)
        return "false" #player two won the toss#
               
#*  Get player names  *#

print("Welcome to Rock Paper Scissors Best of", num_rds)
user1_name = get_name("Player 1") #get user 1 and assign name#
user2_name = get_name("Player 2") #get user 2 and assign name#

#*  Begin game loop  *#
while gm_count < num_rds: #this limits the number of rounds#
    gm_count = gm_count + 1 #looping variable increment to exit#

    #*  Get toss  *#
	
    user1_toss  = get_toss(user1_name) #get user 1 toss and assign#
    user2_toss  = get_toss(user2_name) #get user 2 toss and assign#
    
    #*  Assign winnings  *#
	
    player_t_f = win_tree (user1_name, user2_name, user1_toss, user2_toss) #pass player names and toss. Returns and then assigns the win#
    if player_t_f == "true": #predefined to be player 1 value that will increment that score#
        user1_win = user1_win + 1
    if player_t_f == "false": #predefined to be player 2 value that will increment that score#
        user2_win = user2_win + 1
    else:
       player_t_f == "none" #predefined to do nothing, no score incremented#
       tie_tie = tie_tie + 1
    
    #*  Show scores  *#

    print("Round", gm_count, "of", num_rds) #round counter#
    print(user1_name,"score is", user1_win) #number of games won#
    print(user2_name, "score is", user2_win) #number of games won#
    print("Number of tie games is", tie_tie) #number of tie games#
    if user1_win > user2_win:
       print(user1_name, "is winning!")
    if user1_win < user2_win:
       print(user2_name, "is winning!")
    else:
        print ("There is a tied score, no winner.") 

#*  Show final scores  *#

print("\nFinal scores for this game")
print(user1_name,"score is", user1_win)  #number of games won#
print(user2_name, "score is", user2_win)  #number of games won#
print("Number of tie games is", tie_tie) #number of tie games#
if user1_win > user2_win:
    print(user1_name, "has won!")
if user1_win < user2_win:
    print(user2_name, "has won!")
else:
    print ("There is a tied score, no winner.") 

print("Game Over")

##* END OF MAIN PROGRAM *##

##*  Exit the program  *##

#######################################################################
##* END OF LINE *##
