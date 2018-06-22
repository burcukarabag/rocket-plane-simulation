import pygame
import random
from math import sqrt
import os
import string , unicodedata
import math
from pygame.locals import *
from numpy import *
import pylab
import numpy as np
import matplotlib.pyplot as plt
from pygame_functions import *
from tkinter import *


BLACK = (0 , 0 , 0)
WHITE = (255 , 255 , 255)
GREEN = (0 , 255 , 0)
RED = (255 , 0 , 0)

background_colour = (255 , 130 , 1)

(width , height) = (1000 , 1000)
(w , h) = (50 , 50) #

screen = pygame.display.set_mode((width, height) , )
background = pygame.Surface(screen.get_size())

gok = pygame.image.load(os.path.join('gokyuzu.jpg'))
gok = pygame.transform.scale(gok, (width, height))


pygame.display.set_caption("Rocket-Plane")

pygame.font.init() #
myfont = pygame.font.SysFont('DriftType' , 60)
myfont_2 = pygame.font.SysFont(None , 30)
catch = myfont.render('UÇAK VURULDU!' , False , (255, 0, 200))
miss = myfont.render('UÇAK ISKALANDI!' , False , RED)


circle = pygame.image.load(os.path.join('yuva.png'))
circle = pygame.transform.scale(circle , (5 , 5))


planeimg = pygame.image.load(os.path.join('uçaksvg.png'))
planeimg = pygame.transform.scale(planeimg, (w , h))


rocketimg = pygame.image.load(os.path.join('roket.png'))
rocketimg = pygame.transform.scale(rocketimg , (w , h))

catch_point = pygame.image.load(os.path.join('yuva.png'))
catch_point = pygame.transform.scale(catch_point, (w, h))

radar = pygame.image.load(os.path.join('radarmerkezi.png'))
radar = pygame.transform.scale(radar, (w, h))


class rocket_plane(object):

    def __init__(self , x_rocket , y_rocket , v_rocket , x_plane , y_plane , v_plane , size):
        self.x_p = x_plane
        self.x_r = x_rocket
        self.y_p = y_plane
        self.y_r = y_rocket

        self.v_r = v_rocket
        self.v_p = v_plane

        self.count = 0
        self.colour = (255,255,255)
        self.deltat = 0


    def display(self):
        screen.blit(rocketimg , (int(self.x_r) , int(self.y_r)))
        screen.blit(planeimg , (int(self.x_p) , int(self.y_p)))
        screen.blit(radar , (15 , 710))

        return self.x_p, self.x_r, self.y_p, self.y_r


    def move(self):


        self.x_p = self.x_p + deltaT * (self.v_p) * 0.01
        self.y_p = self.y_p

        self.deltat = deltaT + self.deltat


        if self.x_p > 50 and not (sqrt((self.x_p - 15) * (self.x_p - 15) + (self.y_p - 710) * (self.y_p - 710)) > 1000):
            self.x_r = self.x_r + deltaT * self.v_r * ((self.x_p - self.x_r) / (sqrt((self.x_p - self.x_r) * (self.x_p - self.x_r) + (self.y_p - self.y_r) * (self.y_p - self.y_r)))) * 0.01
            self.y_r = self.y_r + deltaT * self.v_r * ((self.y_p - self.y_r) / (sqrt((self.x_p - self.x_r) * (self.x_p - self.x_r) + (self.y_p - self.y_r) * (self.y_p - self.y_r)))) * 0.01


        elif (sqrt((self.x_p - 15) * (self.x_p - 15) + (self.y_p - 710) * (self.y_p - 710)) > 1000):
            self.x_r = self.x_r + deltaT * (self.v_r) * 0.01
            self.y_r = self.y_r + deltaT * (self.v_r) * 0.01

        self.count += 1


        return self.x_p, self.x_r, self.y_p, self.y_r, self.count




    def stop(self):
        self.x_p = self.x_p - deltaT * (self.v_p) * 0.01
        self.y_p = self.y_p

        self.x_r = self.x_r - deltaT * self.v_r * ((self.x_p - self.x_r) / (sqrt((self.x_p - self.x_r) * (self.x_p - self.x_r) + (self.y_p - self.y_r) * (self.y_p - self.y_r)))) * 0.01
        self.y_r = self.y_r - deltaT * self.v_r * ((self.y_p - self.y_r) / (sqrt((self.x_p - self.x_r) * (self.x_p - self.x_r) + (self.y_p - self.y_r) * (self.y_p - self.y_r)))) * 0.01


    def text(self):

        pygame.draw.rect(screen , GREEN , (35, 790, 380, 90))

        pygame.draw.rect(screen , GREEN , (440 , 790 , 380 , 90))

        pygame.draw.rect(screen , (255 , 0 , 200) , (35 , 890 , 380 , 40))

        pygame.draw.rect(screen , (255 , 0 , 200) , (440 , 890 , 540 , 90))

        rocket_x = myfont_2.render(('rocket - x = ' + str(self.x_r)) , False , WHITE)
        screen.blit(rocket_x , (40, 800))

        rocket_y = myfont_2.render(('rocket - y = ' + str(1000-self.y_r)) , False , WHITE)
        screen.blit(rocket_y , (40 , 830))

        rocket_v = myfont_2.render(('rocket - velocity = ' + str(self.v_r)) , False , WHITE)
        screen.blit(rocket_v , (40 , 860))

        plane_x = myfont_2.render(('plane - x = ' + str(self.x_r)) , False , WHITE)
        screen.blit(plane_x , (450 , 800))

        plane_y = myfont_2.render(('plane - y = ' + str(1000-self.y_p)) , False , WHITE)
        screen.blit(plane_y , (450 , 830))

        plane_v = myfont_2.render(('plane - velocity = ' + str(self.v_p)) , False , WHITE)
        screen.blit(plane_v , (450 , 860))

        time = myfont_2.render(('time period = ' + str(self.deltat)), False , WHITE)
        screen.blit(time , (40 , 900))

        velocity_ratio = myfont_2.render(('velocity ratio = ' + (str(self.v_p)) + "/" + (str(self.v_r)) + '=' +  (str(self.v_p / self.v_r))) , False , WHITE)
        screen.blit(velocity_ratio , (450 , 900))

        y_p = myfont_2.render('-' + str(1000-self.y_p-250) , False , RED)
        screen.blit(y_p , (0 , self.y_p))

        y_r = myfont_2.render('-' + '0' , False , RED)
        screen.blit(y_r , (0 , 750))


running = True
while running:  # Keeps the window open until user quits

    running_2 = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False


    running_3 = True

    vp = ''
    vr = ''

    while running_3:
        vp = float(input("Uçağın hızını girin: "))
        vr = float(input("Roketin hızını girin: "))

        if not vp <= 0 and not vr <=0:
            running_3 = False

    y_plane_f = ''

    running_3 = True


    while running_3:
        y_plane_f = float(input("Roket ve uçak arasındaki mesafeyi girin (Uçağın yerden yüksekliği?): "))
        y_plane_f = (1000-y_plane_f-250)


        if not y_plane_f >= 750 and not y_plane_f <= 0:

            running_3 = False


    deltaT = 0.5
    e = 2
    size = 15

    x_plane = 0
    y_plane = y_plane_f
    v_plane = vp

    x_rocket = 0
    y_rocket = 750
    v_rocket = vr

    rocketplane = rocket_plane(x_rocket , y_rocket , v_rocket , x_plane , y_plane , v_plane , size)


    while running_2:  # Keeps the window open until user quits

        screen.blit(gok , (0 , -10))

        rocketplane.text()

        for event in pygame.event.get():
            if event.type == pygame.K_ESCAPE:
                pygame.quit()
                running = False

        x_p1 , x_r1 , y_p1 , y_r1 = rocketplane.display()
        x_p , x_r, y_p, y_r, count = rocketplane.move()


        if(sqrt((x_p - x_r)*(x_p - x_r) + (y_p - y_r)*(y_p - y_r)) < 1):

            rocketplane.display()
            rocketplane.move()

            while running_2:  # Keeps the window open until user quits
                for event in pygame.event.get():
                    if event.type == pygame.K_ESCAPE:
                        pygame.quit()
                        running = False

                rocketplane.stop()

                root = Tk()
                root.update()

                embed = Frame(root , width=100 , height=100)
                os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
                os.environ['SDL_VIDEODRIVER'] = 'dummy'

                L1 = Label(root , text="UÇAK VURULDU", font=('Helvetica', 16))
                L1.grid(row=5 , column=0)

                root.after(1000 , lambda: root.destroy())  # Destroy the widget after 30 seconds
                root.mainloop()

                running_2 = False


        if(sqrt((x_p-15)*(x_p-15) + (y_p - 710)*(y_p - 710)) > 1000):


            rocketplane.display()
            rocketplane.move()

            if y_r >  750:
                root = Tk()
                root.update()
                embed = Frame(root , width=300 , height=300)
                os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
                os.environ['SDL_VIDEODRIVER'] = 'dummy'

                L2 = Label(root , text="UÇAK ISKALANDI" , font=('Helvetica' , 16))
                L2.grid(row=5 , column=0)
                root.after(1000 , lambda: root.destroy())  # Destroy the widget after 30 seconds
                root.mainloop()


                rocketplane.stop()
                running_2 = False


        else:
            rocketplane.display()
            rocketplane.move()

        pygame.display.update()


    pygame.display.update()















