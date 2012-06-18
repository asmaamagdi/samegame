#######################
#asmaa.magdi@gmail.com#
#######################


from tkinter import *

from samegame import SameGame

class samegameGui(Frame):
    def __init__(self):
        Frame.__init__( self )
        self.master.title( "Same Game" )
        
        self.master.rowconfigure( 0, weight = 1 )
        self.master.columnconfigure( 0, weight = 1 )
        self.grid( sticky = W+E+N+S )

        self.buttons = []

        r = 10
        c = 10
        x = 3
        self.game = SameGame(r, c, x)

        for i in range(0, r):
            tmpButtons = []
            self.buttons.append(tmpButtons)
            for j in range(0, c):
                #self.tmpFrame = Frame(self.frame, bd=1, relief=SUNKEN)
                #self.tmpFrame.grid(row=i, column=j, sticky=N+E+W+S)
                
                self.buttons[i].append(Button(self, bg = "grey", command = lambda
                                    arg1=i, arg2=j:
                                    self.buttonHandler(arg1, arg2)))
                
                self.buttons[i][j].bind("<Return>", lambda
                                event, arg1=i, arg2 = j :
                                self.buttonHandler_a(event, arg1, arg2))
                
                self.buttons[i][j].grid(row = i, column = j, sticky=N+E+W+S)


        self.display()

            

        self.master.rowconfigure( 1, weight = 1 )
        self.master.columnconfigure( 1, weight = 1 )


    def buttonHandler_a(self, event, i, j):
        self.buttonHandler(i)

    def buttonHandler(self, i, j):
        button = self.buttons[i][j]
        self.game.click(i, j)
        self.display()

    def display(self):
        colors = ["red", "green", "blue"]
        for i in range(0, self.game.r):
            for j in range(0, self.game.c):
                button = self.buttons[i][j]
                c = "grey"
                if self.game.grid[i][j] == -1:
                    pass
                    #button.grid_forget()
                    #button.lower(self)
                    #button.configure(state = 'disabled')
                else:
                    c = colors[self.game.grid[i][j]]

                button.configure(activebackground = c)
                button.configure(bg = c)
                


        


samegameGui().mainloop()
