import turtle
import random


width =600
height = 800
big_score=10
# Set up the screen
screen = turtle.Screen()
screen.setup(width, height)
wn = turtle.Screen()
wn.bgcolor()
wn.tracer(3)



#save data

def save_game_data():
    with open("game_data.txt", "w") as file:
        # Player position
        file.write(f"Player position: {player.position()}\n")
        
        # Target position
        file.write(f"Target position: {target.position()}\n")
        
        # Tail positions
        for i, tail in enumerate(tails):
            file.write(f"Tail {i + 1} position: {tail.position()}\n")
        
        # Score
        file.write(f"Score: {score}\n")
        
        print("Game data saved successfully.")






# Create the player turtle
player = turtle.Turtle()
player.shape("triangle")
player.color("blue")
player.penup()
player.speed(0)

# Create the target turtle
target = turtle.Turtle()
turtle.tracer(0, 0)
target.shape("circle")
target.color("red")
target.penup()
target.speed(0)
target.setposition(random.randint(-290, 290), random.randint(-290, 290))

# Initialize the tail list
tails = []


# Score
score = 0
score_display = turtle.Turtle()
score_display.color("black")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Score: {}".format(score), align="center", font=("sans", 24, "normal"))

# Set up direction as a global variable
direction = 0  # 0 for no movement initially

# Functions
def move_left():
    global direction
    player.setheading(180)  # Set direction to left

def move_right():
    global direction
    player.setheading(0)    # Set direction to right
    
def move_up():
    global direction
    player.setheading(90)   # Set direction to up

def move_down():
    global direction
    player.setheading(270)  # Set direction to down



def load_game_data():
    try:
        with open("game_data.txt", "r") as file:
            lines = file.readlines()

            # Check if there are enough lines for all game data
            if len(lines) < 4:
                raise ValueError("nepilna data")

            # Extract player position
            player_pos = eval(lines[0].split(":")[1])
            player.goto(player_pos)

            # Extract target position
            target_pos = eval(lines[1].split(":")[1])
            target.goto(target_pos)

            # Extract tail positions
            for i, line in enumerate(lines[2:-1]): 
                tail_pos = eval(line.split(":")[1])
                tails[i].goto(tail_pos)

            # Extract score
            global score
            score = int(lines[-1].split(":")[1])

            # Update the score
            score_display.clear()
            score_display.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

            print("Game data loaded successfully.")
    except FileNotFoundError:
        print("No saved game data found.")
    except Exception as e:
        print("Error loading game data:", e)




# Keyboard bindings
screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_down, "Down")
screen.onkeypress(load_game_data, "space")

# Function to create a new tail segment
def new_tail_segment():
    segment = turtle.Turtle()
    segment.shape("square")
    segment.color("blue")
    segment.penup()
    tails.append(segment)


# Main game loop
while True:
    if direction == 1:
        player.setheading(180)  # Set direction to left
    elif direction == 2:
        player.setheading(0)    # Set direction to right
    elif direction == 3:
        player.setheading(90)   # Set direction to up
    elif direction == 4:
        player.setheading(270)  # Set direction to down

    player.forward(0)

    # Check for collision with the target
    if player.distance(target) < 20:
        target.setposition(random.randint(-290, 290), random.randint(-290, 290))
        score += 1
        score_display.clear()
        score_display.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))
        save_game_data()
        #backround img
        if score==1:
            wn.bgpic("giphy.gif")
        elif score==2:
            wn.bgpic("giphy (1).gif")
        elif score==3:
            wn.bgpic("R.gif")
        elif score==4:
            wn.bgpic("four.gif")
        elif score==5:
            wn.bgpic("giphy (4).gif")
        elif score==6:
            wn.bgpic("giphy (2).gif")
        elif score==7:
            wn.bgpic("tenor.gif")
        elif score==8:
            wn.bgpic("8_animationreport.gif")
        elif score==9:
            wn.bgpic("9-dribbble.gif")
        elif score>=10:
            wn.bgpic("source.gif")
        
        # Add a new tail segment
        new_tail_segment()

    # Move each tail segment to the position of the segment in front of it
    for i in range(len(tails) - 1, 0, -1):
        x = tails[i - 1].xcor()
        y = tails[i - 1].ycor()
        tails[i].goto(x, y)

    # Move the first segment to the player's position
    if len(tails) > 0:
        tails[0].goto(player.position())  


    # Borders
    if player.xcor() >= width / 2:
        player.setx(-width / 2)
    elif player.xcor() <= -width / 2:
        player.setx(width / 2)
    elif player.ycor() >= height / 2:
        player.sety(-height / 2)
    elif player.ycor() <= -height / 2:
        player.sety(height / 2)

    player.forward(20)

    # Self collision
    for i in range(len(tails)):
        if player.distance(tails[i]) < 1:
            badscore_display = turtle.Turtle()
            badscore_display.color("black")
            badscore_display.penup()
            badscore_display.hideturtle()
            badscore_display.goto(0, 0)
            badscore_display.write("THE END, {}".format(score), align="center", font=("sans", 50, "bold"))
            screen.update()
            screen.ontimer(None, 1000)  
            turtle.bye()

    # Update the screen
    screen.update()
    screen.ontimer(None, 60)  # Add a delay in milliseconds

# Keep the window open
turtle.done()
