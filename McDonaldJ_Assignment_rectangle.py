#######################################################################
# Author: Jonathan McDonald
# CST 100 Fall B
# ID: 1208311061
# Section:
# Date: 12/02/2014
#######################################################################
#   PROGRAM DESCRIPTION
#   
#   This program creates the class Rectangle with built in methods.
#
#   DESCRIPTION OF VARIABLES
#   NAME	| TYPE	| DESCRIPTION
#   -------------------------------------------------------------------
#     
#   -------------------------------------------------------------------
#######################################################################

##*  MAIN PROGRAM  *##

#*  Declare class  *#

class Rectangle(object): #this assumes origin at upper left corner#
    
    def __init__ (self, x, y, width, height): #this makes a new instance of the class object#
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __str__ (self): #this makes allows you to print the object Rectangle#
        return "Rectangle" + "(" + str(self.x) + "," + str(self.y) + "," + str(self.width) + "," + str(self.height) + ")"

    def right(self): #returns the right edge of self#
        rt_x = self.x + self.width #origin plus width, no y axis values#
        return rt_x

    def bottom(self): #returns the bottom edge of self#
        bot_y = self.y + self.height #origin plus height, no x axis values#
        return bot_y

    def size(self): #returns the size of self#
        return "(" + str(self.width) + ", " + str(self.height) + ")"

    def position(self): #returns the origin position x,y#
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def area(self): #returns the area of self#
        rec_area = self.width * self.height #base times height#
        return rec_area

    def expand(self, offset): #this will expand or contract the size and shift the origin#
        int(offset) #recast as integer#
        x_x = self.x - offset
        x_y = self.y - offset
        x_width = self.width + (2 * offset)
        x_height = self.height + (2 * offset)
        x_self = Rectangle(x_x, x_y, x_width, x_height)
        print(x_self)
        return x_self

    def contains_point(self, is_x, is_y): #this is the extra credit method#
        if (self.x <= is_x <= (self.x + self.width)) and (self.y <= is_y <= (self.y + self.height)):
            print(True) 
        else:
            print(False)

                           
##* END OF MAIN PROGRAM *##


##*  Exit the program  *##

#######################################################################
##* END OF LINE *##
