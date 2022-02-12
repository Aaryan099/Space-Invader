import pygame
import random 
import math
from pygame import mixer 

pygame.init()

################### SETUP ##############################
screen = pygame.display.set_mode((720,1600))


################### IMAGES #############################
background = pygame.image.load('galaxy.png')
bulletImg = pygame.image.load('bullet.png')
bulletImg = pygame.transform.scale(bulletImg,(70,70))
bulletImg2 = pygame.transform.scale(bulletImg,(50,50))

################## BACKGROUND SOUND #################
mixer.music.load('background.wav')
mixer.music.play(-1)


################# Title And Icon ###########################
pygame.display.set_caption('My Game')



# Player
playerImg= pygame.image.load('player.png')
playerImg = pygame.transform.scale(playerImg,(150,150))
enemyImg = pygame.image.load('monster.png')
enemyImg = pygame.transform.scale(enemyImg,(80,80))


# Variables
change = 0
x=300
y= 1100


# ENEMY 
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
num_of_enemy= 4


for i in range(num_of_enemy):
	enemy_x.append(random.randint(0,620))
	enemy_y.append(random.randint(10,150))
	enemy_x_change.append(10)
	enemy_y_change.append(60)

#COLOR

white = ((255,255,255))
brown = ((130,60,60))
black = ((0,0,0))
blue = ((0,0,50))


# Bullet
bullet_x =0
bullet_y=1000
bullet_x_change= 0
bullet_y_change = 30
bullet_state = "ready"

#################### Score ##############################
score= 0
font = pygame.font.Font('freesansbold.ttf',32)
txt_x=10
txt_y=10
over_font = pygame.font.Font('freesansbold.ttf',64)



def game_over_text():
	over_text = over_font.render("GAME OVER",True,(255,255,255))
	screen.blit(over_text,(180,500))
	

def show_score(a,b):
	report= font.render("Score = "+ str(score),True,(255,255,255))
	screen.blit(report,(a,b))



def enemy(i):
	screen.blit(enemyImg,(enemy_x[i],enemy_y[i]))

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
	screen.blit(bulletImg,(a+40,b+70))
	
	
def collision(enemy_x,enemy_y,bullet_x,bullet_y):
    distance = (math.sqrt(math.pow(enemy_x-bullet_x,2))+(math.pow(enemy_y-bullet_y,2)))
    
    
    if distance < 140:
    	return True
    else:
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

			
################## INPUT FROM SCREEN ################			
		if event.type == pygame.MOUSEBUTTONDOWN:
			if pygame.mouse.get_pos() >= (60,1280):
				if pygame.mouse.get_pos() <=(200,1420):
					change = -10
					
			if pygame.mouse.get_pos() >= (520,1280):
					if pygame.mouse.get_pos() <= (660,1420):
						change = +10
			if pygame.mouse.get_pos() >=(295,1280):
		 		if pygame.mouse.get_pos() <=(405,1420):
		 		    bullet_sound = mixer.Sound('laser.wav')
		 		    bullet_sound.play()
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
					
############## Boundry Of Game	######################			
	if x<=0:
	   	x=0
	elif x >= 570:
	   	x=570


########### For Loop ######################################

	for i in range(num_of_enemy):
		
############# GAME OVER #############################
		if enemy_y[i] > 1000:
			for j in range(num_of_enemy):
				enemy_y[i]=4000
				game_over_text()
				break
				
#################### Enemy Movement ####################
		enemy_x[i]=enemy_x[i]+enemy_x_change[i]	   	
		if enemy_x[i]<=0:
			enemy_x_change[i] = +10
			enemy_y[i]=enemy_y[i]+enemy_y_change[i]
		elif enemy_x[i]>=640:
			enemy_x_change[i] = -10
			enemy_y [i]= enemy_y[i] + enemy_y_change[i]

			
###################### Collision #########################			
		collision2= collision(enemy_x[i],enemy_y[i],bullet_x,bullet_y)
	
		if collision2:
    			bullet_y = 1000
    			collision_sound= mixer.Sound('explosion.wav')
    			collision_sound.play()
    			bullet_state="ready"
    			score +=1
   	 		enemy_x[i]= random.randint(0,620)
 	   		enemy_y[i] = random.randint(10,150)
		enemy(i)
	
		
		
################### Bullet Movement ######################
	if bullet_y<=-100:
		bullet_y=1000
		bullet_state="ready"
	if bullet_state is "fire":
		bullet(bullet_x,bullet_y)
		bullet_y-=bullet_y_change	
		
	
    	
    	
		
	
	player(x,y)
	button()
	
	show_score(txt_x,txt_y)
	pygame.display.update()
   