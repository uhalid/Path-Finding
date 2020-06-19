from Node_graph import *
from algoritm.Dijkstra import *
from algoritm.A_start import *
import pygame
import copy
from math import floor
from costanti import *
from buttons import Button
from labels import  Label
from random import randint
import sys

pygame.init()
pygame.display.set_caption(TITLE)
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
DISPLAY.fill(WHITE)
beta = False
ui = True
heuristic = "MANHATTAN"
colors = {"N": BLACK,
        "W": BLACK,
        "S": GREEN,
        "E": RED,
        "P": AQUA,
        "SP": YELLOW

        }



class Grid:
    def  __init__(self):
        self.cell_size = 25
        self.start = (0, 0)
        self.end = (1, 1)
        self.algorunned = False
        self.removewall = False        
        self.start_point_clicked = False
        self.end_point_clicked = False
        self.matrix = []
        self.grid = []
        self.create_grid()
        self.draw_grid()
        self.buttons = []
    
    #calcunte numbers of grid and create a matrix
    def create_grid(self):
        DISPLAY.fill(WHITE)
        print(self.cell_size)
        self.num_collumn = (WIDTH-OFFSET_X)//self.cell_size
        self.num_row = (HEIGHT-OFFSET_Y)//self.cell_size
        self.start = (randint(0, self.num_row-1), randint(0, self.num_collumn-1))
        self.end = (randint(0, self.num_row-1), randint(0, self.num_collumn-1))

        self.grid = [[Node(x, y) for x in range(0, (WIDTH-2*OFFSET_X)//self.cell_size)]
                     for y in range(0, (HEIGHT-OFFSET_Y)//self.cell_size)]
        
        self.grid[self.start[0]][self.start[1]].type = "S"
        self.grid[self.end[0]][self.end[1]].type = "E"

    #taken a cell from the matrix it draws it
    def draw_rect(self, node, is_empty, color):
        pygame.draw.rect(DISPLAY,
                        WHITE,
                        [
                            self.cell_size*node.x + OFFSET_X,
                            self.cell_size*node.y + OFFSET_Y,
                            self.cell_size, self.cell_size
                        ], 0)

        pygame.draw.rect(DISPLAY,
                        color,
                        [
                            self.cell_size*node.x + OFFSET_X,
                            self.cell_size*node.y + OFFSET_Y,
                            self.cell_size, self.cell_size
                        ], is_empty)

    #draw the grid
    def draw_grid(self):
        for row in self.grid:
            for cell in row:
                self.draw_rect(cell, cell.fill(), colors[cell.type])


    #return the x  and y of the cell  clicked
    def cell_clicked(self, mouse_pos):
        return (mouse_pos[0] - OFFSET_X) // self.cell_size, (mouse_pos[1] - OFFSET_Y) // self.cell_size

    # Take a list of nodes and drow them
    def draw_nodes(self, nodes_in_order, type="P", velocity=5):
        lastnode = 0
        for node in nodes_in_order:
            if(lastnode != 0 and type == "SP"):
                self.arrow(lastnode.parent, node.parent)
                pygame.display.update()
                pygame.time.delay(int(1000/velocity))
                # lastnode.x = lastnode.x - 1
                # lastnode.y = lastnode.y - 1
                self.draw_rect(lastnode, lastnode.fill(), colors[type])
            # grid[node.x][node.y].type = "P"
            # print(node)
            node.type = type
            lastnode = node
            self.draw_rect(node, node.fill(), colors[node.type])
            pygame.display.update()
            # print((1000/velocity))
            pygame.time.delay(int(1000/velocity))
        

        if type == "SP":
            self.arrow(nodes_in_order[-1].parent, (nodes_in_order[-1].y, nodes_in_order[-1].x))

        pygame.display.update()
        print("Ended")
    
    def change_startpoint(self, row_column):
        
        self.grid[self.start[0]][self.start[1]
                                 ].type = self.grid[self.start[0]][self.start[1]].previus_type
        self.start = row_column
        self.grid[self.start[0]][self.start[1]].previus_type = self.grid[self.start[0]][self.start[1]].type
        self.grid[self.start[0]][self.start[1]].type = "S"

    def change_endpoint(self, row_column):
        self.grid[self.end[0]][self.end[1]
                                 ].type = self.grid[self.end[0]][self.end[1]].previus_type
        self.end = row_column
        self.grid[self.end[0]][self.end[1]
                                 ].previus_type = self.grid[self.end[0]][self.end[1]].type
        self.grid[self.end[0]][self.end[1]].type = "E"

    #still need to complete it, change color of node each time, gradient
    def fancy_animation(self, node, colorss):
        # current_gradiant = gradiant1
        # while current_gradiant[1] > gradiant2[1]:
        #     try:
        #         current_gradiant = [int(x+y) for x,y  in zip(current_gradiant,dif)]
        #         test(tuple(current_gradiant))
        #         # exit()
        #         pygame.display.update()
        #     except Exception as ex:
        #         template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        #         message = template.format(type(ex).__name__, ex.args)
        #         print(message, tuple(current_gradiant))
        #         exit()
        # current_gradiant[1] = -5
    
        # pygame.time.delay(5000)
        pass

    #check if the click  is inside the grid
    def position_valid(self, x, y):
        if min(x, y) < 0 or x >= self.num_row or y >= self.num_collumn:
            return False
        return  True

    #draw an arrow  that follow the current direction 
    def arrow(self, px, cx):
        dirr = ""
        x = cx[1]
        y = cx[0] 
        if  px[1] < cx[1] and px[0] == cx[0]:
            dirr = "RIGHT"
        elif px[1] > cx[1] and px[0] == cx[0]:
            dirr = "LEFT"
        elif px[1] == cx[1] and px[0] < cx[0]:
            dirr = "DOWN"
        elif px[1] == cx[1] and px[0] > cx[0]:
            dirr = "UP"
        if dirr == "UP" :
            pygame.draw.line(DISPLAY, BLACK,
                            (x*self.cell_size +1 +OFFSET_X, y*self.cell_size+ self.cell_size-1 + OFFSET_Y),
                             (x*self.cell_size + self.cell_size//2+1+ OFFSET_X,  y*self.cell_size + self.cell_size//2 + OFFSET_Y),
                            3)
            pygame.draw.line(DISPLAY, BLACK,

                            (x*self.cell_size + self.cell_size -2+OFFSET_X, y*self.cell_size + self.cell_size -2+OFFSET_Y),
                            (x*self.cell_size + self.cell_size//2 +2+OFFSET_X,  y*self.cell_size + self.cell_size//2 +2+OFFSET_Y),
                            3)
        elif dirr == "DOWN" :
            pygame.draw.line(DISPLAY, BLACK,
                             (x*self.cell_size + 1 + OFFSET_X,
                              y*self.cell_size + 1 + OFFSET_Y),
                             (x*self.cell_size + self.cell_size//2+ OFFSET_X,y*self.cell_size + self.cell_size//2+1+ OFFSET_Y),
                            3)
            pygame.draw.line(DISPLAY, BLACK,
                             (x*self.cell_size + self.cell_size - 3 +
                              OFFSET_X, y*self.cell_size + 1 + OFFSET_Y),
                             (x*self.cell_size + self.cell_size//2 + OFFSET_X,
                              y*self.cell_size + self.cell_size//2 + OFFSET_Y),
                            3)
        elif dirr == "RIGHT" :
            pygame.draw.line(DISPLAY, BLACK,
                             (x*self.cell_size + 1+OFFSET_X, y*self.cell_size + 1 + OFFSET_Y),
                             (x*self.cell_size + self.cell_size//2, y*self.cell_size + self.cell_size//2+ OFFSET_Y),
                            3)
            pygame.draw.line(DISPLAY, BLACK,
                             (x*self.cell_size + OFFSET_X , y*self.cell_size + self.cell_size - 2 + OFFSET_Y),
                             (x*self.cell_size + self.cell_size//2 +OFFSET_X , y *
                              self.cell_size + self.cell_size//2 + OFFSET_Y),
                             3)
        elif dirr == "LEFT":
            pygame.draw.line(DISPLAY, BLACK,
                             (x*self.cell_size + self.cell_size -2+OFFSET_X,
                              y*self.cell_size + self.cell_size -3+OFFSET_Y),
                             (x*self.cell_size + self.cell_size//2 + OFFSET_X,
                              y*self.cell_size + self.cell_size//2 + OFFSET_Y),
                             3)
            pygame.draw.line(DISPLAY, BLACK,
                             (x*self.cell_size + self.cell_size-1 +
                              OFFSET_X, y*self.cell_size+1+OFFSET_Y),
                             (x*self.cell_size + self.cell_size//2+OFFSET_X,
                              y*self.cell_size + self.cell_size//2+OFFSET_Y),
                             3)

    def draw_shortest_path(self, distance, nodes_in_order, matrix, sn, en):
        self.draw_nodes(nodes_in_order, velocity=200)
        if(distance == INF):
            print("--------- NON RAGGIUNGIBILE ----------------")
            return

        print(distance)
        shortest_path = trace_back(
            matrix,  matrix[self.start[0]][self.start[1]], matrix[self.end[0]][self.end[1]])
        self.algorunned = True
        self.draw_nodes(shortest_path, "SP", 50)

    def handle_astar(self):
        self.draw_grid()

        distance, nodes_in_order, matrix, sn, en = astar(self.num_collumn, self.num_row, self.grid,
                                                         self.grid[self.start[0]][self.start[1]], self.grid[self.end[0]][self.end[1]], heuristic)
    
        self.draw_shortest_path(
            distance, nodes_in_order, matrix, sn, en)
    

    def handle_dijkstra(self):
        self.draw_grid()
        distance, nodes_in_order, matrix, sn, en = dijkstra(self.num_collumn, self.num_row, self.grid,
                                                    self.grid[self.start[0]][self.start[1]], self.grid[self.end[0]][self.end[1]])
        
        self.draw_shortest_path(
            distance, nodes_in_order, matrix, sn, en)

    #draw button, labels  ecc
    def draw_ui(self):
        self.buttons = []
        astar_button = Button(0, 3, 40, 100, DISPLAY, WHITE,
                      (150, 150, 150), "RUN A*", self.handle_astar, 25)
        dijkstra_button = Button(WIDTH-153, 3, 40, 150, DISPLAY, WHITE,
                      (150, 150, 150), "RUN DIJKSTRA", self.handle_dijkstra, 25)

        # self.buttons.append(astar_button, dijkstra_button)
        self.buttons.extend((astar_button, dijkstra_button))
        for button in self.buttons:
            button.create()
    
    #check if some button has been pressed
    def handle_ui(self, pos):
        for button in self.buttons:
            if button.isOver(pos):
                button.function()
def main():
    dddd = Grid()

    if ui:
        dddd.draw_ui()
    while True:
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                if __debug__ == True:
                    for row in dddd.grid:
                        for cell in row:
                            print("#" if  cell.type != "N" else ".", end = " ")
                        print()
                    
            elif event.type == pygame.MOUSEBUTTONDOWN:
                left, middle, right = pygame.mouse.get_pressed()
                
                if event.button == 4:
                    if beta:
                        dddd.cell_size += 5
                    
                    elif dddd.cell_size == 50:
                        pass
                    elif dddd.cell_size == 20:
                        dddd.cell_size = 25
                    elif dddd.cell_size == 25:
                        dddd.cell_size = 35
                                            
                    elif dddd.cell_size == 35:
                        dddd.cell_size = 50
                    dddd.create_grid()
                    dddd.draw_grid()
                    if ui:
                        dddd.draw_ui()
                    continue

                elif event.button == 5:
                    if beta:
                        if dddd.cell_size - 5 > 0:
                            dddd.cell_size -= 5
                    elif(dddd.cell_size == 10):
                        continue
                    elif dddd.cell_size == 50:
                        dddd.cell_size = 35  
                        continue
                    elif dddd.cell_size == 35:
                        dddd.cell_size = 25
                        continue
                    elif dddd.cell_size == 25:
                        dddd.cell_size = 20    
                        continue
                    dddd.create_grid()
                    
                    dddd.draw_grid()
                    
                    if ui:
                        dddd.draw_ui()

                    continue

                
                if right:
                    dddd.removewall = True

                
                mouse_pos = pygame.mouse.get_pos()
                if ui:
                    print(event.button)
                    dddd.handle_ui(mouse_pos)
                # if(test.isOver(mouse_pos)):
                #     test.funciont()
                #     continue

                column, row = dddd.cell_clicked(mouse_pos)
                # print(row, column, dddd.cell_size)

                if not dddd.position_valid(row, column):
                    continue
                
                if (row, column) == dddd.start:
                    dddd.start_point_clicked = True
                elif (row, column) == dddd.end:
                    dddd.end_point_clicked = True
                else:
                    if  dddd.removewall:
                        dddd.grid[row][column].type = 'N'
                    else:
                        dddd.grid[row][column].type = 'W'
                
                
                dddd.draw_grid()

            elif event.type == pygame.MOUSEMOTION:
                
                left, middle, right = pygame.mouse.get_pressed()
                
                if not left and not right: 
                    continue

                if right:
                    dddd.removewall = True

                mouse_pos = pygame.mouse.get_pos()
                column, row = dddd.cell_clicked(mouse_pos)
                if not dddd.position_valid(row, column):
                    continue
                
                if(dddd.start_point_clicked):
                    dddd.change_startpoint((row,column))
    
                elif(dddd.end_point_clicked):
                    dddd.change_endpoint((row,column))

                    # if(dddd.algorunned):
                    #     shortest_path = trace_back(
                    #         matrix,  matrix[dddd.start[0]][dddd.start[1]], matrix[dddd.end[0]][dddd.end[1]])
                    #     dddd.draw_nodes(shortest_path, "SP", 100)
                elif (row, column) == dddd.start:
                    pass
                elif (row, column) == dddd.end:
                    pass
                else:
                    type = "W"
                    if dddd.removewall:
                        type = "N"
                    dddd.grid[row][column].type = type


                dddd.draw_grid()
            elif event.type == pygame.MOUSEBUTTONUP:
                dddd.start_point_clicked = dddd.end_point_clicked = dddd.removewall = False
            
            elif event.type == pygame.KEYDOWN:
                pressed = pygame.key.get_pressed()

                if pressed[pygame.K_a]:
                    dddd.handle_astar()

            
                elif pressed[pygame.K_d]:
                    dddd.handle_dijkstra()

            elif event.type == pygame.KEYUP:
                dddd.removewall = False
        
        

        
        pygame.display.update()

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        if "--no-ui" in sys.argv:
            ui = False
            OFFSET_Y = 0
        if "--beta" in sys.argv:
            beta = True
        if "--euclidean" in sys.argv:
            heuristic = "EUCLIDEAN"
    main()
# pygame.quit()
