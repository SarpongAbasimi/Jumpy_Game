import pygame
import random

width = 480
height = 600
font_name = "Times"
fps =60
player_friction = -0.12
player_acc =0.9
player_gravity = 0.5
#starting platform
platform_list = [(0,height -40,width,40),(width/2 -50,height*3/4,100,10),
                (125,height -350,100,10),(350,200,100,10),(175,100,50,10)] 
#difine colour
white = (255,255,255)
black =(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
yellow =(255,255,0)
lightblue =(0,155,155)
bgcolor = lightblue
