import turtle

rules = {
    "F": "F+F-F-F+F",
    "+": "+",
    "-": "-"
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
    for instruction in instructions:
        if instruction == "F":
            turtle_instance.forward(length)
        elif instruction == "+":
            turtle_instance.left(angle)
        elif instruction == "-":
            turtle_instance.right(angle)

turtle.setup(width=800, height=600)
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("L-system")

pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.goto(-500, -300)
pen.pendown()

axiom = "F"
iterations = 5
angle = 90
length = 5

draw_L_system(pen, axiom, iterations, angle, length)

pen.hideturtle()
screen.mainloop()