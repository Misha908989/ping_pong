from pygame import*
from time import time as timer

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)

        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player1(GameSprite):
    def update_1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y > 5:
            self.rect.y += self.speed
    def update_2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y > 5:
            self.rect.y += self.speed




class Ball:
    #Створюємо метод-конструктор. Він приймає наступні аргументи: радіус, колір, колір кордону, x, y, швидкість !!! не забуваємо про self у дужках
    def __init__(self,radius,color,color_border,x,y,speed,path_image=None):  
        #Створюємо властивість радіус
        self.RADIUS = radius
        #Створюємо властивість колір
        self.COLOR = color
        #Створюємо властивість колір кордону
        self.COLOR_BORDER = color_border
        #Створюємо властивість x
        self.X = x
        #Створюємо властивість y
        self.Y = y
        #Створюємо властивість швидкість
        self.SPEED = speed
        #Напрям польоту кульки
        self.WHERE_MOVE = None
        #Швидкіть польоту кульки в сторону
        self.ANGLE_SPEED = self.SPEED
        # властивість відповідає, чи відбувається рух кульки
        self.MOVING = True
        self.ball_rect = Rect(self.X - self.RADIUS,self.Y - self.RADIUS,self.RADIUS*2,self.RADIUS*2)   
    #Створюємо метод, що малює нашу кульку. !!! не забуваємо про self у дужках
    def show_ball(self,window):
        #Малюємо кульку
        draw.circle(window, self.COLOR, (self.X, self.Y), self.RADIUS)
        #Малюємо кордон кульки
        draw.circle(window, self.COLOR_BORDER, (self.X, self.Y), self.RADIUS,  5)
    # Створюємо метод, для руху кульки
    def move_ball(self,platform,platform1):
        # Створюємо невидимий прямокутник, всередині якого знаходиться кулька

        self.ball_rect.x+=self.SPEED
        self.ball_rect.y+=self.SPEED
        if self.ball_rect.y < 0 or self.ball_rect.y+20 > height:
            self.ball_rect.y *= -1
        if self.ball_rect.colliderect(platform.rect) or self.ball_rect.colliderect(platform1.rect):
            self.ball_rect.x *= -1


font.init()
text1 = font.SysFont("Arial", 36)
text2 = font.SysFont("Arial", 80)

win1 = text2.render("PLayer1 WIN!", True, (0, 255, 0))
win2 = text2.render("Player2 WIN!", True, (255, 0, 0))

mixer.init()
mixer.music.load("music.wav")
mixer.music.play()

img_back = "bg.jpg"
img_player = "pt.jpg"

speed_x = 3
speed_y = 3
tvick = (220, 255, 255)
widht = 600
height = 500

window = display.set_mode((widht, height))
window.fill(tvick)

player1 = Player1(img_player, 50, height//2, 10, 100, 10)
player = Player1(img_player, widht-100, height//2, 10, 100, 10)

ball = Ball(20, (0, 0, 0), (10, 10, 100), 250, 300, 5)

clock = time.Clock()
FPS = 30
game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.fill(tvick)
    player.reset()
    player1.reset()
    ball.show_ball(window)
    player.update_1()
    player1.update_2()
    ball.move_ball(player, player1)

    display.update()
    clock.tick(FPS)