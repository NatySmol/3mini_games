import pygame as pg
import sys
import time

#inicializace
pg.init()
clock = pg.time.Clock()


class Square(pg.sprite.Sprite):
    def __init__(self, x_pos, y_pos, num):
        super().__init__()
        self.width = 120
        self.height = 120
        self.x = x_pos * self.width
        self.y = y_pos * self.height
        self.content = " "
        self.number = num
        self.image = blank_square
        self.image = pg.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = (self.x, self.y)

    def clicked(self, x_value, y_value):
        global turn, won
        if self.content == " ":
            if self.rect.collidepoint(x_value, y_value):
                self.content = turn
                board[self.number] = turn

                if turn == "x":
                    self.image = x_image
                    self.image = pg.transform.scale(self.image, (self.width, self.height))
                    turn = "o"
                    check_winner("x")

                    if not won:
                        ai_move()
                else:
                    self.image = o_image
                    self.image = pg.transform.scale(self.image, (self.width, self.height))
                    turn = "x"
                    check_winner("o")


def check_position():
    global move, AI_move


def check_center():
    global AI_move, move
    if board[5] == " ":
        AI_move = 5
        move = False


def check_corner():
    global AI_move, move

    for i in range(1, 11, 2):
        if i != 5 :
            if board[i] == " ":
                AI_move = i
                move = False
                break


def check_edge():
    global AI_move, move

    for i in range(2, 10, 2):
        if board[i] == " ":
            AI_move = i
            move = False
            break


def check_winner(player):
    global won, background, startx, starty, endx, endy, running
    for i in range(8):
        if board[winners[i][0]] == player and board[winners[i][1]] == player and board[winners[i][2]] == player:
            won = True
            get_position(winners[i][0], winners[i][2])
            break

    if won:
        Update()
        draw_line(startx, starty, endx, endy)
        square_group.empty()
        background = pg.image.load( player + "_winner.png")
        background = pg.transform.scale(background, (screen_width, screen_height))






def Winner(player):
    global AI_move, move

    for i in range(8):
        if board[winners[i][0]] == player and board[winners[i][1]] == player and board[winners[i][2]] == " ":
            AI_move = winners[i][2]
            move = False

        elif board[winners[i][0]] == player and board[winners[i][1]] == " " and board[winners[i][2]] == player:
            AI_move = winners[i][1]
            move = False
        elif board[winners[i][0]] == " " and board[winners[i][1]] == player and board[winners[i][2]] == player:
            AI_move = winners[i][0]
            move = False

def ai_move():
    global move, background
    move = True

    if move:
        Winner("o")
    if move:
        Winner("x")

    if move:
        check_center()
    if move:
        check_corner()
    if move:
        check_edge()
    if not move:
        for square in squares:
            if square.number == AI_move:
                square.clicked(square.x, square.y)

    else:  #remiza
        Update()
        time.sleep(1)
        square_group.empty()
        background = pg.image.load("tie.png")
        background = pg.transform.scale(background, (screen_width, screen_height))



def get_position(n1, n2):
    global startx, starty, endx, endy

    for s in squares:
        if s.number == n1:
            startx = s.x
            starty = s.y
        elif s.number == n2:
            endx = s.x
            endy = s.y


def draw_line(x1, y1, x2, y2):
    pg.draw.line(screen, (255, 0, 0), (x1, y1), (x2, y2), 10)
    pg.display.update()
    time.sleep(1.5)


def Update():
    screen.blit(background, (0,0))
    square_group.draw(screen)
    square_group.update()
    pg.display.update()

def reset():
    global won, starty, startx, endy, endx
    square_group.empty()
    startx = 0
    starty = 0
    endx = 0
    endy = 0
    won = False


#screen
screen_height = 500
screen_width = 500
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("Piškvorky")


background_color = (60, 190, 190)
background = pg.image.load("background.png")
background = pg.transform.scale(background, (screen_width, screen_height))

#images
x_image = pg.image.load("x_image2.png")
o_image = pg.image.load("o_image2.png")
blank_square = pg.image.load("square.png")

#text
font = pg.font.Font("CaviarDreams.ttf", 25)
text = font.render("Play again", True, (0, 0, 153))

#moves
move = True
AI_move = 5
won = False

#squares
square_group = pg.sprite.Group()
squares = []

#kombinace výhry
winners = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

board = [" " for i in range(10)]

startx = 0
starty = 0
endx = 0
endy = 0

#vykreslí čtverečky
num = 1
for y in range(1, 4):
    for x in range(1, 4):
        sq = Square(x, y, num)
        square_group.add(sq)
        squares.append(sq)

        num += 1

turn = "x"


while True:
    mouse = pg.mouse.get_pos()
    user = pg.key.get_pressed()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        if event.type == pg.MOUSEBUTTONDOWN and turn == "x":
            mx, my = pg.mouse.get_pos()
            for s in squares:
                s.clicked(mx, my)
        if user[pg.K_r]:
           reset()



    Update()
    clock.tick(60)