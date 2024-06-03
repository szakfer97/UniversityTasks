import turtle

def apply_rules(letter):
    """Aplică reguli pentru o literă individuală și returnează rezultatul."""
    if letter == 'F':
        new_string = 'F-F++F-F'
    else:
        new_string = letter
    
    return new_string

def process_string(original_string):
    """Aplică reguli unui șir, literă cu literă, și returnează rezultatul."""
    tranformed_string = ""
    for letter in original_string:
        tranformed_string = tranformed_string + apply_rules(letter)
    
    return tranformed_string

def create_l_system(number_of_iterations, axiom):
    """Începe cu un axioma și aplică regulile șirului original axiom de number_of_iterations ori, apoi returnează rezultatul."""
    start_string = axiom
    for counter in range(number_of_iterations):
        end_string = process_string(start_string)
        start_string = end_string
    
    return end_string

def draw_l_system(some_turtle, instructions, angle, distance):
    """Desenează cu some_turtle, interpretând fiecare literă din instrucțiunile transmise."""
    for task in instructions:
        if task == 'F':
            some_turtle.forward(distance)
        elif task == 'B':
            some_turtle.backward(distance)
        elif task == '+':
            some_turtle.right(angle)
        elif task == '-':
            some_turtle.left(angle)

instruction_string = create_l_system(4, "F")
print(instruction_string)

window = turtle.Screen()
jill = turtle.Turtle()
jill.speed(0)
jill.up()
jill.back(200)
jill.down()

draw_l_system(jill, instruction_string, 60, 5)
window.mainloop()