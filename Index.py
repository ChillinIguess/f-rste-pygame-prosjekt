import pygame
from sys import exit
import os

#Variables for the screen
gameWidth = 1280
gameHeight = 720


#Game variables
playerX = gameWidth/2
playerY = gameHeight/2
playerWidth = 40
playerHeight = 40
playerDistance = 5
size = 40
kanHoppe = False
turnedRight = True
#Gravity and jumping
playerVelocityY = 0
gravity = 0.5
jump_strength = -15
onGround = False
gravityplus = 1
fastFall = 1
groundY = gameHeight
maxFallSpeed = 20
neutralJump = -1
lowJump = -12
#Glidning
playerVelocityX = 0
gliding = 0.5
moving = False

#colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
pygame.init()

'''platform = pygame.rect(10, 100, 10)
pygame.draw.platform'''

#Window variables 
clock = pygame.time.Clock()
window = pygame.display.set_mode((gameWidth, gameHeight))
tileSize = ((gameWidth + gameHeight)/2/10)
'''
def draw_grid():
    for line in range(0, 6):
        pygame.draw.line(window, (255, 255, 255), (0, line * tileSize), (gameWidth, line * tileSize))
        pygame.draw.line(window, (255, 255, 255), (0, line * tileSize, 0), (line * tileSize, gameHeight))

class platform():

    
 

class world():
    def __init__(self, data):
        ground = (white)

        for row in data:
            for tile in row:
                if tile == 1:
                    ground 

worldData = [1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1],

draw_grid()
'''
#Defines player
class Player():
    def __init__(self,x,y,size):
      self.x = x
      self.y = y
      self.size = size
      self.velocity_y = 0
      self.playerRect = pygame.Rect(self.x, self.y, self.size,self.size)
    def playerMove(self):
         self.playerRect = pygame.Rect(self.x, self.y, self.size,self.size)
    def draw(self):
        pygame.draw.rect(window, (green), self.playerRect)
#Defines enemy
class Enemy(Player):
    def __init__(self,x,y,size):
        Player.__init__(self,x,y,size)
player = Player(playerX, playerY, playerWidth)
e = Enemy(111,111,50)




pygame.display.update()




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
             # Jump
       

    # Apply gravity
    
    playerVelocityY += gravity
    player.y += playerVelocityY    
    
   
   
    

    # Collision with ground
    if player.y + playerHeight >= groundY:
        player.y = groundY - playerHeight
        onGround = True
        kanHoppe = True
        playerVelocityY = 0

    window.fill(black)
     
    ''' if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT: 
                player.x += playerDistance
            
            if event.key == pygame.K_a or event.key == pygame.K_LEFT: 
                player.x -= playerDistance'''
                

        
    keys = pygame.key.get_pressed()

    

    #Jumping
    if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
        if kanHoppe == True:
            playerVelocityY = jump_strength 
            onGround = False 
            kanHoppe = False
                
             
    
            
          
          #Faster fall downwards 
    if playerVelocityY > 2 and playerVelocityY < maxFallSpeed:
                playerVelocityY += fastFall

    #Makes the jump hight variable depending on how long you hold jump
    if not (keys[pygame.K_SPACE] or keys[pygame.K_UP]) and playerVelocityY > lowJump:
        if onGround == False:
            if playerVelocityY < neutralJump:
                playerVelocityY = neutralJump

    #Makes sure that there is a max fall speed
    if playerVelocityY > maxFallSpeed:
        playerVelocityY = maxFallSpeed     
    
    
 
    #Left movement
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and player.x - playerDistance >= 0: 
        player.x -= playerDistance
        turnedRight = False
    

    
   
    '''if not (keys[pygame.K_LEFT] or keys[pygame.K_a]):
        if player.x > 0 and player.x < playerDistance:  
            player.x -= playerDistance - neutralSpeed'''
          
               
         
        #Right movement
        
    if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and player.x + playerDistance <= gameWidth - playerWidth:
        player.x += playerDistance
        turnedRight = True



        ''' if player.x <= 5:
            PLAYER_VELOCITY_X += PLAYER_DISTANCE
            player.x += PLAYER_VELOCITY_X'''
        
    

#Variables
    player.playerMove()
    player.draw()
    e.draw()
    pygame.display.update()
    clock.tick(60)
        

       