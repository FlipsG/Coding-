import turtle

# Bildschirm initialisieren
screen = turtle.Screen()
screen.title("Eine Blume mit Turtle")
screen.bgcolor("white")

# Turtle initialisieren
flower = turtle.Turtle()
flower.shape("turtle")
flower.color("red")
flower.speed(0)

# Funktion, um eine Blume zu zeichnen
def draw_flower():
    for _ in range(36):
        flower.forward(100)
        flower.left(170)

# Die Blume zeichnen
flower.speed(10)
draw_flower()

# Warten, bis auf den Bildschirm geklickt wird, um ihn zu schließen
screen.exitonclick()