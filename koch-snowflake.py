import turtle

def koch_curve(t, length, depth):
    if depth == 0:
        t.forward(length)
    else:
        new_length = length / 3
        
        koch_curve(t, new_length, depth - 1) # Move forward 1/3
        t.left(60)
        koch_curve(t, new_length, depth - 1) # Peak left
        t.right(120)
        koch_curve(t, new_length, depth - 1) # Peak right
        t.left(60)
        koch_curve(t, new_length, depth - 1) # Final 1/3

def draw_snowflake(t, length, depth):
# A snowflake is just 3 Koch curves joined in a triangle
    for _ in range(3):
        koch_curve(t, length, depth)
        t.right(120)

screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Koch Snowflake Generator")

snowflake_turtle = turtle.Turtle()
snowflake_turtle.speed(0)
snowflake_turtle.penup()
snowflake_turtle.goto(-150, 100)
snowflake_turtle.pendown()
snowflake_turtle.color("royalblue")

# Draw a Level 3 snowflake (change 3 to 4 or 5 for more detail!)
draw_snowflake(snowflake_turtle, 300, 4)

snowflake_turtle.hideturtle()
screen.exitonclick()