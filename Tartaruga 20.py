from turtle import *
def main():
    colors = ("magenta4","Violetred1", "purple4", "orange","MediumOrchid2","maroon2", "orchid4")

    up()
    goto(-300,-180)
    width(50)

    for pcolor in colors:
        color(pcolor)
        down()
        forward(600)
        up()
        backward(600)
        left(90)
        forward(66)
        right(90)

main()
mainloop()