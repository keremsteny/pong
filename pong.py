

from pygame import *


#шрифты и надписи
font.init()
font1 = font.SysFont('Arial', 40)
win1 = font1.render('Игрок 1 выйграл', True, (255, 255, 255))
lose = font1.render('Игрок 2 выйграл', True, (180, 0, 0))
font2 = font.SysFont('Arial', 40)

#нам нужны такие картинки:
img_back = "fon.jpg" #фон игры
img_hero = "player.jpg" #герой
img_bullet = "pong.png" #пуля


#класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
 #конструктор класса
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       #вызываем конструктор класса (Sprite):
       sprite.Sprite.__init__(self)


       #каждый спрайт должен хранить свойство image - изображение
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed


       #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 #метод, отрисовывающий героя на окне
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))


#класс главного игрока
class Player(GameSprite):
    #метод для управления спрайтом стрелками клавиатуры
    def update_R(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 5:
            self.rect.y += self.speed
    def update_L(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 5:
            self.rect.y += self.speed
       

#создаем окошко
win_width = 700
win_height = 500
display.set_caption("Ping Pong")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))


#создаем спрайты
roketka1 = Player(img_hero, 5, 50, 15, 100, 10)
roketka2 = Player(img_hero, 680, 100, 15, 100, 10)
ball = GameSprite(img_bullet,350,250,50,50,10)

finish = False
#основной цикл игры:
run = True #флаг сбрасывается кнопкой закрытия окна
clock = time.Clock()
x_speed = 5
y_speed = 5
while run:
    #событие нажатия на кнопку Закрыть
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        #обновляем фон
        window.blit(background,(0,0))


        #производим движения спрайтов
        roketka1.update_L()
        roketka2.update_R()

        ball.rect.x += x_speed
        ball.rect.y += y_speed

        if ball.rect.y > win_height -25 or ball.rect.y < 0:
            y_speed *= -1
        if sprite.collide_rect(roketka1,ball):
            x_speed *= -1
        if sprite.collide_rect(roketka2,ball):
            x_speed *= -1
        if ball.rect.x >= 700:
            finish = True
            window.blit(win1,(200,200))
        elif ball.rect.x <= 0:
            finish = True
            window.blit(lose,(200,200))


        #обновляем их в новом местоположении при каждой итерации цикла
        roketka1.reset()
        roketka2.reset()
        ball.reset()


    display.update()
    clock.tick(60)
