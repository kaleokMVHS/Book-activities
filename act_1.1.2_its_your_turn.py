from contextlib import redirect_stderr
import turtle as trtl

outline_color = trtl.textinput("Outline color", "Please enter a valid color for the outline.\n")

fill_color = trtl.textinput("Fill Color", "Please enter a valid color for the body of the shape.")

painter = trtl.Turtle()

painter.pendown()
painter.pencolor(outline_color)

painter.fillcolor(fill_color)
painter.begin_fill()

# initial square
for i in range(4):
    painter.forward(100)
    painter.right(90)
painter.end_fill()

painter.penup()

painter.goto(50, 50)

painter.pendown()
painter.begin_fill()

painter.forward(100)
painter.right(90)
painter.forward(100)

painter.penup()

# connect lines to first square
painter.goto(100, 0)
painter.left(135)

painter.pendown()
painter.begin_fill()

painter.forward(70.71)

painter.right(135)
painter.forward(100)
painter.right(45)
painter.forward(70.71)
painter.right(135)
painter.forward(100)

painter.left(90)
painter.forward(100)
painter.right(135)
painter.forward(70.71)
painter.right(45)
painter.forward(100)

painter.end_fill()
painter.pu()

# plant pot
painter.goto(50, 25)
painter.pencolor("black")
painter.pd()
painter.fillcolor("grey")
painter.begin_fill()

painter.forward(50)
painter.left(80)
painter.forward(50)
painter.left(100)
painter.forward(66)
painter.left(100)
painter.forward(50)

painter.end_fill()

wn = trtl.Screen()
wn.mainloop()