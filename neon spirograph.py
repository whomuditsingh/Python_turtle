import turtle
import math
import colorsys

def draw_spirograph():
    # 1. Screen Setup
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Mathematical Spirograph")
    screen.tracer(0)  # Turns off animation for instant drawing

    # 2. Turtle Setup
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    
    # 3. Parameters for the "Gears"
    # R is the large circle radius, r is the small circle radius, 
    # and d is the distance of the pen from the center of the small circle.
    R = 125
    r = 75
    d = 125
    
    # 4. Drawing Logic
    # We use colorsys to create a smooth rainbow gradient
    for i in range(361):
        theta = math.radians(i * 10) 
        
        # The Hypotrochoid Formula
        x = (R - r) * math.cos(theta) + d * math.cos(((R - r) / r) * theta)
        y = (R - r) * math.sin(theta) - d * math.sin(((R - r) / r) * theta)
        
        color = colorsys.hsv_to_rgb(i / 360, 1.0, 1.0)
        t.pencolor(color)
        
        # Move turtle
        if i == 0:
            t.up()
            t.goto(x, y)
            t.down()
        else:
            t.goto(x, y)
        
        screen.update()

    screen.exitonclick()

if __name__ == "__main__":
    draw_spirograph()