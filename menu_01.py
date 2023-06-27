import pygame as pg
import sys
import snake

pg.init()
clock = pg.time.Clock()

#screen
screen_width = 700
screen_height = 700
screen = pg.display.set_mode((screen_width, screen_height))
background_color = (204, 229, 255)
pg.display.set_caption("Menu")

font =pg.font.Font("CaviarDreams.ttf", 30)
font_uvod = pg.font.Font("CaviarDreams.ttf", 50)
text_pingpong = font.render('PingPong', True, (0, 0, 153))
text_snake = font.render("Snake", True, (0, 0, 153))
text_piskvorky = font.render("Piškvorky" ,True,(0, 0, 153) )
text_uvod = font_uvod.render("Choose one of the games!", True, (0, 0, 153))

button1 = pg.Rect(280, 350, 150, 40)
button2 = pg.Rect(280, 290, 150, 40)
button3 = pg.Rect(280, 230, 150, 40)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        #pingpong button
        if event.type == pg.MOUSEBUTTONDOWN:
            if 280 <= mouse[0] <= 420 and 330 <= mouse[1] <= 370:
                import pingpong.pingpong_01
        #snake button
        if event.type == pg.MOUSEBUTTONDOWN:
            if 280 <= mouse[0] <= 420 and 270 <= mouse[1] <= 310:
                import snakeandapple_01

        #piskvorky button
        if event.type == pg.MOUSEBUTTONDOWN:
            if 280 <= mouse[0] <= 420 and 210 <= mouse[1] <= 250:
                import piskvorky_01


    screen.fill(background_color)
    mouse = pg.mouse.get_pos()

    #pong button rectangles
    if 280 <= mouse[0] <= 410 and 350 <= mouse[1] <= 390:
        pg.draw.rect(screen, (102, 178, 255),button1)

    else:
        pg.draw.rect(screen, (0, 204, 204), button1)
    screen.blit(text_pingpong, (290,350))

    #snake button rectangles
    if 280 <= mouse[0] <= 410 and 270 <= mouse[1] <= 310:
        pg.draw.rect(screen, (102, 178, 255),button2)

    else:
        pg.draw.rect(screen, (0, 204, 204), button2)
    screen.blit(text_snake, (290,290))

    #piskvorky rectangles
    if 280 <= mouse[0] <= 410 and 210 <= mouse[1] <= 250:
        pg.draw.rect(screen, (102, 178, 255),button3)

    else:
        pg.draw.rect(screen, (0, 204, 204), button3)
    screen.blit(text_piskvorky, (290,230))

    #text uvod
    screen.blit(text_uvod, (50, 50))

    pg.display.update()
    clock.tick(60)