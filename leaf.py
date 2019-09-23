import turtle

def draw_branch(branch_size,branch_length):
    if branch_length > 5:
        turtle.pensize(branch_size)
        if branch_length<20:
            turtle.pencolor('green')
        else:
            turtle.pencolor('black')
        turtle.forward(branch_length)
        turtle.right(20)
        draw_branch(branch_size - 2,branch_length - 10)
        turtle.left(40)
        draw_branch(branch_size - 2, branch_length - 10)
        turtle.right(20)
        turtle.pu()
        turtle.backward(branch_length)
        turtle.pd()

def main():
    turtle.left(90)
    turtle.pu()
    turtle.backward(100)
    turtle.pd()
    draw_branch(10,60)
    turtle.exitonclick()

if __name__ == '__main__':
    main()
