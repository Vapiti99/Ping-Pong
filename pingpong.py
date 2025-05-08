from pygame import *
class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (wight, height)) 
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y

   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
   def update_r(self):
       keys = key.get_pressed()
       if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.y < win_height - 80:
           self.rect.y += self.speed
   def update_l(self):
       keys = key.get_pressed()
       if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_s] and self.rect.y < win_height - 80:
           self.rect.y += self.speed

#игровая сцена:
back = transform.scale(image.load('fon.png'), (600,500))
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Ping-Pong")
fire = image.load('fire.png')

#создания мяча и ракетки   
racket1 = Player('rocket.png', 0, 200, 4, 50, 150) 
racket2 = Player('rocketR.png', 550, 200, 4, 50, 150)
ball = GameSprite('ball.png', 200, 200, 4, 50, 50)

font.init()
font = font.Font(None, 35)
lose1 = font.render('Правый игрок - УМНИЧКА!', True, (255, 147, 0))
lose2 = font.render('Левый игрок - СУПЕРГЕРОЙ', True, (255, 155, 0))

speed_x = 3
speed_y = 3


#флаги, отвечающие за состояние игры
game = True
finish = False
clock = time.Clock()
FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
        window.blit(back,(0,0))
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= 1
        
        #если мяч достигает границ экрана, меняем направление его движения
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1

        #если мяч улетел дальше ракетки, выводим условие проигрыша для первого игрока
        if ball.rect.x < 10:
            finish = True
            window.blit(lose1, (200, 180))


        #если мяч улетел дальше ракетки, выводим условие проигрыша для второго игрока
        if ball.rect.x > win_width-10:
            finish = True
            window.blit(lose2, (50, 180))
            window.blit(fire, (120, 250))

        racket1.reset()
        racket2.reset()
        ball.reset()


    display.update()
    clock.tick(FPS)
