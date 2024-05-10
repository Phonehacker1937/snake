Report: Implementation of Object-Oriented Programming Principles and Design Patterns
# Introduction
The goal of this coursework is to implement object-oriented programming principles and design patterns in a Python program. The program is a simple game where a player (represented by a turtle) navigates through a maze to reach a target while avoiding collisions with obstacles. Below, we'll discuss how the program utilizes various OOP principles and design patterns, along with the implementation of file reading/writing functionality.


# Running the Program

To run the program, ensure you have Python installed on your system. Additionally, the program utilizes the turtle module for graphics rendering. Some computers may not have this module installed or may have restrictions that prevent its use. If you encounter issues with the turtle module, you may need to install it separately or use a different environment that supports it.

Here are the general steps to run the program:

Install Python: If you haven't already, download and install Python from the official website: https://www.python.org/downloads/.

Install Turtle Module (if necessary): If the turtle module is not included with your Python installation, you can install it using the following command in your command prompt or terminal:
(pip install PythonTurtle)

Download the Program: Download the Python script containing the game code to your computer.

Run the debuger and the Script: Open a command prompt or terminal, navigate to the directory where the script is located, and run and debug the script using the Python interpreter:

python your_script_name.py
Replace your_script_name.py with the actual name of the Python script.
If you encounter any issues or have further questions, feel free to ask for assistance.


# Example of Polymorphism
 Create the player turtle
 
	player = turtle.Turtle()

	player.shape("triangle")

	player.color("blue")

	player.penup()

	player.speed(0)

# Abstraction
Abstraction hides complex implementation details and exposes only essential features of an object. In the game code, abstraction is achieved by encapsulating the game logic within functions and methods, hiding the implementation details from the user.

# Example of Abstraction
	def move_left():

	    global direction
    
	    player.setheading(180)
    
# Inheritance
Inheritance allows a class to inherit properties and behavior from another class. While not explicitly demonstrated in the code, the Turtle objects inherit properties and behavior from the Turtle class provided by the turtle module.

# Encapsulation
Encapsulation bundles the data (attributes) and methods (functions) that operate on the data into a single unit (class), restricting access to some of the object's components. In the game code, encapsulation is demonstrated by encapsulating game logic within functions and methods.

# Example of Encapsulation
	def save_game_data():
	    with open("game_data.txt", "w") as file:
	        # Player position
	        file.write(f"Player position: {player.position()}\n")
# Design Patterns

# Observer Pattern
The Observer pattern is used to handle keyboard events in the game. Event handling functions (move_left, move_right, move_up, move_down) are registered as observers for specific keyboard events (e.g., key presses), enabling decoupling between event sources and handlers.

# Factory Method Pattern
The Factory Method pattern is used to create new tail segments in the game. Instead of directly instantiating tail segments within the main game loop, the creation of tail segments is delegated to the new_tail_segment factory method, promoting code reuse and consistency.

# Results and Summary
The program successfully implements the defined objectives and functional requirements.
Challenges were faced during the implementation, particularly in managing the movement and collision detection of game elements.
Overall, the program provides a functional and entertaining game experience.
Conclusions
In conclusion, this coursework has achieved its goal of implementing object-oriented programming principles and design patterns in a Python program. The program demonstrates effective use of encapsulation, abstraction, polymorphism, and the Observer and Factory Method design patterns. Future prospects of the program include enhancing gameplay features, optimizing performance, and improving user experience.

