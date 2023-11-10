import pygame, sys

pygame.init()
screen = pygame.display.set_mode((400, 500)) #Display surface
clock = pygame.time.Clock() 
# test_surface = pygame.Surface((100,200)) #Surface
# test_surface.fill((0, 0, 255)) #Color
# x_pos = 200 #Actualizar la  posición: y+ = abajo, y- = arriba
# test_rect = test_surface.get_rect(center = (200, 250)) #Rectangulo posicionado en el centro de esas coordenadas

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #Salir de la ventana
            pygame.quit()
            sys.exit()
    #Puede recibirlo como RGB en tuple o Color Object
    # screen.fill(pygame.Color('gold'))
    screen.fill((205, 255, 45))
    #Block Image Transfer (Para transferir el surface al display surface, x, y position)
    # screen.blit(test_surface, test_rect) #test_rect posicion.
    pygame.display.update()
    #Recibe como argumento un "Framerate", se refiere a cuánto tiempo este ciclo corre por segundo
    clock.tick(60)
