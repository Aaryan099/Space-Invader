
import pygame
import random 
import math



pygame.init()
screen = pygame.display.set_mode((720,1600))
background = pygame.image.load('galaxy.png')
bulletImg = pygame.image.load('bullet.png')
bulletImg = pygame.transform.scale(bulletImg,(50,50))
bulletImg2 = pygame.transform.scale(bulletImg,(50,50))
# Title And Icon
pygame.display.set_caption('My Game')
# icon = pygame.image.load('')
#  pygame.display.set_icon()



# Player
playerImg= pygame.image.load('player.png')
playerImg = pygame.transform.scale(playerImg,(150,150))
enemyImg = pygame.image.load('monster.png')
enemyImg = pygame.transform.scale(enemyImg,(100,100))


# Variables
change = 0
x=300
y= 1000

enemy_x = random.randint(0,620)
enemy_y = random.randint(10,150)
enemy_x_change = 5
enemy_y_change = 60

white = ((255,255,255))
brown = ((130,60,60))
black = ((0,0,0))
blue = ((0,0,50))


# Bullet
bullet_x =0
bullet_y=1000
bullet_x_change= 0
bullet_y_change = 20
bullet_state = "ready"

# Score
score= 0



def enemy():
	screen.blit(enemyImg,(enemy_x,enemy_y))

def player(a,b):
	screen.blit(playerImg,(a,b))



def button():
	pygame.draw.rect(screen,blue,(0,1250,720,200))
	pygame.draw.rect(screen,brown,(0,1450,720,10))
	pygame.draw.circle(screen,white,(130,1350),70)
	pygame.draw.circle(screen,white,(590,1350),70)
	pygame.draw.rect(screen,brown,(0,1250,10,200))
	pygame.draw.circle(screen,white,(365,1350),70)
	

def bullet(a,b,):
	global bullet_state 
	bullet_state = "fire"
	screen.blit(bulletImg,(a+50,b+70))
	
	
def collision(enemy_x,enemy_y,bullet_x,bullet_y):
    distance = math.sqrt(math.pow(enemy_x-bullet_x,2))+(math.pow(enemy_y-bullet_y))
    
    if distance <27:
        return True
    else :
        return False
	
	
run = True
while run:
	#Red , Blue , Green			
	screen.fill((0,0,0))
	screen.blit(background,(0,0))
	
	
	#Quit 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
			
		if event.type == pygame.MOUSEBUTTONDOWN:
			if pygame.mouse.get_pos() >= (60,1280):
				if pygame.mouse.get_pos() <=(200,1420):
					change = -10
					
			if pygame.mouse.get_pos() >= (520,1280):
					if pygame.mouse.get_pos() <= (660,1420):
						change = +10
			if pygame.mouse.get_pos() >=(295,1280):
		 		if pygame.mouse.get_pos() <=(405,1420):
		 		    if bullet_state is "ready":
		 		        bullet_x =x
		 		        bullet(bullet_x,bullet_y)
			
                    	
						
		if event.type == pygame.MOUSEBUTTONUP:
			if pygame.mouse.get_pos() >= (60,1280):
				if pygame.mouse.get_pos() <=(200,1420):
					change = 0
			if pygame.mouse.get_pos() >= (520,1280):
					if pygame.mouse.get_pos() <= (660,1420):
						change = 0
		
							
						
			

					
	x=x + change
	enemy_x=enemy_x+enemy_x_change				
# Boundry Of Game				
	if x<=0:
	   	x=0
	elif x >= 570:
	   	x=570
	   	
	   	
	if enemy_x<=0:
					enemy_x_change = +5
					enemy_y=enemy_y+enemy_y_change
	elif enemy_x>=620:
					enemy_x_change = -5
					enemy_y = enemy_y + enemy_y_change
	if bullet_y<=-100:
		bullet_y=1000
		bullet_state="ready"
	if bullet_state is "fire":
		bullet(bullet_x,bullet_y)
		bullet_y-=bullet_y_change	
		
    colli= collision(enemy_x, enemy_y, bullet_x, bullet_y)
    
    if colli:
    	bullet_y=1000
    	bullet_state="ready"
    	score +=1
    	enemy_x = random.randint(0,620)
        enemy_y = random.randint(10,150)
    	
		
	
	player(x,y)
	button()
	enemy()
	pygame.display.update()