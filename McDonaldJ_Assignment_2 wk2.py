#######################################################################
# Author: Jonathan McDonald
# CST 100 Fall B
# ID: 1208311061
# Section:
# Date: 10/28/2014
#######################################################################

#   PROGRAM DESCRIPTION
#   This program will build a snowman with the given design requirements listed.
#   The snowman should be on a blue background, and should be drawn filled with white.
#   The outline of the snowman should be in black.
#   The snowman’s body should be made of 3 filled circles.
#   The outline of each circle should be 3 pixels wide.
#   The bottom circle should have a radius of 100 pixels.
#   The middle circle should have a radius of 70 pixels.
#   The top circle should have a radius of 40 pixels.
#   Each circle should be centered above the one below it (except the bottom circle, which can be located anywhere).
#   There should be no gap between the circles.
#   Give the snowman a mouth, eyes, and a nose (a hat is optional).
#   Make sure to include two stick-arms and at least two fingers on each hand.
#
#   DESCRIPTION OF VARIABLES
#   NAME		| TYPE	| DESCRIPTION
#   -------------------------------------------------------------------
#   bot_ball                           | str	| the snowman object bottom ball
#   mid_ball                          | str	| the snowman object middle ball
#   top_ball                           | str	| the snowman object top ball
#   r_bot_ball                        | int	| Radius of bot_ball in pixels
#   r_mid_ball                       | int	| Radius of mid_ball in pixels
#   r_top_ball                        | int	| Radius of top_ball in pixels
#   ls_bot_ball                      | int	| Length of side of polygon in pixels
#   ls_mid_ball                     | int	| Length of side of polygon in pixels
#   ls_top_ball                      | int	| Length of side of polygon in pixels
#   step_counter_b  	| int	| number of sides in the ball polygon, bottom
#   step_counter_m	| int	| number of sides in the ball polygon, middle
#   step_counter_t	              | int	| number of sides in the ball polygon, top
#   turn_deg_b		| float	| degrees of turn for each side, bottom
#   turn_deg_m		| float	| degrees of turn for each side, middle
#   turn_deg_t		| float	| degrees of turn for each side, top
#   e_hat			| str	| the snowman object extra hat, not used
#   alpha_t		| str	| the assigned name of the turtle, alpha turtle
#   -------------------------------------------------------------------
#######################################################################

##*  MAIN PROGRAM  *##
import math #get extended math functionality#
import turtle #get turtle extension#
wn = turtle.Screen() #load turtle screen#
wn.bgcolor("blue") #set background screen color#

#*  Declare and initialize variables  *#

r_bot_ball = int(100) ##this is a given size radius##
r_mid_ball = int(70) ##this is a given size radius##
r_top_ball = int(40) ##this is a given size radius##
step_counter_b = 78 ##this is the number of sides in the polygon, worked till x.0... hand comp hard coded##
step_counter_m = 73 ##this is the number of sides in the polygon, worked till x.0... hand comp hard coded##
step_counter_t = 50 ##this is the number of sides in the polygon, worked till x.0... hand comp hard coded##

#*  Set initial conditions  *#

alpha_t = turtle.Turtle() ##assign name to turtle##
alpha_t.pensize(3) ##set line width##
alpha_t.goto(0,0) ##verify starting position##
alpha_t.penup() ##don't draw##
alpha_t.setheading(0) ##facing 0 deg east##

#*  Define functions  *#

def length_of_side(r_ball,ns): ##this finds the length of the side##
    return int((2*r_ball)*(math.sin(3.1459/ns))) ##returns truncated answer for pixels##

def deg_of_turn(ns): ##this finds the degree of the turns##
    return round(360/ns,2) ##returns answer rounded to two places for simplicity##
	
def dr_ball(rad,side,step,turn): ##draw ball (ball radius, length of side, number of sides, degree of turn)##
    alpha_t.setheading(180) ##turn from east to face west for travel##
    alpha_t.pendown() ##draw##
    alpha_t.fillcolor("white") ##fill shape color##
    alpha_t.begin_fill() #start shape outline to fill##
    alpha_t.forward(side) #this is first side##
    for x in range(0,step-1): ##repeat till done##
        alpha_t.left(turn)
        alpha_t.forward(side)
    alpha_t.end_fill() ##end shape outline to fill##
    alpha_t.penup() ##stop draw##
    
def charcoal(color): ##(turtle color)##
    alpha_t.setheading(180) ##turn from east to face west for travel##
    alpha_t.pendown() ##draw##
    alpha_t.color(color) ##turtle color##
    alpha_t.fillcolor(color) ##fill shape color##
    alpha_t.begin_fill() #start shape outline to fill##
    for x in range(0,4): ##repeat till done##
        alpha_t.left(90)
        alpha_t.forward(5)
    alpha_t.end_fill() ##end shape outline to fill##
    alpha_t.penup() ##stop draw##

def mouth(head,turn_up): ##(heading to start moving, direction of corner of mouth##
    alpha_t.setheading(head) ##facing out from center line of body##
    alpha_t.pendown() ##draw##
    alpha_t.forward(10) ##draw side##
    alpha_t.setheading(turn_up) ##turn corner of mouth##
    alpha_t.forward(5) ##draw corner of mouth##
    alpha_t.penup() ##stop draw##

    
def arm_hand(head,color,direction): ##(heading to start moving, turtle color, direction of elbow bend##
    alpha_t.setheading(head) ##turn from body for travel##
    alpha_t.pendown() ##draw##
    alpha_t.color(color) ##turtle color##
    alpha_t.forward(30)
    alpha_t.setheading(direction) ##direction of elbow break##
    alpha_t.forward(30)
    alpha_t.left(45)
    alpha_t.forward(10)
    alpha_t.left(180)
    alpha_t.forward(10)
    alpha_t.left(45)
    alpha_t.forward(10)
    alpha_t.penup() ##stop draw##
    
def reset_home(): ##return turtle home##
    alpha_t.goto(0,0) ##go to starting position##
    alpha_t.setheading(0) ##facing 0 deg east##
    alpha_t.color("black") ##turtle back to black##
    
#*  Find length of sides and angle of turn  *#

ls_bot_ball = length_of_side(r_bot_ball,step_counter_b) ##assign length to function answer and pass ( radius, number of sides)##
ls_mid_ball = length_of_side(r_mid_ball,step_counter_m) ##assign length to function answer and pass ( radius, number of sides)##
ls_top_ball = length_of_side(r_top_ball,step_counter_t) ##assign length to function answer and pass ( radius, number of sides)##

turn_deg_b = deg_of_turn(step_counter_b) ##assign degree of turn to function answer and pass ( number of sides)##
turn_deg_m = deg_of_turn(step_counter_m) ##assign degree of turn to function answer and pass ( number of sides)##
turn_deg_t = deg_of_turn(step_counter_t) ##assign degree of turn to function answer and pass ( number of sides)##

#*  Build snow body  *#

#bottom ball#
alpha_t.goto(0,-r_mid_ball) ##go to starting position##
dr_ball(r_bot_ball,ls_bot_ball,step_counter_b,turn_deg_b) ##ball radius, length of side, number of sides, degree of turn##
reset_home() ##return turtle home##

#middle ball#
alpha_t.goto(0,r_mid_ball) ##go to starting position##
dr_ball(r_mid_ball,ls_mid_ball,step_counter_m,turn_deg_m) ##ball radius, length of side, number of sides, degree of turn##
reset_home() ##return turtle home##

#top ball#
alpha_t.goto(0,(r_mid_ball+(2*r_top_ball))) ##go to starting position##
dr_ball(r_top_ball,ls_top_ball,step_counter_t,turn_deg_t) ##ball radius, length of side, number of sides, degree of turn##
reset_home() ##return turtle home##

#*  Add charcoal  *#

#left eye#
alpha_t.goto(-15,(r_mid_ball+r_top_ball+5)) ##go to starting position left eye + size of eye##
charcoal("black") ##turtle color##
reset_home() ##return turtle home##

#right eye#
alpha_t.goto(10,(r_mid_ball+r_top_ball+5)) ##go to starting position right eye+ size of eye##
charcoal("black") ##turtle color##
reset_home() ##return turtle home##

#right side of mouth#
alpha_t.goto(0,(r_mid_ball+r_top_ball)-20) ##go to starting position for right side##
mouth(0, 45) ##(heading to start moving = 0, direction of corner of mouth = 45##
reset_home() ##return turtle home##

#left side of mouth#
alpha_t.goto(0,(r_mid_ball+r_top_ball)-20) ##go to starting position for left side##
mouth(180, 135) ##(heading to start moving = 180, direction of corner of mouth = 135##
reset_home() ##return turtle home##

#top button#
alpha_t.goto(-2,(r_mid_ball/2)) ##go to starting position middle ball top button##
charcoal("black") ##turtle color##
reset_home() ##return turtle home##

#middle button#
alpha_t.goto(-2,(0)) ##go to starting position middle ball middle button##
charcoal("black") ##turtle color##
reset_home() ##return turtle home##

#bottom button#
alpha_t.goto(-2,(-r_mid_ball/2)) ##go to starting position middle ball bottom button##
charcoal("black") ##turtle color##
reset_home() ##return turtle home##

#*  Add carrot  *#

#nose#
alpha_t.goto(-2,(r_mid_ball+r_top_ball)) ##go to starting position left + size of eye##
charcoal("orange") ##turtle color##
reset_home() ##return turtle home##

#*  Add arms  *#

#left arm
alpha_t.goto(r_mid_ball,0) ##go to left side of body##
arm_hand(0,"brown",20) ##(heading=0, turtle color=brown, direction of elbow bend=20##
reset_home() ##return turtle home##

#right arm
alpha_t.goto(-r_mid_ball,0) ##go to left side of body##
arm_hand(180,"brown",200) ##(heading=180, turtle color=brown, direction of elbow bend=200##
reset_home() ##return turtle home##

##* END OF MAIN PROGRAM *##

alpha_t.hideturtle() ##hide turtle from finished drawing##

##*  Exit the program  *##

wn.exitonclick() #hold program open till user clicks#

#######################################################################
##* END OF LINE *##
