import pygame, sys,random
from pygame.math import Vector2


class Snake:
    def __init__(self): #Inicio
        self.body = [Vector2(5,10),Vector2(6,10),Vector2(7,10)] #El cuerpo de la serpiente.
        self.direction = Vector2(1,0) #Input del jugador.
        self.new_block = False
        self.speed = 150  # Velocidad inicial en milisegundos

    def draw_snake(self): #Dibujar a la serpiente
        for block in self.body:
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            #Creando el rectangulo
            block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)
            #Dibujando el rectangulo
            pygame.draw.rect(screen,(255,217,25),block_rect)

    def move_snake(self): #Mover a la serpiente
        if self.new_block == True:
            body_copy = self.body[:] #No se borra el ultimo elemento pero se sigue añadiendo un bloque.
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
            if self.speed >= 60:
                self.speed -= 2 #Aumentando la velocidad
                pygame.time.set_timer(SCREEN_UPDATE,self.speed)
            else:
                pygame.time.set_timer(SCREEN_UPDATE,self.speed)

        else:   
            body_copy = self.body[:-1] #Eliminar el ultimo bloque de la serpiente.
            body_copy.insert(0,body_copy[0] + self.direction) #Nuevo cuerpo
            self.body = body_copy[:]

    def add_block(self): #Añadir nuevo bloque a la serpiente
        self.new_block = True

class Fruit:
    def __init__(self): #Inicio
        #Crear un cuadro, usando y, x position.
        self.randomize()

    def draw_fruit(self):
        # Creando un rectangulo
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size)
        # Dibujar el rectangulo
        pygame.draw.rect(screen,(255,255,255),fruit_rect)

    def randomize(self):
        self.x = random.randint(0,cell_number - 1) #Uso de random para generar una fruta en una coordenada x al azar.
        self.y = random.randint(0,cell_number - 1) #Uso de random para generar una fruta en una coordenada y al azar.
        self.pos = Vector2(self.x,self.y) #Evitar poner pygame.math implementandolo. Se hace uso de vectores para la posición. Tablero dividido en cuadros.

class Main:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()

    def update(self):
        self.snake.move_snake()
        self.check_collision()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]: #Detectando colision de la serpiente con la fruta
            self.fruit.randomize()
            self.snake.add_block()

pygame.init() #Inicio del juego
cell_size = 40 #Tamaño de las celdas
cell_number = 20 #Numero de celdas
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size)) #Display surface, la ventana ejecutable.
clock = pygame.time.Clock() #Para controlar tiempos en el ciclo.

SCREEN_UPDATE = pygame.USEREVENT #Eventos en mayusculas. Un evento que podemos rastrear.
pygame.time.set_timer(SCREEN_UPDATE,150) #Actualización cada 150 milisegundos.

main_game = Main()

#Ciclo de juego.
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Boton de cerrar
            #Salir de la ventana
            pygame.quit()
            sys.exit() #Implementado al principio con el import
        if event.type == SCREEN_UPDATE: #Mover a la serpiente.
            main_game.update()
        if event.type == pygame.KEYDOWN: #Presionar cualquier tecla.
            if event.key == pygame.K_UP:
                main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                main_game.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT:
                main_game.snake.direction = Vector2(1, 0)


    screen.fill((15, 22, 68)) #Fondo 
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60) #Fotogramas por segundo.
