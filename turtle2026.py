import turtle
import random


screen = turtle.Screen()
screen.bgcolor("black")
screen.title("CodeWeek Plovdiv 2026 - Creative Coding")

t = turtle.Turtle()
t.speed(0)  # Най-бързо рисуване
t.hideturtle()

# Функция за рисуване на една фигура
def draw_shape(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    colors = ["#FF5733", "#33FF57", "#3357FF", "#F33FF5", "#FFFF33"]
    t.color(random.choice(colors))
    
    # спирала
    for i in range(20):
        t.forward(i * 3)
        t.right(45)

#При клик с мишката се извиква функцията
screen.onscreenclick(draw_shape)

turtle.done()

