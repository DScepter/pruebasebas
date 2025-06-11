# ¡Crea tu propio juego de disparos!
from random import *
from pygame import *
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Tirador")
background = transform.scale(image.load("galaxy.jpg"), (win_width, win_height))
mixer.init()
mixer.music.load("fire.ogg")
mixer.music.play()
fire_sound=mixer.Sound("fire.ogg")

font.init()
font1 = font.Font(None,36)
font2 = font.Font(None,36)

game = True
final = True
points = 0
lost = 0
FPS = 60
clock = time.Clock()
lasers = sprite.Group()

# clase padre para otros objetos
class GameSprite(sprite.Sprite):
    # constructor de clase
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # llamamos al constructor de la clase (Sprite):
        sprite.Sprite.__init__(self)

        # cada objeto debe almacenar una propiedad image
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        # cada objeto debe almacenar la propiedad rect en la cual está inscrito
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    # método que dibuja al personaje en la ventana
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



# clase del jugador principal
class Player(GameSprite):
    def update_1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 40:
            self.rect.y += self.speed
    def update_2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 40:
            self.rect.y += self.speed


class Ball(GameSprite):
    def update(self):
        speed_x = self.speed
        speed_y = self.speed

        self.rect.y += speed_x
        self.rect.x += speed_y

        if sprite.collide_rect(racket1, self) or sprite.collide_rect(racket2, self):
            speed_x *= -1
            speed_y *= 1
        
        if self.rect.y > win_height-50 or self.rect.y < 0:
            speed_y *= -1

        if self.rect.x < 0:
            finish = True
            window.blit(text_lose, (200, 200))
            game_over = True
        
        if self.rect.x > win_width:
            finish = True
            window.blit(text_lose, (200, 200))
            game_over = True


racket1 = Player("racket.png",50,400,30,60,5)
racket2 = Player("racket.png",600,400,30,60,5)
ball = Ball("tenis_ball.png",0,0,40,40,4)

while game:   
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background,(0, 0))
    text_lose = font2.render("Fallados: " + str(lost), 1, (255,255,255))
    window.blit(text_lose,(10,10)) 
    if final:    
    
        racket1.update_1()
        racket1.reset()
        racket2.update_2()
        racket2.reset()
        ball.update()
        ball.reset()

        #if sprite.spritecollide(player, enemies,False):
        #    final = False
    else: 
        text_gameover = font2.render("Has Perdido",)
        window.blit(text_lose,(100,100))

    display.update()
    clock.tick(FPS)
