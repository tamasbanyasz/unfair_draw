import turtle

'''
author:         Bányász Tamás
since:          2024.05.17
version:        1.0
created_to:     Dr.Faragó Csaba
product_name:   unfair_draw

'''

"""

#DESCRIBE:

                    ***********************************
                    ***** WARNING! SPOILER ALERT! *****
                    *********************************** 
    
    
At the beginning in this code the program write a name (TOMI) on the surface. After it finished then we get a message 
to click to exit...but it's a scam. If you click the '>here<' text you will be getting a new fake message.


"""


class DrawTOMI:
    def __init__(self, turtle):
        self.turtle = turtle
        self.screen = self.turtle.Screen()
        self.screen.register_shape('image_01.gif')


        self.turtle.hideturtle()
        self.turtle.pensize(20)
        self.turtle.color("green")

    def draw_letter_t(self):
        self.turtle.penup()
        self.turtle.goto(-200, 0)
        self.turtle.pendown()

        self.turtle.forward(120)
        self.turtle.backward(55)
        self.turtle.right(90)
        self.turtle.forward(120)

    def draw_letter_o(self):
        self.turtle.penup()
        self.turtle.setpos(-100, -70)
        self.turtle.pendown()

        self.turtle.circle(50)
        self.turtle.forward(1)

    def draw_letter_m(self):
        self.turtle.penup()
        self.turtle.setpos(30, 0)
        self.turtle.pendown()
        self.turtle.setheading(0)

        self.turtle.right(90)
        self.turtle.forward(120)
        self.turtle.backward(120)

        self.turtle.left(45)
        self.turtle.forward(90)

        self.turtle.left(95)
        self.turtle.forward(90)

        self.turtle.right(140)
        self.turtle.forward(120)

    def draw_letter_i(self):
        self.turtle.penup()
        self.turtle.setpos(190, 0)
        self.turtle.pendown()
        self.turtle.setheading(0)
        self.turtle.right(90)
        self.turtle.forward(115)

    def draw_first_click_to_extit_message(self):
        self.turtle.penup()
        self.turtle.goto(220, -120)

        self.turtle.color("black")
        self.turtle.write("Click >here< to exit.", move=True, font=("Verdana", 15, "normal"))



    def exit_phase(self):
        self.turtle.undo()
        self.turtle.goto(-190, 180)
        self.turtle.write("OKAY! Time to exit. Press 'Up' button \U0001f600", move=True, font=("Verdana", 15, "normal"))



        gif = turtle.Turtle()


        def up():
            gif.setheading(90)
            gif.forward(10)

        gif.penup()
        gif.color("white")
        gif.goto(-40, -700)
        gif.shape('image_01.gif')

        self.screen.onkeypress(up, 'Up')
        #self.turtle.exitonclick()
        self.screen.listen()


    def hit_the_second_clickable_surface(self, c, v):

        if (125.0 < c < 203.0) and (212.0 > v > 140):
            self.turtle.onscreenclick(None)
            self.turtle.undo()

            self.exit_phase()



    def hit_the_first_clickable_surface(self,x, y):

        if (270.0 < x < 354.0) and (-130.0 < y < -93.0):
            self.turtle.onscreenclick(None)
            self.turtle.undo()
            self.turtle.goto(x - 300, y + 300)
            self.turtle.write("Nope. Click >here< to exit. \U0001f600", move=True, font=("Verdana", 15, "normal"))

            self.turtle.onscreenclick(self.hit_the_second_clickable_surface)

    def click(self):
        self.turtle.onscreenclick(self.hit_the_first_clickable_surface)




    def run(self):

        self.draw_letter_t()
        self.draw_letter_o()
        self.draw_letter_m()
        self.draw_letter_i()

        self.draw_first_click_to_extit_message()

        self.click()

        self.turtle.mainloop()

if __name__ == '__main__':
    DrawTOMI(turtle).run()


