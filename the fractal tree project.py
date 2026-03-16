import turtle
import random

def draw_tree(branch_length, t):
    """
    Recursively draws a fractal tree.
    """
    # Base case: if the branch is too short, stop drawing
    if branch_length < 5:
        # Add a "leaf" effect by changing color and drawing a circle
        t.color("forest green")
        t.stamp() # Leave a leaf impression
        t.color("saddle brown") # Reset color for branching
        return

    # Draw the current branch (the trunk or a main branch)
    t.pensize(branch_length / 10) # Thicker branches for longer lengths
    t.forward(branch_length)

    # --- Recursive Steps ---
    
    # 1. Prepare to draw the right branch
    # Randomize angle and length reduction for a more natural look
    right_angle = random.uniform(15, 30)
    length_reduction = random.uniform(0.6, 0.8)
    
    t.right(right_angle)
    # Recursively call draw_tree for the right side
    draw_tree(branch_length * length_reduction, t)

    # 2. Prepare to draw the left branch
    # Left angle needs to compensate for the right turn, then add its own angle
    left_angle = random.uniform(15, 30)
    
    t.left(right_angle + left_angle)
    # Recursively call draw_tree for the left side
    draw_tree(branch_length * length_reduction, t)

    # 3. Return to the starting position of this branch
    # This is critical for the recursion to work correctly
    t.right(left_angle)
    t.backward(branch_length)

# --- Main Setup ---
def main():
    # 1. Screen setup
    screen = turtle.Screen()
    screen.bgcolor("sky blue")
    screen.title("Recursive Fractal Tree Generator")

    # 2. Turtle (the "pen") setup
    tree_turtle = turtle.Turtle()
    tree_turtle.color("saddle brown")
    tree_turtle.speed(0) # Fastest speed
    tree_turtle.hideturtle() # Don't show the turtle icon
    
    # 3. Position the turtle at the bottom center, pointing up
    tree_turtle.left(90)
    tree_turtle.up()
    tree_turtle.backward(200) # Move down from the center
    tree_turtle.down()

    # 4. Start drawing the tree (initial trunk length)
    draw_tree(100, tree_turtle)

    # 5. Keep the window open until clicked
    screen.exitonclick()

if __name__ == "__main__":
    main()