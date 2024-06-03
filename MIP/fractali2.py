import turtle

axiom = "F+F+F+F"
rules = {
    "F": "FF+F+F+F+F+F-F"
}
angle = 90
iterations = 4
length = 5

def apply_rules(axiom):
    result = ""
    for char in axiom:
        result += rules.get(char, char)
    return result

def generate_l_system(axiom, iterations):
    for _ in range(iterations):
        axiom = apply_rules(axiom)
    return axiom

def draw_l_system(turtle, instructions, length, angle):
    stack = []
    for command in instructions:
        if command == "F":
            turtle.forward(length)
        elif command == "+":
            turtle.right(angle)
        elif command == "-":
            turtle.left(angle)
        elif command == "[":
            position = turtle.position()
            heading = turtle.heading()
            stack.append((position, heading))
        elif command == "]":
            position, heading = stack.pop()
            turtle.penup()
            turtle.goto(position)
            turtle.setheading(heading)
            turtle.pendown()

def main():
    turtle.speed(0)
    turtle.hideturtle()
    turtle.tracer(0, 0) 

    l_system = generate_l_system(axiom, iterations)

    turtle.penup()
    turtle.goto(-200, 200) 
    turtle.pendown()

    draw_l_system(turtle, l_system, length, angle)

    turtle.update()
    turtle.done()

if __name__ == "__main__":
    main()
