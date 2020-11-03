####______importation______####
import pygame
from script.image import image
from script.text import text
from script.player import player
from script.IA import IA
from random import randint
from time import sleep
pygame.init()
####______initialisation______####
pygame.display.set_caption("STAR INVADER")
screen=pygame.display.set_mode((1920,1080))
####______variable______####
running=True
pressed={}
all_IA=pygame.sprite.Group()
all_laser=pygame.sprite.Group()

####______chargement______####
bg=pygame.image.load("image/background.jpg")
bouton_play=image("image/bouton_play.png",685,480)
menu=image("image/STAR_INVADER.png", 550, 300)
icone=pygame.image.load("image/icone.png")
heart=pygame.image.load("image/heart.png")
player=player(895, 900)#895,900
game_over=pygame.image.load("image/game_over.png")

####______générale______####
pygame.display.set_icon(icone)

####______boucles de jeux(menu)______####
def main():
    global screen,running,pressed,bg,menu, all_IA
    while running:
    ####______affichage des éléments______####
        screen.blit(bg, (0, 0))
        screen.blit(menu.image, menu.rect)
        screen.blit(bouton_play.image, bouton_play.rect)

        pygame.display.flip()
    ####______Event______####
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                print("fermeture du jeu!!")
            if event.type == pygame.KEYDOWN:
                pressed[event.key] = True
            if event.type == pygame.KEYUP:
                pressed[event.key]=False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
                if bouton_play.rect.collidepoint(x ,y):
                    print("bouton clicker !")
                    secondaire()
                    break

####______boucle du jeux(jeux)______####
def secondaire():
    global screen,running,pressed,bg,menu,all_IA,all_laser
    player.health = 3
    all_IA.empty()
    while running:
        ####______affichage des éléments______####
        menu.remove()
        bouton_play.remove()
        screen.blit(bg, (0, 0))
        screen.blit(player.image, player.rect)

        #généré ou pas un mmonstre
        if randint(0, 50) == randint(0, 50):
            IA_player = IA(randint(0,1790), -140)
            all_IA.add(IA_player)

        all_IA.draw(screen)
        all_laser.draw(screen)

        #affichage des coeur du joueur en fonction de sa vie !
        if player.health == 3:
            screen.blit(heart, (0,0))
            screen.blit(heart, (80, 0))
            screen.blit(heart, (160, 0))
        elif player.health == 2:
            screen.blit(heart, (0, 0))
            screen.blit(heart, (80, 0))
        elif player.health == 1:
            screen.blit(heart, (0, 0))
        else:
            main()
            #gameOver()  #voir pk pas utilisé a la fonction même  
            break

        pygame.display.flip()

        ####______update_____####
        #update IA
        for ia in all_IA:
            ia.move_down()
            if ia.rect.y >= 1080:
                all_IA.remove(ia)
            if pygame.sprite.spritecollide(ia, all_laser, True, pygame.sprite.collide_mask):
                all_IA.remove(ia)

        if pygame.sprite.spritecollide(player, all_IA, False, pygame.sprite.collide_mask):
            player.health -= 100

        #update laser
        for q in all_laser:
            q.move_up(15)
            if q.rect.y <= -140:
                all_laser.remove(q)
            if pygame.sprite.spritecollide(q, all_IA, True, pygame.sprite.collide_mask):
                all_laser.remove()

        ####______Event______####
        if pressed.get(pygame.K_q):
            player.move_left()
        if pressed.get(pygame.K_d):
            player.move_right()
        if pressed.get(pygame.K_z):
            player.move_up()
        if pressed.get(pygame.K_s):
            player.move_down()
        if pressed.get(pygame.K_SPACE):
            laser_x = player.rect.x + 50
            laser_y = player.rect.y
            laser = image("image/laser.png",laser_x,laser_y)
            all_laser.add(laser)
            print("tir lancé")


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                print("fermeture du jeu!!")
            if event.type == pygame.KEYDOWN:
                pressed[event.key] = True
            if event.type == pygame.KEYUP:
                pressed[event.key]=False
                                                                            
def gameOver():                             #je n'utilise pas cette fonction car je le rediréctionne sur la boucle de menu !!
    global screen, running, pressed, bg, menu, all_IA,game_over
    #affichage des éléments
    screen.blit(bg, (0, 0))

    pygame.display.flip()
    #boucle de jeux game over !
    while running:
        #event pour fermer la fenetre
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                print("fermeture du jeu !")

main()