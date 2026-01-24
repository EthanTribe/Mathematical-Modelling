import turtle


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
debugMode = False
debugColours = []
for r in [0, 0.5, 1]:
    for b in [0, 0.5, 1]:
        for g in [0, 0.5, 1]:
            debugColours.append((r,b,g))

def GetMap(rules, char):
    if char in rules:
        return rules[char]
    else:
        return char

def GetTree(rules, axiom):
    tree = axiom
    tree = "".join(GetMap(rules,char) for char in tree)
    return tree

def CalculateStep(turtle, tree, dist, angle):
    stack = []

    for char in tree:
        if char == "[":
            stack.append((turtle.heading(), turtle.pos()))
        elif char == "]":
            (h, p) = stack.pop()
            turtle.penup()
            turtle.setheading(h)
            turtle.setpos(p)
            turtle.pendown()
        elif char in alphabet:
            if (debugMode):
                turtle.color(debugColours[alphabet.index(char)])
                #turtle.write(f"   {char}", font=("Arial", 10, "bold"))
            turtle.forward(dist)
        elif char == "+":
            turtle.left(angle)
        elif char == "-":
            turtle.right(angle)

    if (debugMode):
        print(tree)


# The system's variables
systems = [
    {
        "name": "Barnsley Fern",
        "rules": {
            "X": "F+[[X]-X]-F[-FX]+X",
            "F": "FF"
        },
        "axiom": "-X",
        "angle": 25,
        "colour": "olive drab",
        "startPos": ((-100, -450))
    },
    {
        "name": "Sierpinski arrowhead curve",
        "rules": {
            "A": "B-A-B",
            "B": "A+B+A"
        },
        "axiom": "A",
        "angle": 60,
        "colour": "hot pink",
        "startPos": ((0, -400))
    },
    {
        "name": "Christmas Tree",
        "rules": {
            "A": "BBB[++[+D][C][-D]][BA][--[+D][C][-D]]",
            "C": "BB[+D][C][-D]",
            "D": "E[+E][E][-E]"
        },
        "axiom": "A",
        "angle": 45,
        "colour": "olive drab",
        "startPos": ((0, -450))
    }
]

# User input to choose system
for i in range(len(systems)):
    print(str(i + 1) + ". " + systems[i]["name"])

reinput = True
while (reinput):
    reinput = False
    choice = input("\nChoose a Lindenmayer system from the above list: ")

    try:
        choice = int(choice)
    except ValueError:
        print("Invalid input - try again")
        reinput = True

    if (not reinput):
        choice -= 1
        if (choice not in range(len(systems))):
            print("Number not in range - try again")
            reinput = True

system = systems[choice]

# Generate the L-System
print()

tree = system["axiom"]

screen = turtle.Screen()
screen.title(system["name"])
screen.setup(1000, 1000)
screen.bgcolor("azure")
screen.tracer(0, 0)

turtle = turtle.Turtle()
turtle.pensize(2)
turtle.speed("fastest")
turtle.hideturtle()
turtle.color(system["colour"])

def Step():
    global tree

    turtle.clear()
    turtle.penup()
    turtle.goto(system["startPos"])
    turtle.setheading(90)
    turtle.pendown()

    CalculateStep(turtle, tree, 20, system["angle"])
    screen.update()

    tree = GetTree(system["rules"], tree)

def ToggleDebugMode():
    global debugMode
    debugMode = not debugMode
    if (debugMode):
        print("Debug colouring on")
    else:
        turtle.color(system["colour"])
        print("Debug colouring off")

def SaveImage():
    screen.getcanvas().postscript(file=system["name"] + ".ps")
    print("Saved image")

Step()

print("ENTER to advance")
print("D for debug mode")
print("SPACE to save image")

screen.onkey(Step, "Return")
screen.onkey(ToggleDebugMode, "d")
screen.onkey(SaveImage, "space")

screen.listen()
screen.mainloop()