import turtle

def main():
    s=turtle.Screen()
    s.setup(800, 600)
    s.bgcolor("black")
    t = turtle.RawTurtle(s)
    t.shape("square")
    t.penup()
    t.color("lightgreen")
    s.tracer(0)
    snake=[[0, 0],[20, 0],[40, 0],[60, 0]]
    for snake_pos in snake:
        t.goto(*snake_pos)
        t.stamp()

    
    s.exitonclick()

if __name__=="__main__":
    main()