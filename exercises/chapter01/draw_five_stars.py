import turtle as t


def draw_five_stars(len):

    count = 1
    while count <= 5:

        t.forward(len)
        t.right(144)
        count += 1

    len += 10

    # if len <= 100:

    #     draw_five_stars(len)

def main():

    t.penup()
    t.backward(100)
    t.pendown()
    t.pensize(2)
    t.pencolor('red')
    segment = 50
    draw_five_stars(segment)
    t.exitonclick()


if __name__ == '__main__':

    main()