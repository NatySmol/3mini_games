import pygame as pg
import sys
from pygame.math import Vector2
import random


class Snake:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)
        self.new_block = False
        self.sound_eating = pg.mixer.Sound("crunch.wav")


    def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            snake_rect = pg.Rect(x_pos, y_pos, cell_size, cell_size)
            pg.draw.rect(screen, blue, snake_rect)

    def move_snake(self):
       if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
       else:
           body_copy = self.body[:-1]
           body_copy.insert(0, body_copy[0] + self.direction)
           self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

    def reset(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)

    def sound_of_eating(self):
        self.sound_eating.play()


class Apple:
    def __init__(self):
        #position (vektor)
        self.randomize()

    def draw_apple(self):
        #rectangle
        apple_rect = pg.Rect(int(self.pos.x * 40), int(self.pos.y * 40), 40, 40)
        screen.blit(fruit, apple_rect)
        # pg.draw.rect(screen, red, apple_rect)

    def randomize(self):
        # position (vektor)
        self.x = random.randint(0, cell - 1)
        self.y = random.randint(0, cell - 1)
        self.pos = Vector2(self.x, self.y)


class LOGIC:
    def __init__(self):
        self.snake = Snake()
        self.apple = Apple()
        self.sound_gameover = pg.mixer.Sound("gameover.wav")

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_borders()

    def draw(self):
        self.draw_grass()
        self.apple.draw_apple()
        self.snake.draw_snake()
        self.score()


    def check_collision(self):
        if self.apple.pos == self.snake.body[0]: #když se srazí hlava hada s jablkem tak:
            self.apple.randomize()  #jablko se umístí jinam
            self.snake.add_block()   #přidám nový blok hada
            self.snake.sound_of_eating()

        for block in self.snake.body[1:]:
            if block == self.apple.pos:     #pokud se jablko zobrazí na hada, změní se pozice jablka
                self.apple.randomize()

    def check_borders(self): #kontroluje jestli jsme nenarazili do sebe nebo jestli nejsme mimo obrazovku
        if not 0 <= self.snake.body[0].x < cell or not 0 <= self.snake.body[0].y < cell: #had narazí do stěny
            self.sound_gameover.play()
            self.gameover()

        for block in self.snake.body[1:]: #had narazí do sebe
            if block == self.snake.body[0]:
                self.gameover()

    def gameover(self):
        self.snake.reset()

    def draw_grass(self): #vykreslí kostičkovaně pozadí
        grass_color = (167, 209, 61)
        for row in range(cell):
            if row %2 == 0:
                for col in range(cell):
                    if col % 2 == 0:
                        grass_rect = pg.Rect(col * cell_size , row* cell_size, cell_size, cell_size)
                        pg.draw.rect(screen, grass_color,grass_rect)
            else:
                for col in range(cell):
                    if col % 2 != 0:
                        grass_rect = pg.Rect(col * cell_size , row* cell_size, cell_size, cell_size)
                        pg.draw.rect(screen, grass_color,grass_rect)

    def score(self): #score odpovídá délce hada, tj. kolikrát jsme snědli jablko
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text, True, (56, 74, 12))
        score_x = 400
        score_y = 20
        score_rect = score_surface.get_rect(center = (score_x, score_y))
        screen.blit(score_surface,score_rect)

        screen.blit(trophy,(340, 5) )




#inicializace
pg.mixer.pre_init(44100, -16, 2, 512)
pg.init()
clock = pg.time.Clock()

#obrazky
fruit = pg.image.load("apple.png")
trophy = pg.image.load("trophy.png")

#font
game_font = pg.font.Font("PoetsenOne-Regular.ttf", 40)

#screen
screen_width = 800
screen_height = 800
screen = pg.display.set_mode((screen_width, screen_height))

#colors
green = (50, 200, 150)
blue = pg.Color("blue")
red = pg.Color("red")

cell = 20
cell_size = 40



apple = Apple()
snake = Snake()

Update = pg.USEREVENT
pg.time.set_timer(Update, 150)

main_game = LOGIC()


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == Update:
            main_game.update()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
            if event.key == pg.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)
            if event.key == pg.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)
            if event.key == pg.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)


    screen.fill(green)

    main_game.draw()


    pg.display.update()
    clock.tick(60)
