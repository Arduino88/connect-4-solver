import pygame
from pygame import Color
import random
from queue import Queue

game_state = {
    0: {0: None, 1: None, 2: None, 3: None, 4: None, 5: None},
    1: {0: None, 1: None, 2: None, 3: None, 4: None, 5: None},
    2: {0: None, 1: None, 2: None, 3: None, 4: None, 5: None},
    3: {0: None, 1: None, 2: None, 3: None, 4: None, 5: None},
    4: {0: None, 1: None, 2: None, 3: None, 4: None, 5: None},
    5: {0: None, 1: None, 2: None, 3: None, 4: None, 5: None},
    6: {0: None, 1: None, 2: None, 3: None, 4: None, 5: None}  
}


columns = 7
rows = 6
scale = 100

class Player():
    def __init__(self):
        self.team
        pass
        
    

    class Chip():
        def __init__(self):
            self.column = None
            self.row = None
            
        def place_chip(self, column) -> bool:
            self.color = Color(self.team)
            temp_row = 0
            for row in game_state[column]:
                if row == 0 and game_state[column][temp_row] is not None:
                    print('Column Full!')
                    return False
                
                elif row + 1 >= rows or game_state[column][row+1] is not None:
                    game_state[column][temp_row] = self
                    self.column = column
                    self.row = row
                    return True
                    
                elif game_state[column][row+1] is None:
                    temp_row += 1
                    
                else: 
                    print('error')
                    return False
                
                
        def draw(self, screen):
            pygame.draw.ellipse(screen, self.color, (self.column*scale + 5, self.row*scale + 5, scale - 10, scale-10))
        


def main():

    pygame.init()
    
    player1 = Player()
    player1.team = 'yellow'
    player2 = Player()
    player2.team ='red'

    screen = pygame.display.set_mode((columns * scale, rows * scale))
    screen.fill((100, 100, 100))
             
    running = True
    
    active_player = player1
    # main loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_column = event.__dict__['pos'][0] // scale
                print(mouse_column)
                new_chip = active_player.Chip()
                new_chip.place_chip(mouse_column, 1)
                print(game_state)
                
                

                    
        # clear screen
        pygame.draw.rect(screen,(100, 100, 90), [0, 0 , columns * scale, rows * scale])
        for column in game_state:
            for row in game_state[column]:
                if game_state[column][row] is not None:
                    
                    game_state[column][row].draw(screen)

        
        pygame.display.flip()
        
if __name__=="__main__":
    main()
    
    
    
    
    