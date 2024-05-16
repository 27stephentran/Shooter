from pygame import *
from random import randint
from time import time as timer

img_background = "galaxy.jpg"
img_player = "rocket.png"
img_ufo = "ufo.png"
img_asteroid = "asteroid.png"
img_bullet = "bullet.png"

win_height = 700
win_width = 700

lost = 0
goals = [6, 12, 18, 24]
health = 3

window = display.set_mode((win_height, win_width))
display.set_caption("Space Shooter")
background = transform.scale(image.load(img_background), (win_height, win_width))


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

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed 
        if keys[K_d] and self.rect.x < win_width - 80:
            self.rect.x += self.speed

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost += 1

# create the player
player = Player(img_player, 5, win_height - 100, 80, 100, 10)

# creating the enemies
ufos = sprite.Group()
for i in range(3):
    ufo = Enemy(img_ufo, randint(80, win_width - 80), -40, 80, 50, randint(1,7))
    ufos.add(ufo)

asteroids = sprite.Group()
for i in range(3):
    asteroid = Enemy(img_asteroid, randint(80, win_width - 80), -40, 80, 50, randint(1,7))
    asteroids.add(asteroid)

font.init()
font1 = font.Font(None, 80)
win = font1.render("YOU WIN!", True, (255, 255, 255))
lose = font1.render("YOU LOSE!", True, (255, 255, 255))


font2 = font.Font(None, 36)


finish = False
real_time = False
num_fire = 0
run = True
FPS = 60
clock = time.Clock()
score = 0


while run:
    for e in event.get():
        if e.type == QUIT:
            run = False




    if not finish:
        window.blit(background, (0,0))

        player.update()
        ufos.update()
        asteroids.update()

        player.reset()
        ufos.draw(window)
        asteroids.draw(window)

        # for goal in goals:
        if score >= goals[0]:
            finish = True
            window.blit(win, (200, 200))

        text = font2.render("Score:" + str(score), 1, (255, 255, 255)) 
        window.blit(text, (10, 20))

        text_lose = font2.render("Missed:" + str(lost), 1, (255, 255, 255))
        window.blit(text_lose, (10, 50))


    display.update()
    clock.tick(FPS)



