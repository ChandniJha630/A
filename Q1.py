import turtle

# Initialize the turtle screen
screen = turtle.Screen()
screen.title("Drone Movement Simulation")

# Create a turtle object for the drone
drone = turtle.Turtle()

# Function to move the drone forward
def move_forward():
    drone.forward(50)  # You can adjust the distance as needed

# Function to move the drone backward
def move_backward():
    drone.backward(50)  # You can adjust the distance as needed

# Function to turn the drone left
def move_left():
    drone.left(90)  # You can adjust the angle as needed

# Function to turn the drone right
def move_right():
    drone.right(90)  # You can adjust the angle as needed

# Keyboard bindings
screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")

# Close the window when clicked
screen.exitonclick()
