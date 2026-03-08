# Lindenmayer Systems
A Lindenmayer system (or L-System for short) is a set of recursive rules to form a branching sequence iteratively.
They are typically used to model plant growth or generate other fractals.

To program this I have implimentend the recursion in Python and used a turtle to draw out the configured system.

In a system's rules the letters represent segments, + and - represent turning left or right respectively, and square brackets mean the enclosed section is a subset.

## Using the Script *Lindenmayer System.py*
When the script is run it will prompt the user to chose an L-System from the given list. Once the system is selected, a graphics window will appear and command options printed to the terminal.

The options are as follows:
* Advance one step on the system,
* Save the image as a .ps file (the only option supported by the turtle library annoyingly, so screenshots are recommended),
* Enter debug mode.

Debug mode will make the following image display differnt variables as different colours on the screen, as well as printing the current sequence to the terminal.

When you want to close the program, simply close the graphics window.

## Barnsley Fern
This fractal has two variables variables X and F. Turns have an angle of 25°.

The rules are:
* X -> F+[[X]-X]-F[-FX]+X
* F -> FF

The system's initial sequence is "-X".

<img src="Barnsley%20Fern.png" width="500"/>

## Sierpinski Arrowhead Curve
This system approximates the famous Sierpinski Triangle fractal - a collection of triangles within triangles.

This fractal has two variables variables A and B. Turns have an angle of 60° this time.

The rules are:
* A -> B-A-B
* B -> A+B+A

The system's initial sequence is "A".

For a more refined system I swapped the rules so that two steps are done at once, otherwise the curve is mirrored each iteration. The length of lines that the turtle drew also had to changed dynamically to keep this system on the screen.

<img src="Sierpinski%20Arrowhead%20Curve.png" width="500"/>

## Christmas Tree
This is a system I came up with. I wanted to build a tree that grew outwards in horizontal branches as well as upwards. The result is the perfect looking Christmas tree shape.

This fractal has four variables variables A, B, C, and D. Turns have an angle of 45°.

The rules are:
* A -> BBB[++[+D][C][-D]][BA][--[+D][C][-D]]
* C -> BB[+D][C][-D]
* D -> B[+B][B][-B]

Notice that there is not a rule for B, this variable stays constant and does not decay into anything.

The system's initial sequence is "A".

<img src="Christmas%20Tree.png" width="500"/>
