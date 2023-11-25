import pygame, sys,random
from pygame.math import Vector2
import cv2
# from pyvidplayer import Video

class Snake:
    def __init__(self): #Inicio
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)] #El cuerpo de la serpiente.
        self.direction = Vector2(1,0) #Input del jugador.
        self.new_block = False
        self.speed = 150  # Velocidad inicial en milisegundos

        self.head_up = pygame.image.load('Graficos/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('Graficos/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('Graficos/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('Graficos/head_left.png').convert_alpha()
		
        self.tail_up = pygame.image.load('Graficos/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('Graficos/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('Graficos/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('Graficos/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load('Graficos/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('Graficos/body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load('Graficos/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('Graficos/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('Graficos/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('Graficos/body_bl.png').convert_alpha()

    def draw_snake(self): #Dibujar a la serpiente
        self.update_head_graphics()
        self.update_tail_graphics()

        for index,block in enumerate(self.body):
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)

            if index == 0:
                screen.blit(self.head,block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail,block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical,block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal,block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl,block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl,block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr,block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br,block_rect)
    
    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1,0): self.head = self.head_left
        elif head_relation == Vector2(-1,0): self.head = self.head_right
        elif head_relation == Vector2(0,1): self.head = self.head_up
        elif head_relation == Vector2(0,-1): self.head = self.head_down

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1,0): self.tail = self.tail_left
        elif tail_relation == Vector2(-1,0): self.tail = self.tail_right
        elif tail_relation == Vector2(0,1): self.tail = self.tail_up
        elif tail_relation == Vector2(0,-1): self.tail = self.tail_down


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
        screen.blit(apple,fruit_rect)
        # Dibujar el rectangulo
        # pygame.draw.rect(screen,(255,255,255),fruit_rect)

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
        self.check_fail()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]: #Detectando colision de la serpiente con la fruta
            self.fruit.randomize()
            self.snake.add_block()
            
    def check_fail(self): #Checar si pierde la serpiente tocando el borde del tablero o chocando contra ella misma.
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()

        for block in self.snake.body[1:]:
             if block == self.snake.body[0]:
                 self.game_over() 

    def game_over(self):
        pygame.quit()
        sys.exit()



pygame.init() #Inicio del juego
cell_size = 40 #Tamaño de las celdas
cell_number = 20 #Numero de celdas
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size)) #Display surface, la ventana ejecutable.
clock = pygame.time.Clock() #Para controlar tiempos en el ciclo.
apple = pygame.image.load('Graficos/fruit.png').convert_alpha() #Añadiendo gráfico al bocadillo
# fondo = pygame.image.load('Graficos/fondo.jpeg').convert_alpha()
fondo_movimiento = cv2.VideoCapture("Graficos/fondo_movimiento.mp4")



SCREEN_UPDATE = pygame.USEREVENT #Eventos en mayusculas. Un evento que podemos rastrear.
pygame.time.set_timer(SCREEN_UPDATE,150) #Actualización cada 150 milisegundos.

main_game = Main()

#Ciclo de juego.
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Boton de cerrar
            #Salir de la ventana
            # vid.close()
            pygame.quit()
            sys.exit() #Implementado al principio con el import
        if event.type == SCREEN_UPDATE: #Mover a la serpiente.
            main_game.update()
        if event.type == pygame.KEYDOWN: #Presionar cualquier tecla.
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)

    # vid.draw(screen, (0, 0))
    ret, frame = fondo_movimiento.read()
    if not ret:
        fondo_movimiento.set(cv2.CAP_PROP_POS_FRAMES, 0)
        _, frame = fondo_movimiento.read()
    fondo_movimiento_surf = pygame.image.frombuffer(frame.tobytes(), frame.shape[1::-1], "BGR")
    screen.blit(fondo_movimiento_surf, (0, 0)) #Fondo 
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60) #Fotogramas por segundo.
