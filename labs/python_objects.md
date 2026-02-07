# Python Objects

In this tutorial, we will build a graphical interactive simulation through object-oriented programming.

## Contents


- [Recap](#recap)

- [Exercise](#exercise)

- [Classes](#classes)

- [Sketch](#sketch)

- [Defining a Ball](#ball)

- [Moving a Ball](#motion)

- [Defining a Simulation](#simulation)

- [Draw the System](#draw)

- [Get the Mouse](#mouse)

- [Interacting with the Mouse](#interacting)

- [Cleaning Up](#cleanup)

- [Next Steps](#next)



## Recap

In our first tutorial, we introduced the idea that computer programs are like empty worlds. To populate those worlds, we can give names to numbers and text. We can breathe life into those objects by defining the rules that dictate their behavior. However, our programs did not know about much else on its own beyond what a number is and how to do arithmetic with it. In other words, the types of objects we could build were limited. In the second tutorial, we brought in libraries to make these worlds graphical by leaning on the work of other developers that came before us. This let us make new types of things even if we were constrained by what those prior developers imagined. Finaly, this tutorial explores how we can tell the computer about new concepts and how we can use that power to create interactive simulations.


## Exercise

We will build a simulation in which balls rush out across the screen, bouncing off the edges once they reach the ends of the sketch. This will demonstrate how to tell the computer about new things and how they behave. Additionally, we will let the user interact with these balls with the mouse. In each of these steps, we will have the computer draw the full path that these balls take, creating branch-like structures across the screen.


## Classes

To tell the computer about a new type of thing, we create a class. Specifically, we will make a class for the balls which are bouncing around and a simulation which tracks all of those balls. About classes A class is like the blueprint or the DNA for something (which we call objects). It says what properties (which we call fields) define that something and what behaviors (which we call methods) we can expect from that thing. Here, behaviors mean things that the objects can do or have be done to them. You can think of fields as variables bound to an object and methods as functions tied to an object. Let's explore an example conceptually before actually building a class for a ball. For this conceptual example, let's return to bank accounts from the first tutorial. It may have fields like owner, balance, and interest rate. These properties define the bank account, offering the information needed for each bank account to function. It may have methods like withdraw, deposit, and give_interest. If we make a BankAccount class, you might have a bank account and I might have a bank account. Each individual bank account is said to be an "instance" of the BankAccount class and each one would have its own owner, balance, and interest rate. We will make our own class in just a moment but, to learn more about classes, see A Byte of Python.


## Sketch

Let's start by making a sketch. import sketchingpy import time WIDTH = 500 # pixels HEIGHT = 400 # pixels sketch = sketchingpy.Sketch2D(WIDTH, HEIGHT) Here, Sketch2D is a class and sketch is an instance. About comments and constants The # refers to a comment as we might have seen in prior example code (anything on the line of code after # is ignored by the computer). We also see some variables in all caps. We call these constants and, by putting it in all caps, we signal to other developers that the value of these variables should not change over time


## Defining a Ball

Let's make our first class. Our ball will have an x and y position on screen. This ball will also be in motion. We will define that movement through velocity as pixels per second in the x and y direction. One important method is called "__init__" which is called when an instance is first made. class Ball: def __init__(self, position_x, position_y, velocity_x, velocity_y): self.position_x = position_x self.position_y = position_y self.velocity_x = velocity_x self.velocity_y = velocity_y This snippet creates the concept of a ball. When that ball is made, we ask for the position and velocity. Finally, within the __init__ method, we create the following fields: position_x, position_y, velocity_x, and velocity_y. Remember self from the previous tutorial? Now we can see now why it is used: the self parameter refers to the instance. By using this parameter, we can manipulate variables tied to that individual instance like position_x. More about self Note that we don't pass self to the method. A parameter value for self is inserted behind the scenes by Python. In other words, the first parameter to every method is always the instance. By convention, the vast majority of Python developers call that parameter self. While you can technically use whatever name you would like, self is very strongly recommended.


## Moving a Ball

Now that we have created the fields on a ball, let's define its behaviors. The ball will "bounce" by reversing its x and / or y velocities. Starting with that: class Ball: def __init__(self, position_x, position_y, velocity_x, velocity_y): self.position_x = position_x self.position_y = position_y self.velocity_x = velocity_x self.velocity_y = velocity_y def reverse_x(self): self.velocity_x = self.velocity_x * -1 def reverse_y(self): self.velocity_y = self.velocity_y * -1 If we had a ball, we could now call ball.reverse_x() to reverse its horizontal direction. Anyway, with that in mind, we now have all the pieces needed to make a method which updates the position of the ball on each step: def update(self, duration): self.position_x = self.position_x + self.velocity_x * duration self.position_y = self.position_y + self.velocity_y * duration if self.position_x > WIDTH: self.position_x = WIDTH self.reverse_x() elif self.position_x HEIGHT: self.position_y = HEIGHT self.reverse_y() elif self.position_y We will call update on each ball for each step within our simulation. About offscreen Note that our if statements are checking if the ball has fallen offscreen. Developers and designers have been thinking hard for a long time about what to do when this happens. Sometimes, folks will have an object falling offscreen appear at the opposite side of the world. This is like how one's position on a map continues moving right as you move west until you reach the edge but, as the Earth is round, you wouldn't fall off but simply would appear on the other side of the map. This is called wrapping. For us, we simply have the ball bounce off the edges. This is an "in-bounds" behavior that imagines that nothing exists past the edge of our flat coordinate system.


## Defining a Simulation

It is common to make a class for an overall simulation as well. This can be used to keep track of time and the different instances that make up the simulated world. class Simulation: def __init__(self): self.balls = [ Ball(WIDTH / 2, HEIGHT / 2, -10, -10), Ball(WIDTH / 2, HEIGHT / 2, -10, 10), Ball(WIDTH / 2, HEIGHT / 2, 10, 0) ] self.last_time = time.time() Notice how we are making three instances of the Ball class. Let's also add an update method to the Simulation class which updates each of those balls using a loop. def update(self): new_time = time.time() duration = new_time - self.last_time self.last_time = new_time for ball in self.balls: ball.update(duration) Now, we have everything we need to simulate this system. In the next step, we will draw the state of the system after updating it.


## Draw the System

We are simulating the system but we haven't yet made it visible. Let's go ahead and create a new simulation and register a function to call on each step of the sketch: simulation = Simulation() def update_and_draw_balls(self): simulation.update() for ball in simulation.balls: sketch.draw_ellipse(ball.position_x, ball.position_y, 2, 2) sketch.on_step(update_and_draw_balls) sketch.show() Here's some more info about draw_ellipse. Need some help? Here's what my code looks like. Anyway, let's go ahead and let this run. Try also changing the initial velocities of the balls or their starting positions. How does that change the patterns displayed to the user?


## Get the Mouse

Next, we want the user to be able to interact with the simulation through the mouse. For this, we need to route that information to each Ball instance. Let's start by updating the on_step callback: def update_and_draw_balls(self): mouse = sketch.get_mouse() mouse_x = mouse.get_pointer_x() mouse_y = mouse.get_pointer_y() simulation.update(mouse_x, mouse_y) for ball in simulation.balls: sketch.draw_ellipse(ball.position_x, ball.position_y, 2, 2) Next, we need to update the simulation (the Simulation class) to take that information: def update(self, mouse_x, mouse_y): new_time = time.time() duration = new_time - self.last_time self.last_time = new_time for ball in self.balls: ball.update(duration, mouse_x, mouse_y) Finally, we need to have the Ball class understand how to respond. This will take a little bit of thinking.


## Interacting with the Mouse

At a high level, we want to see if the mouse is near the ball. If it is, we then change the x velocity if the ball bounces against the cursor horizontally or we change the y velocity if the ball bounces against the cursor vertically. Let's start by writing out this high level logic by changing the Ball's update method: def update(self, duration, mouse_x, mouse_y): self.position_x = self.position_x + self.velocity_x * duration self.position_y = self.position_y + self.velocity_y * duration if self.position_x > WIDTH: self.position_x = WIDTH self.reverse_x() elif self.position_x HEIGHT: self.position_y = HEIGHT self.reverse_y() elif self.position_y This code provides a translation of our thoughts in English to our thoughts in Python. However, there are a few items missing. Let's start by adding a new method in Ball called get_is_near_mouse: def get_is_near_mouse(self, mouse_x, mouse_y): x_near = abs(mouse_x - self.position_x) Here we are using a function that is built into Python called abs which returns the absolute value of a number. If the ball is within 10 pixels, we say that it has collided with the cursor and we check in which direction the velocity should change. For that, let's add a new method called get_hit_mouse_in_direction: def get_hit_mouse_in_direction(self, coordinate, mouse, velocity): if mouse > coordinate and velocity > 0: distance = mouse - coordinate return distance -10 else: return False This function allows us to check if the mouse was hit along a certain axis. Both if statements see if the mouse was moving towards the cursor in the given direction and then we return True or False depending on if the ball was close along that given axis.


## Cleaning Up

Go ahead and give this a run if you haven't already. Need help? Here is what my file looks like after adding mouse interaction. Before we conclude, there's a few things we need to discuss as you will likely see them in Python code from other developers. First, if I were writing this code for my job, I would have said self._position_x instead of self.position_x. This leading underscore tells other developers not to modify that value directly and to, instead, access it through the methods of class. We say that we are indicating that position_x is a "private" field. Similarly, there are some methods that I would make private as they are only used internally within the object like self._reverse_x instead of self.reverse_x. Why private attributes Some developers think that all fields should be private such that changes to variables on an instance can only happen through public methods (those without a leading underscore). To understand why, let's return to the example of BankAccount. Maybe changes to the balance require other actions like sending the owner a note. Specifically, imagine that we need to inform the owner by text each time money is withdrawn. Of course, we could add that logic to the withdraw method. However, what if a developer using the BankAccount class started doing account.balance = account.balance + 10? That extra logic within the withdraw method wouldn't execute if someone accessed balance directly. In this case, we want to make balance private to ensure developers go through the methods of the class. Many developers typically make things private by default and then decide which select methods should be public. This dictates how code outside the object should interact with each instance. We say that this is defining an "interface" that is used "publicly" outside the object. This ensure all of the actions that need to happen are taken care of as the fields or "state" of the object changes over time. We can do this for our simulation too. What would you make private? Note that this concept is called encapsulation. Second, I want to discuss what """ does. This defines a special kind of comment called a docstring which tells another developer that this is an important comment that defines how to use a file, a class, a function, or a method. Some code editors can also take advantage of these docstrings to help provide contextual information while you program. All of this in mind, please see this final version of our code which is how I would have written it for my job.


## Next Steps

We've reached the end of our first set of skills labs! If you are taking the course with me during the semester, please note that lectures (and recordings) will go back to normal for a bit instead of using the flipped format. So, there won't be a recording sent out ahead of our next class time. If you are doing this on your own time, you can return to the lectures or continue onwards to Skills Lab 4.




## Citations


- C. Swaroop, A Byte of Python. 2024. [Online]. Available: https://python.swaroopch.com

- A. Pottinger, "Sketchingpy." Sketchingpy Project, 2024. [Online]. Available: https://sketchingpy.org/

- A. Sharma, "Docstrings in Python Tutorial." Datacamp, Dec. 20, 2022. [Online]. Available: https://www.datacamp.com/tutorial/docstrings-python

- H. Amit, "Encapsulation in Object-Oriented Programming." Meidum, Nov. 19, 2024. [Online]. Available: https://medium.com/@heyamit10/encapsulation-in-object-oriented-programming-f10ed08c2998

