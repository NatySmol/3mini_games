import pygame as pg
import sys
import random

def ball_movement():
    global ball_speedx, ball_speedy, player_score, opponent_score, score_time
    ball.x += ball_speedx
    ball.y += ball_speedy

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speedy *= -1

    if ball.left <= 0:
        player_score += 1
        score_time = pg.time.get_ticks()

    if ball.right >= screen_width:
        opponent_score += 1
        score_time = pg.time.get_ticks()



    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speedx *= -1

def ball_restart():
    global ball_speedx, ball_speedy, score_time

    time = pg.time.get_ticks()

    ball.center = (screen_width/2, screen_height/2)
    #odpočet
    if time - score_time < 700:
        number3 = counter_font.render("3", False, black)
        screen.blit(number3, (screen_width/2-15, screen_height/2+20))
    if 700< time - score_time < 1400:
        number2 = counter_font.render("2", False, black)
        screen.blit(number2, (screen_width/2-15, screen_height/2+20))

    if 1400 < time - score_time < 2100:
        number1 = counter_font.render("1", False, black)
        screen.blit(number1, (screen_width/2- 15, screen_height/2+20))

    if time - score_time < 2100:
        ball_speedx, ball_speedy = 0, 0
    else:
        ball_speedy = 6 * random.choice((1, -1))
        ball_speedx = 6 * random.choice((1, -1))
        score_time = None



def player_movement():
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def opponent_movement():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

#inicializace
pg.init()
clock = pg.time.Clock()

#hlavní okno
screen_width = 960
screen_height = 760
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("Ping Pong")

#rectangles
ball = pg.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
player = pg.Rect(screen_width-20, screen_height/ - 70, 10, 140)
opponent = pg.Rect(10, screen_height/2 - 70, 10, 140)

background_color = (180, 60, 80)
grey = pg.Color("grey")
black = pg.Color("black")


ball_speedx = 6
ball_speedy = 6
player_speed = 0
opponent_speed = 6

# text
player_score = 0
opponent_score = 0
game_font = pg.font.Font("freesansbold.ttf", 32)
counter_font = pg.font.Font("freesansbold.ttf", 64)

#timer
score_time = True



#main Loop
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit() #zavírá celou hru
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_DOWN:
                player_speed += 7
            if event.key == pg.K_UP:
                player_speed -= 7
        if event.type == pg.KEYUP:
            if event.key == pg.K_DOWN:
                player_speed -= 7
            if event.key == pg.K_UP:
                player_speed += 7


    ball_movement()
    player.y += player_speed
    player_movement()
    opponent_movement()

    # vizualizace
    screen.fill(background_color)
    pg.draw.rect(screen, grey, player)
    pg.draw.rect(screen, grey, opponent)
    pg.draw.ellipse(screen, grey, ball)
    pg.draw.aaline(screen, grey, (screen_width /2, 0), (screen_width/2, screen_height))

    if score_time:
        ball_restart()

    #text - score
    player_text = game_font.render(f"{player_score}", False, grey)
    screen.blit(player_text, (495,10))
    opponent_text = game_font.render(f"{opponent_score}", False, grey)
    screen.blit(opponent_text, (450, 10))


    pg.display.flip() #vykresluje vše na obrazovku
    clock.tick(60)
