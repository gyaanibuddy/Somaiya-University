# ---------------------------------------------------------------------------------- 

# This is the BreakOut game created in python using pygame 
# it works perfectly fine  and it contains easy code which is easy to understand.....
# i hope you like it and enjoy the game and learning....
# :)

# ---------------------------------------------------------------------------------- 

# requirement : install python
#             : intall pygame module  

# ---------------------------------------------------------------------------------- 




import pygame
from pygame.locals import *
from pygame import mixer
import random


pygame.init()

screen_width = 600
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("BreakOut")

# tile colors 
bg = (80, 80, 80)
red = (242, 70, 75)
green = (86, 194, 87)
blue = (69, 177, 232)
yellow = (255,188,19)

#paddle colors
paddle_col = (229,255,110)
paddle_outline = (255, 250, 125)

# text color 
text_col = (255, 255, 255)

# global game variables
columns = 6
rows = 6
clock = pygame.time.Clock()
fps = 100
live_ball = False
game_over = 0


# generate random positions for yellow tile...
rand_block1 = round(random.randrange(7, 37)) 
rand_block2 = round(random.randrange(7, 37)) 
if rand_block1 == rand_block2:
    rand_block2 = round(random.randrange(7, 37)) 


# define font
font = pygame.font.SysFont("Consolas", 30, bold=True)

# text on the screen
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


# brick wall class
class wall():
    def __init__(self):
        self.width = screen_width // columns
        self.height = 50

    def create_wall(self):
        self.blocks = []
        # define an empty list for individual blocks
        block_individual = []
        tag = 0
        for row in range(rows):
            block_row = []
            # iterate through each columns in that row...
            for col in range(columns):
                # generate x and y position for each blocks and rectangle for that...
                block_x = col * self.width
                block_y = row * self.height
                rect = pygame.Rect(block_x, block_y, self.width, self.height)

                #assign block strength based on rows
                if row < 2:
                    strength = 3
                    tag += 1
                elif row < 4:
                    strength = 2
                    tag += 1
                elif row < 6:
                    strength = 1
                    tag += 1

                #create a list at this point to store rect and color data
                block_individual = [rect, strength, tag]
                # append that individual block to block_row
                block_row.append(block_individual)
            
            # append the row to the full list of blocks
            self.blocks.append(block_row)

    def draw_wall(self):
        for row in self.blocks:  # gives each row
            for block in row:    # gives each block
                # assign color based on block strength
                
                if block[1] == 3:
                    block_col = blue
                    if block[2] == rand_block1 or block[2] == rand_block2:
                        block_col = yellow
                elif block[1] == 2:
                    block_col = green
                    if block[2] == rand_block1 or block[2] == rand_block2:
                        block_col = yellow
                elif block[1] == 1:
                    block_col = red
                    if block[2] == rand_block1 or block[2] == rand_block2:
                        block_col = yellow
                


                pygame.draw.rect(screen, block_col, block[0])
                pygame.draw.rect(screen, bg, block[0], 2 )


# paddle class
class paddle():
    def __init__(self):
        self.reset()
    
    def move(self):
        # reset movement direction
        self.direction = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
            
        if key[pygame.K_RIGHT] and self.rect.right < screen_width:
            self.rect.x += self.speed
            self.direction = 1
        
    def draw(self):
        pygame.draw.rect(screen, paddle_col, self.rect)
        pygame.draw.rect(screen, paddle_outline, self.rect, 3)
    
    def reset(self):
        self.height = 20
        self.width = int(screen_width/columns)
        self.x = int((screen_width/2) - (self.width/2))
        self.y = screen_height - (self.height*2)
        self.speed = 10
        self.rect = Rect(self.x, self.y, self.width, self.height)
        self.direction = 0


# ball class
class game_ball():
    def __init__(self, x, y):
        self.reset(x, y)
        

    def move(self):
        # collision threshold 
        collision_thresh = 5
         
        # start off with the assumption that the wall has been destroyed completely
        wall_destroyed = 1
        row_count = 0
        for row in wall.blocks:
            item_count = 0
            for item in row:
                # check collision 
                # item[0] : rect present in the individual_block[]
                if self.rect.colliderect(item[0]):  
                    # check if the collision was from above 
                    if abs(self.rect.bottom - item[0].top) < collision_thresh and self.speed_y > 0:
                        self.speed_y *= -1
                        mixer.music.load("E:/Python Pygame/BreakOut/resources/move.mp3")
                        mixer.music.play()  

                    # check if the collision was from below
                    if abs(self.rect.top - item[0].bottom) < collision_thresh and self.speed_y < 0:
                        self.speed_y *= -1
                        mixer.music.load("E:/Python Pygame/BreakOut/resources/move.mp3")
                        mixer.music.play()  

                    # check if the collision was from left
                    if abs(self.rect.right - item[0].left) < collision_thresh and self.speed_x > 0:
                        self.speed_x *= -1
                        mixer.music.load("E:/Python Pygame/BreakOut/resources/move.mp3")
                        mixer.music.play()  

                    # check if the collision was from right
                    if abs(self.rect.left - item[0].right) < collision_thresh and self.speed_x < 0:
                        self.speed_x *= -1
                        mixer.music.load("E:/Python Pygame/BreakOut/resources/move.mp3")
                        mixer.music.play()  
                    
                    # reduce the block's strength by doing damage to it
                    if wall.blocks[row_count][item_count][1] > 1:
                        wall.blocks[row_count][item_count][1] -= 1
                    else:
                        wall.blocks[row_count][item_count][0] = (0,0,0,0)
                    

                    if wall.blocks[row_count][item_count][2] == rand_block1 or wall.blocks[row_count][item_count][2] == rand_block2 :  
                                     
                        # # for deleting the entire row...
                        # wall.blocks[4][item_count][0] = (0,0,0,0)
                        # wall.blocks[4][item_count+1][0] = (0,0,0,0)
                        # wall.blocks[4][item_count-1][0] = (0,0,0,0)
                        # wall.blocks[4][item_count-2][0] = (0,0,0,0)
                        # wall.blocks[4][item_count-3][0] = (0,0,0,0)
                        # wall.blocks[4][item_count-4][0] = (0,0,0,0)
                        
                        wall.blocks[0][item_count][0] = (0,0,0,0)
                        wall.blocks[1][item_count][0] = (0,0,0,0)
                        wall.blocks[2][item_count][0] = (0,0,0,0)
                        wall.blocks[3][item_count][0] = (0,0,0,0)
                        wall.blocks[4][item_count][0] = (0,0,0,0)


                # check if blocks still exists, in which case the wall is not destroyed
                if wall.blocks[row_count][item_count][0] != (0,0,0,0):
                    wall_destroyed = 0
                
                #increase the item counter
                item_count += 1
            # increase the row counter
            row_count += 1
        # after iterating through all the blocks, check if the wall is destroyed
        if wall_destroyed == 1:
            self.game_over = 1

        #check for collision with walls
        if self.rect.left < 0 or self.rect.right > screen_width:
            self.speed_x *= -1    # after collision ball moves in opposite direction...
            mixer.music.load("E:/Python Pygame/BreakOut/resources/move.mp3")
            mixer.music.play()
        
        # check for collision with top and bottom of the screen
        if self.rect.top < 0:
            self.speed_y *= -1    # after collision ball moves in opposite direction...
            mixer.music.load("E:/Python Pygame/BreakOut/resources/move.mp3")
            mixer.music.play()

        if self.rect.bottom > screen_height:
            self.game_over = -1
            mixer.music.load("E:/Python Pygame/BreakOut/resources/gameover.mp3")
            mixer.music.play()

        # look for collision with paddle
        if self.rect.colliderect(player_paddle):
            # check if colliding from the top
            if abs(self.rect.bottom - player_paddle.rect.top) < collision_thresh and self.speed_y > 0:
                self.speed_y *= -1
                self.speed_x += player_paddle.direction
                mixer.music.load("E:/Python Pygame/BreakOut/resources/move.mp3")
                mixer.music.play()

                if self.speed_x > self.speed_max:
                    self.speed_x = self.speed_max
                elif self.speed_x < 0 and self.speed_x <-self.speed_max:
                    self.speed_x = -self.speed_max

            # if collision is from any other surface of the paddle then
            # ball moves in opposite x direction...        
            else:
                mixer.music.load("E:/Python Pygame/BreakOut/resources/move.mp3")
                mixer.music.play()
                self.speed_x *= -1

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
    
        return self.game_over        


    def draw(self):
        pygame.draw.circle(screen, paddle_col, (self.rect.x + self.ball_rad, self.rect.y + self.ball_rad), self.ball_rad)
        pygame.draw.circle(screen, paddle_outline, (self.rect.x + self.ball_rad, self.rect.y + self.ball_rad), self.ball_rad, 3) 
    
    def reset(self, x, y):
        self.ball_rad = 10
        self.x = x - self.ball_rad
        self.y = y
        self.rect = Rect(self.x, self.y, self.ball_rad * 2, self.ball_rad * 2)
        self.speed_x = 4
        self.speed_y = -4
        self.speed_max = 5
        self.game_over = 0




# create a wall
wall = wall()
wall.create_wall()

#create a paddle
player_paddle = paddle()

#create ball
ball = game_ball(player_paddle.x + (player_paddle.width//2), player_paddle.y - player_paddle.height)


run = True 

while run:
    clock.tick(fps)
    screen.fill(bg)

    # draw all objects 
    wall.draw_wall()
    player_paddle.draw()
    ball.draw()

    if live_ball:
        player_paddle.move()
        game_over = ball.move()
        if game_over != 0:
            live_ball = False
        
    if not live_ball:
        if game_over == 0:
            draw_text("CLICK ENTER TO START", font, text_col, 135, screen_height//2 + 100)
            
        elif game_over == 1:
            draw_text("YOU WON!", font, text_col, 240, screen_height//2 + 50)
            draw_text("CLICK ENTER TO START AGAIN", font, text_col, 80, screen_height//2 + 100)

        elif game_over == -1:
            draw_text("YOU LOST", font, text_col, 240, screen_height//2 + 50)
            draw_text("CLICK ENTER TO START", font, text_col, 135, screen_height//2 + 100)


    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if not live_ball:    
                    live_ball = True
                    ball.reset(player_paddle.x + (player_paddle.width // 2), player_paddle.y - player_paddle.height)
                    player_paddle.reset()
                    wall.create_wall()
                    # for choosing the random block.....
                    rand_block1 = round(random.randrange(7, 37)) 
                    rand_block2 = round(random.randrange(7, 37)) 
                    if rand_block1 == rand_block2:
                        rand_block2 = round(random.randrange(7, 37)) 


    pygame.display.update()

pygame.quit()


