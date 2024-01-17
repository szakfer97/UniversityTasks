from turtle import *

color('red', 'yellow')
title("Drawing the sun")
begin_fill()
while True:
    forward(250)
    left(220)
    if abs(pos()) < 1:
        break
end_fill()
done()