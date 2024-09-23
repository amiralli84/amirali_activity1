"""
This program is responsible for drawing a scene including a table, cake, and a candle
This program uses eight functions, where main(), drawTable(), and drawCake() are the key functions

The concept of this program is to use coordinates to draw lines to form 3D and 2D structures
    therefore .goto() is a key method of the Turtle class used in this program

"""

# importing the Screen and Turtle from the turtle library
from turtle import Screen, Turtle

# The cursor otherwise known as the turta is a global variable, accessable by all functions
cursor = Turtle()

def drawTableBase(point_a_xcor, point_a_ycor, table_length, table_horizontal_margin, table_depth, table_width, table_color):
    """
    This function is responsible for drawing the base of the table
    This function has seven parameters and requires seven arguments
    """

    # Moving the cursor to point A, this will make it easier for this function to begin
    cursor.penup()
    cursor.goto(point_a_xcor, point_a_ycor)

    # Drawing the table
    cursor.pendown()

    cursor.begin_fill()
    cursor.fillcolor(table_color)
    cursor.pencolor(table_color)
    
    point_b_xcor = point_a_xcor + table_length
    point_b_ycor = point_a_ycor
    cursor.goto(point_b_xcor, point_b_ycor)

    point_c_xcor = point_b_xcor - table_horizontal_margin
    point_c_ycor = point_b_ycor + table_width
    cursor.goto(point_c_xcor, point_c_ycor)

    point_d_xcor = point_c_xcor - (table_length - (table_horizontal_margin * 2))
    point_d_ycor = point_c_ycor
    cursor.goto(point_d_xcor, point_d_ycor)

    cursor.goto(point_a_xcor, point_a_ycor)

    point_e_xcor = point_a_xcor
    point_e_ycor = point_a_ycor - table_depth
    cursor.goto(point_e_xcor, point_e_ycor)

    point_f_xcor = point_b_xcor
    point_f_ycor = point_b_ycor - table_depth
    cursor.goto(point_f_xcor, point_f_ycor)

    cursor.goto(point_b_xcor, point_b_ycor)

    cursor.end_fill()

    # Moving the cursor to point E, this will make it easier for the drawTableLegs function to begin
    cursor.penup()
    cursor.goto(point_e_xcor, point_e_ycor)

def drawTableLeg(point_a_xcor, point_a_ycor, table_color, leg_length, leg_width):
    """
    This function is responsible for drawing the table leg
    This function has five parameters and requires five arguments
    """

    # # Moving the cursor to point A, this will make it easier for this function to begin
    cursor.penup()
    cursor.goto(point_a_xcor, point_a_ycor)

    cursor.pendown()

    # Drawing the table leg
    cursor.begin_fill()
    cursor.fillcolor(table_color)
    cursor.pencolor(table_color)

    point_b_xcor = point_a_xcor
    point_b_ycor = point_a_ycor - leg_length
    cursor.goto(point_b_xcor, point_b_ycor)

    point_c_xcor = point_b_xcor + leg_width
    point_c_ycor = point_b_ycor
    cursor.goto(point_c_xcor, point_c_ycor)

    point_d_xcor = point_c_xcor
    point_d_ycor = point_c_ycor + leg_length
    cursor.goto(point_d_xcor, point_d_ycor)

    cursor.goto(point_a_xcor, point_a_ycor)

    cursor.end_fill()

def drawCakeLayer(point_a_xcor, point_a_ycor, cake_lenght, cake_layer_height, layer_color):
    """
    This function is responsible for drawing a cake layer
    This function has five parameters and requires five arguments
    """

    # Moving the cursor to point A, this will make it easier for this function to begin
    cursor.penup()
    cursor.goto(point_a_xcor, point_a_ycor)
    
    # Drawing the cake layer
    cursor.pendown()
    cursor.begin_fill()
    cursor.fillcolor(layer_color)
    cursor.pencolor(layer_color)

    point_b_xcor = point_a_xcor + cake_lenght
    point_b_ycor = point_a_ycor
    cursor.goto(point_b_xcor, point_b_ycor)

    point_c_xcor = point_b_xcor
    point_c_ycor = point_b_ycor + cake_layer_height
    cursor.goto(point_c_xcor, point_c_ycor)

    point_d_xcor = point_c_xcor - cake_lenght
    point_d_ycor = point_c_ycor
    cursor.goto(point_d_xcor, point_d_ycor)

    cursor.goto(point_a_xcor, point_a_ycor)

    cursor.end_fill()

def drawCakeFrosting(point_a_xcor, point_a_ycor, semi_circle_radius, frosting_color):
    """
    This function is responsbile for drawing the frosting
    This function has four parameters and requires four arugments
    """

    # Moving the cursor to point A, this will make it easier for this function to begin
    cursor.penup()
    cursor.goto(point_a_xcor, point_a_ycor)

    # Drawing the frosting
    cursor.pendown()
    cursor.begin_fill()
    cursor.fillcolor(frosting_color)
    cursor.pencolor(frosting_color)
    cursor.circle(semi_circle_radius, 180)
    cursor.goto(point_a_xcor, point_a_ycor)
    cursor.end_fill()

    cursor.right(180)
    
def drawCakeCandle(midpoint_x, midpoint_y, candle_height, candle_width, candle_color):
    """
    This function is responsible for drawing the candle
    This function has five parameters and requires five arugments
    """

    # Candle calculations
    midpoint_margin = candle_width / 2

    # Drawing the candle
    cursor.penup()
    cursor.goto(midpoint_x, midpoint_y)

    cursor.pendown()
    cursor.begin_fill()
    cursor.fillcolor(candle_color)
    cursor.pencolor(candle_color)
 
    cursor.left(90)
    cursor.forward(midpoint_margin)
    cursor.left(90)
    cursor.forward(candle_height)
    cursor.left(90)
    cursor.forward(midpoint_margin * 2)
    cursor.left(90)
    cursor.forward(candle_height)
    cursor.left(90)
    cursor.forward(midpoint_margin)

    cursor.end_fill()

def drawCake(point_a_xcor, point_a_ycor, cake_height, table_length, cake_layer_one_color, cake_layer_two_color, cake_layer_three_color, cake_layer_four_color, frosting_color, candle_color):
    """
    This function is responsible for drawing the cake
    This function will call the supporting functions drawCakeLayer, drawCakeFrosting, and drawCakeCandle
    This function has nine parameters and requires nine arguments
    """

    # Hardcoded cake and candle dimensions
    number_of_layers = 4
    cake_horizontal_margin = 40
    cake_vertical_margin = 20
    candle_height = 20
    candle_width = 10
    
    # Cake layer calculations
    cake_layer_height = cake_height / number_of_layers
    cake_length = table_length - (cake_horizontal_margin * 2)
    semi_circle_radius = cake_length / 8


    layer_one_point_a_xcor = point_a_xcor + cake_horizontal_margin
    layer_one_point_a_ycor = point_a_ycor + cake_vertical_margin

    layer_two_point_a_xcor = layer_one_point_a_xcor
    layer_two_point_a_ycor = layer_one_point_a_ycor + cake_layer_height

    layer_three_point_a_xcor = layer_one_point_a_xcor
    layer_three_point_a_ycor = layer_one_point_a_ycor + (cake_layer_height * 2)

    layer_four_point_a_xcor = layer_one_point_a_xcor
    layer_four_point_a_ycor = layer_one_point_a_ycor + (cake_layer_height * 3)

    # Drawing the cake
    drawCakeLayer(layer_one_point_a_xcor, layer_one_point_a_ycor, cake_length, cake_layer_height, cake_layer_one_color)
    drawCakeLayer(layer_two_point_a_xcor, layer_two_point_a_ycor, cake_length, cake_layer_height, cake_layer_two_color)
    drawCakeLayer(layer_three_point_a_xcor, layer_three_point_a_ycor, cake_length, cake_layer_height, cake_layer_three_color)
    drawCakeLayer(layer_four_point_a_xcor, layer_four_point_a_ycor, cake_length, cake_layer_height, cake_layer_four_color)

    # Frosting calculations
    cursor.penup()
    cursor.right(90)

    frosting_one_xcor = layer_four_point_a_xcor
    frosting_one_ycor = layer_four_point_a_ycor + cake_layer_height

    frosting_two_xcor = frosting_one_xcor + (semi_circle_radius * 2)
    frosting_two_ycor = frosting_one_ycor

    frosting_three_xcor = frosting_one_xcor + (semi_circle_radius * 4)
    frosting_three_ycor = frosting_one_ycor

    frosting_four_xcor = frosting_one_xcor + (semi_circle_radius * 6)
    frosting_four_ycor = frosting_one_ycor

    # Drawing the frosting
    drawCakeFrosting(frosting_one_xcor, frosting_one_ycor, semi_circle_radius, frosting_color)
    drawCakeFrosting(frosting_two_xcor, frosting_two_ycor, semi_circle_radius, frosting_color)
    drawCakeFrosting(frosting_three_xcor, frosting_three_ycor, semi_circle_radius, frosting_color)
    drawCakeFrosting(frosting_four_xcor, frosting_four_ycor, semi_circle_radius, frosting_color)

    # Moving the cursor to midpoint, this will make it easier for the drawCakeCandle to begin
    cursor.penup()

    cake_midpoint_xcor = frosting_one_xcor + (semi_circle_radius * 4)
    cake_midpoint_ycor = frosting_one_ycor

    drawCakeCandle(cake_midpoint_xcor, cake_midpoint_ycor, candle_height, candle_width, candle_color)
    
def drawTable(point_a_xcor, point_a_ycor, table_length, table_color, leg_length):
    """
    This function is responsible for drawing the table
    This function will call the supporting functions drawTableBase and drawTableLeg
    This function has five parameters and requires five arguments
    """

    # Hardcoded table dimensions
    table_width = table_length / 4
    table_horizontal_margin = 25
    table_depth = 20

    # Drawing the table
    drawTableBase(point_a_xcor, point_a_ycor, table_length, table_horizontal_margin, table_depth, table_width, table_color)
    
    # Table leg calculations
    front_leg_one_point_a_xcor = point_a_xcor
    front_leg_one_point_a_ycor = point_a_ycor - table_depth

    front_leg_two_point_a_xcor = front_leg_one_point_a_xcor + table_length
    front_leg_two_point_a_ycor = front_leg_one_point_a_ycor

    back_leg_one_point_a_xcor = point_a_xcor + table_horizontal_margin
    back_leg_one_point_a_ycor = point_a_ycor - table_depth

    back_leg_two_point_a_xcor = front_leg_two_point_a_xcor - table_horizontal_margin
    back_leg_two_point_a_ycor = back_leg_one_point_a_ycor

    back_leg_length = leg_length - 20

    leg_width = table_horizontal_margin / 3

    # Drawing the table legs
    drawTableLeg(front_leg_one_point_a_xcor, front_leg_one_point_a_ycor, table_color, leg_length, leg_width)
    drawTableLeg(front_leg_two_point_a_xcor, front_leg_two_point_a_ycor, table_color, leg_length, -leg_width)
    drawTableLeg(back_leg_one_point_a_xcor, back_leg_one_point_a_ycor, table_color, back_leg_length, leg_width)
    drawTableLeg(back_leg_two_point_a_xcor, back_leg_two_point_a_ycor, table_color, back_leg_length, -leg_width)

    # Moving the cursor to point A, this will make it easier for the drawCake function to begin
    cursor.penup()
    cursor.goto(point_a_xcor, point_a_ycor)

def main():
    """
    This function is the core of the program
    This function will ask the user for inputs and call the supporting functions drawTable and drawCake
    """

    # Asking the user for inputs

    print("""
    _________________________________________________
          
                 GENERAL SPECIFICATIONS
    _________________________________________________
    """)

    screen_background_color = input("Enter the screen's background color: ")
    point_a_xcor = int(input("Enter the x-cor to draw the table from (Minimum 0 | Maximum 10): "))
    point_a_ycor = int(input("Enter the y-cor to draw the table from (Minimum 0 | Maximum 10): "))

    print("""
    _________________________________________________
          
                  TABLE SPECIFICATIONS
    _________________________________________________
    """)

    table_length = int(input("Enter the table's length (Minimum 200 | Maximum 400): "))
    leg_length = int(input("Enter the leg's length (Minimum 100 | Maximum 200): "))
    table_color = input("Enter the table's color: ")

    print("""
    _________________________________________________
          
                  CAKE SPECIFICATIONS
    _________________________________________________
    """)

    cake_height = int(input("Enter the cake's height (Minimum 60 | Maximum 120): "))
    cake_layer_one_color = input("Enter the cake's layer one color: ")
    cake_layer_two_color = input("Enter the cake's layer two color: ")
    cake_layer_three_color = input("Enter the cake's layer three color: ")
    cake_layer_four_color = input("Enter the cake's layer four color: ")
    cake_frosting_color = input("Enter the cake's frosting color: ")
    cake_candle_color = input("Enter the cake's candle color: ")

    # Starting the screen
    screen = Screen()
    screen.bgcolor(screen_background_color)
    
    # Calling the functions
    drawTable(point_a_xcor, point_a_ycor, table_length, table_color, leg_length)
    drawCake(point_a_xcor, point_a_ycor, cake_height, table_length, cake_layer_one_color, cake_layer_two_color, cake_layer_three_color, cake_layer_four_color, cake_frosting_color, cake_candle_color)

    # Returning the cursor back to the starting point
    cursor.penup()
    cursor.goto(point_a_xcor, point_a_ycor)

    print("""
    _________________________________________________
          
        Press the 'X' button to close the screen
    _________________________________________________
    """)

    screen.exitonclick()

if __name__ == "__main__":
    main()

