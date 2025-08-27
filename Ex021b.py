#Faça um programa que abra e reproduza o áudio de um arquivo MP3.

import pygame

pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()

# Mantém rodando enquanto a música está tocando
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

pygame.quit()
