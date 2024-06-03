import turtle

def createLSystem(numIters, axiom):
    startString = axiom
    endString = ""
    for i in range(numIters):
        endString = processString(startString)
        startString = endString
    return endString

def processString(oldStr):
    newstr = ""
    for ch in oldStr:
        newstr = newstr + applyRules(ch)
    return newstr

def applyRules(ch):
    newstr = ""
    if ch == 'F':
        newstr = 'FF-F+F-F-FF'
    else:
        newstr = ch
    return newstr

def drawLsystem(aTurtle, instructions, angle, distance):
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == 'B':
            aTurtle.backward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)

def main():
    inst = createLSystem(5, "F")
    print(inst)
    t = turtle.Turtle()
    wn = turtle.Screen()

    wn.setup(width=1200, height=800)
    t.up()
    t.goto(-300, 0)
    t.down()
    t.speed(0)
    drawLsystem(t, inst, 90, 5)
    wn.exitonclick()

main()
