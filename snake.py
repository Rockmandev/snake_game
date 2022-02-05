import turtle

def main():
    s=turtle.Screen()
    s.setup(800, 600)
    s.bgcolor("black")
    t = turtle.RawTurtle(s)
    t.shape("square")
    t.penup()
    t.color("grey")
    t.goto(0,0)
    t.stamp()
    
    s.exitonclick()

if __name__=="__main__":
    main()