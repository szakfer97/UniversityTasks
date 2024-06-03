import turtle

rules = {
    "X": "F+[[X]-X]-F[-FX]+X",
    "F": "FF"
}

def apply_rules(input_string):
    output_string = ""
    for char in input_string:
        if char in rules:
            output_string += rules[char]
        else:
            output_string += char
    return output_string

def generate_string(axiom, iterations):
    current_string = axiom
    for _ in range(iterations):
        current_string = apply_rules(current_string)
    return current_string

def draw_L_system(turtle_instance, axiom, iterations, angle, length):
    instructions = generate_string(axiom, iterations)
    stack = []
    for instruction in instructions:
        if instruction == "F":
            turtle_instance.forward(length)
        elif instruction == "+":
            turtle_instance.left(angle)
        elif instruction == "-":
            turtle_instance.right(angle)
        elif instruction == "[":
            stack.append((turtle_instance.pos(), turtle_instance.heading())) 
        elif instruction == "]":
            pos, heading = stack.pop()
            turtle_instance.penup()
            turtle_instance.goto(pos)
            turtle_instance.setheading(heading)
            turtle_instance.pendown()

turtle.setup(width=800, height=600)
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("L-system - Pom")

pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.goto(0, -300) 
pen.setheading(90) 
pen.pendown()

axiom = "X"
iterations = 5 
angle = 25 
length = 5

draw_L_system(pen, axiom, iterations, angle, length)

pen.hideturtle()
screen.mainloop()