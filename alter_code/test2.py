import turtle

wn = turtle.Screen()
wn.bgcolor("light green")
skk = turtle.Turtle()
skk.color("blue")
 
def draw_squares(start, end, step):
    for size in range(start, end, step):
        for _ in range(4):
            skk.fd(size)
            skk.left(90)
            size = size+5

draw_squares(6, 147, 20)

turtle.done()