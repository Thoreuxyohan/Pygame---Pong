import pygame, sys, random

def ball_animation():
    global ball_speed_x,ball_speed_y
    #Speed of the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y  

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *=-1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_restart()

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

def player_animation():
    global player_speed
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def opponent_animation():
    global opponent_speed
    opponent.y += opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

def ball_restart():
    global ball_speed_x,ball_speed_y
    ball.center = (screen_width/2,screen_height/2)
    ball_speed_x *= random.choice((1,-1))
    ball_speed_y *= random.choice((1,-1))

#General Setup
pygame.init()
clock = pygame.time.Clock()

#Setting up the main screen
screen_width = 1280
screen_height = 900
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pong')

#Game Rectangles
ball = pygame.Rect(screen_width/2 - 15,screen_height/2 - 15,30,30,)
player = pygame.Rect(screen_width - 20,screen_height/2 - 70,10,140)
opponent = pygame.Rect(10,screen_width/2 - 70,10,140)

bg_color = pygame.Color('grey12')
light_grey = (200,200,200)

ball_speed_x = 7
ball_speed_y = 7
player_speed = 0
opponent_speed = 0

#Function to play the game
while True:
    #Handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #Player Movement Keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7

        #Opponent Movement Keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                opponent_speed += 7
            if event.key == pygame.K_a:
                opponent_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                opponent_speed -= 7
            if event.key == pygame.K_a:
                opponent_speed += 7

    ball_animation()
    player_animation()
    opponent_animation()

    #Visual of the game
    screen.fill(bg_color)
    pygame.draw.rect(screen,light_grey,player)
    pygame.draw.rect(screen,light_grey,opponent)
    pygame.draw.ellipse(screen,light_grey,ball) 
    pygame.draw.aaline(screen,light_grey, (screen_width/2,20), (screen_width/2,screen_height))


    pygame.display.flip()
    clock.tick(60)
