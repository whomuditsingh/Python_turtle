import turtle

def langtons_ant():
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.setup(800, 800)
    screen.tracer(0)

    ant = turtle.Turtle()
    ant.shape("square")
    ant.shapesize(0.5)
    ant.speed(0)

    # Keys will be (x, y) tuples, values will be color (0 for white, 1 for black)
    grid = {}

    # The Simulation Loop
    for _ in range(12000): # Run for 12,000 steps
        pos = (round(ant.xcor()), round(ant.ycor()))
        current_color = grid.get(pos, 0)

        if current_color == 0: 
            ant.right(90)
            grid[pos] = 1 
            ant.dot(10, "black")
        else:
            ant.left(90)
            grid[pos] = 0
            ant.dot(10, "white")

        ant.forward(10)
        if _ % 100 == 0:
            screen.update()

    screen.update()
    screen.exitonclick()

if __name__ == "__main__":
    langtons_ant()