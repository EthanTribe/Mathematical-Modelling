import turtle


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
debugMode = False
colours = []
for r in [0, 0.5, 1]:
    for b in [0, 0.5, 1]:
        for g in [0, 0.5, 1]:
            colours.append((r,b,g))

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
                turtle.color(colours[alphabet.index(char)])
                turtle.write(f"   {char}", font=("Arial", 10, "bold"))
            turtle.forward(dist)
        elif char == "+":
            turtle.left(angle)
        elif char == "-":
            turtle.right(angle)

    if (debugMode):
        print(tree)


# The system's variables
name = "Barnsley Fern"
rules = {
    "X": "F+[[X]-X]-F[-FX]+X",
    "F": "FF"
}
axiom = "-X"
angle = 25
colour = "olive drab"
startPos = ((-100, -450))


# Generate the L-System

print()

tree = axiom

screen = turtle.Screen()
screen.title(name)
screen.setup(1000, 1000)
screen.bgcolor("azure")
screen.tracer(0, 0)

turtle = turtle.Turtle()
turtle.pensize(2)
turtle.speed("fastest")
turtle.hideturtle()
turtle.color(colour)

def Step():
    global tree

    turtle.clear()
    turtle.penup()
    turtle.goto(startPos)
    turtle.setheading(90)
    turtle.pendown()

    CalculateStep(turtle, tree, 10, angle)
    screen.update()

    tree = GetTree(rules, tree)

def ToggleDebugMode():
    global debugMode
    debugMode = not debugMode
    if (debugMode):
        print("Debug colouring on")
    else:
        turtle.color(colour)
        print("Debug colouring off")

def SaveImage():
    screen.getcanvas().postscript(file=f"{name}.ps")
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