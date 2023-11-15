import pygame, sys,random
from pygame.math import Vector2

class Snake:
    def __init__(self): #Inicio
        self.body = [Vector2(5,10),Vector2(6,10),Vector2(7,10),Vector2(8,10)] #El cuerpo de la serpiente.
        self.direction = Vector2(1,0) #Input del jugador.

    def draw_snake(self): #Dibujar a la serpiente
        for block in self.body:
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            #Creando el rectangulo
            block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)
            #Dibujando el rectangulo
            pygame.draw.rect(screen,(45,154,200),block_rect)

    def move_snake(self): #Mover a la serpiente
        body_copy = self.body[:-1] #Eliminar el ultimo bloque de la serpiente.
        body_copy.insert(0,body_copy[0] + self.direction) #Nuevo cuerpo
        self.body = body_copy[:]               

class Fruit:
    def start(self): #Inicio
        #Crear un cuadro, usando y, x position.
        self.x = random.randint(0,cell_number - 1) #Uso de random para generar una fruta en una coordenada x al azar.
        self.y = random.randint(0,cell_number - 1) #Uso de random para generar una fruta en una coordenada y al azar.
        self.pos = Vector2(self.x,self.y) #Evitar poner pygame.math implementandolo. Se hace uso de vectores para la posición. Tablero dividido en cuadros.

    # def draw_fruit(self):
    #     #Creando un rectangulo
    #     fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size)
    #     #Dibujar el rectangulo
    #     pygame.draw.rect(screen,(255,50,50),fruit_rect)

pygame.init() #Inicio del juego
cell_size = 40 #Tamaño de las celdas
cell_number = 20 #Numero de celdas
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size)) #Display surface, la ventana ejecutable.
clock = pygame.time.Clock() #Para controlar tiempos en el ciclo.

# fruit = Fruit() 
snake = Snake()

SCREEN_UPDATE = pygame.USEREVENT #Eventos en mayusculas. Un evento que podemos rastrear.
pygame.time.set_timer(SCREEN_UPDATE,150) #Actualización cada 150 milisegundos.
#Ciclo de juego.
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Boton de cerrar
            #Salir de la ventana
            pygame.quit()
            sys.exit() #Implementado al principio con el import
        if event.type == SCREEN_UPDATE: #Mover a la serpiente.
            snake.move_snake() 
    
    screen.fill((205, 255, 45)) #Fondo 
    # fruit.draw_fruit()
    snake.draw_snake()
    pygame.display.update()
    clock.tick(60) #Fotogramas por segundo.
