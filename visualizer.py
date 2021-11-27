import pygame
import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox

class Grid:

    # Colors
    black = (0, 0, 0)
    white = (255, 255, 255)
    green = (0, 255, 0)
    red = (255, 0, 0)
    blue = (0,0,255)
    yellow = (255,255,0)
    purple = (128,0,128)

    # This sets the wdith of the screeen and number of rows and cols in the grid
    width = 800
    window_size = [width, width]

    # This sets the margin between each cell
    margin = 2


    def __init__(self,rows=50,cols=50,percent=0.3,start=[0,0],end=[0,0]):
        self.rows = rows
        self.cols = cols
        self.grid = [ [0]*cols for i in range(rows)]
        self.percent = percent
        self.length = (self.width - rows*self.margin) // self.rows
        self.start = start
        self.end = end
        self.root = Tk()

        # Create interface
        Label(self.root,text="Would you like to build the grid randomly or manually:").grid(row=0, sticky=W)
        randomly = IntVar()
        Checkbutton(self.root, text="Randomly", variable=randomly).grid(row=1, sticky=W)
        manually = IntVar()
        Checkbutton(self.root, text="Manually", variable=manually).grid(row=2, sticky=W)

        Button(self.root, text='Okay', command=self.root.quit).grid(row=3, sticky=W, pady=4)
        mainloop()

        # Assign setup variable based on user input
        self.setup = ''
        if manually.get() < randomly.get():
            self.setup = 'R'
        else:
            self.setup = 'M'

        self.root.withdraw()

        # Assign random nodes if prompted
        for row in range(rows):
            for col in range(cols):
                if self.percent > random.random() and self.setup == 'R':
                    self.grid[row][col] = -1

        # Initialize pygame
        pygame.init()
        
        # Set the size of the screen
        self.screen = pygame.display.set_mode(self.window_size)
        
        # Set title of screen
        pygame.display.set_caption("A* Pathfinding Algorithm")
        self.clock = pygame.time.Clock()


    def draw_grid(self):
        '''
        This function takes a 2D list of nodes and draws the grid in pygame
        '''

        # Set the screen background
        self.screen.fill(self.black)

        # Draw the grid
        for row in range(self.rows):
            for col in range(self.cols):
                color = self.white

                if self.grid[row][col] == -1:
                    color = self.black
                elif self.grid[row][col] == 1:
                    color = self.blue
                elif self.grid[row][col] == 2:
                    color = self.purple
                elif self.grid[row][col] == 3:
                    color = self.green
                elif self.grid[row][col] == 4:
                    color = self.red
                elif self.grid[row][col] == 5:
                    color = self.purple

                pygame.draw.rect(self.screen,
                                color,
                                [(self.margin + self.length) * col + self.margin,
                                (self.margin + self.length) * row + self.margin,
                                self.length,
                                self.length])

            # Limit to 60 frames per second
        self.clock.tick(60)
    
        # Update the screen with what we've drawn.
        pygame.display.flip()


    def initialize_grid(self):

        self.draw_grid()

        instructions = ''
        if self.setup == 'M':
            instructions = ("Left click to add a start and then an end. Once start and end points "
                            "have been specfied, left click to add obstacles. Right click to remove"
                            " start, end, or obstacles. Press spacebar to run algorithm")
        elif self.setup == 'R':
            instructions = ("Left click to add a start and then an end. Right click to remove"
                            " start or end points. Press spacebar to run the algorithm")

        messagebox.showinfo("Instructions",instructions)

        start = False
        end = False
        done = True

        while(done):

            self.draw_grid()

            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    done = False  # Flag that we are done so we exit this loop

                # If user presses the spacebar, the algorithm starts.
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and start != False and end != False:
                        done = False


                # User grid component setup/creation
                if pygame.mouse.get_pressed()[0]:
                    # User clicks the mouse. Get the position
                    pos = pygame.mouse.get_pos()
                    # Change the x/y screen coordinates to grid coordinates
                    col = pos[0] // (self.length + self.margin)
                    row = pos[1] // (self.length + self.margin)

                    # Create start node and add to open list
                    if start == False and self.grid[row][col] == 0:
                        start = True
                        self.grid[row][col] = 1
                        self.start = [row,col]
                    
                    # Create end node
                    elif start == True and end == False and self.grid[row][col] == 0:
                        end = True
                        self.grid[row][col] = 2
                        self.end = [row,col]

                    # Create obstacle nodes
                    elif start == True and end == True and self.setup == 'M' and self.grid[row][col] == 0:
                        self.grid[row][col] = -1

                # User grid component removal/modificatoin
                elif pygame.mouse.get_pressed()[2]:
                    # User clicks the mouse. Get the position
                    pos = pygame.mouse.get_pos()
                    # Change the x/y screen coordinates to grid coordinates
                    col = pos[0] // (self.length + self.margin)
                    row = pos[1] // (self.length + self.margin)

                    # Remove start node and remove from open list
                    if start == True and self.grid[row][col] == 1:
                        start = False
                        self.grid[row][col] = 0

                    # Remove end node
                    elif end == True and self.grid[row][col] == 2:
                        end = False
                        self.grid[row][col] = 0
                    
                    # Remove barrier nodes
                    elif self.grid[row][col] == -1 and self.setup == 'M':
                        self.grid[row][col] = 0

    
    def get_map(self):
        return self.grid


    def mark_open(self, open_list):
        for key in open_list.keys():
            key = key[1:-1]
            pos = key.split(',')
            self.grid[int(pos[0])][int(pos[1])] = 3


    def mark_closed(self, closed_list):
        for key in closed_list.keys():
            key = key[1:-1]
            pos = key.split(',')
            self.grid[int(pos[0])][int(pos[1])] = 4


    def mark_path(self, path):
        print (path)
        for pos in path:
            self.grid[pos[0]][pos[1]] = 5




