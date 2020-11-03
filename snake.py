import pygame, random

def randomizeFood(): #A function to randomize the spawn location of the food
    x = 0
    y = 0
    while x == 0 or y == 0 or x == 59 or y == 59:
        x = random.randint(0, 59)
        y = random.randint(0, 59)
    return (x*10, y*10)

def eatFood(snakePos, foodPos): #Verify if encountered a food
    if(snakePos[0] == foodPos):
        return True

def gameOver(): #verify if it collided with itself or the borders
    for part in snakePos[1:]:
        if snakePos[0] == part:
            return True
    if snakePos[0][0] >= 600 or snakePos[0][1] >= 600 or snakePos[0][0] < 0 or snakePos[0][1] < 0:
        return True

clock = pygame.time.Clock()
direction = 'Right'

pygame.init()

screen = pygame.display.set_mode( (600, 600) )
pygame.display.set_caption('Snake Game')

#Creating snake position and size of each part
snakePos = [(200, 200), (210, 200)]
snakePart = pygame.Surface((10, 10)) 
snakePart.fill((42, 161, 46))

#Creating borders
borderX1Color = pygame.Surface((600, 10))
borderX1Color.fill((255, 255, 255))

borderY1Color = pygame.Surface((10, 600))
borderY1Color.fill((255, 255, 255))

borderX2Color = pygame.Surface((600, 10))
borderX2Color.fill((255, 255, 255))

borderY2Color = pygame.Surface((10, 600))
borderY2Color.fill((255, 255, 255))


foodPos = randomizeFood()
foodRespawn = (0, 0)

foodBlock = pygame.Surface((10, 10))
foodBlock.fill((255, 0, 0))

while True:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill((0, 0, 0)) #Cleaning the screen

    for part in snakePos:
        screen.blit(snakePart, part) #Painting the snake in the screen

    for i in range(len(snakePos) - 1, 0, -1): #Each part of the snake assumes the position of the one ahead of it, making the body follow the head
        snakePos[i] = (snakePos[i-1][0], snakePos[i-1][1])

    if event.type == pygame.KEYDOWN: #Verify direction
        if event.key == pygame.K_UP and direction != 'Down':
            direction = 'Up'
        if event.key == pygame.K_DOWN and direction != 'Up':
            direction = 'Down'
        if event.key == pygame.K_LEFT and direction != 'Right':
            direction = 'Left'
        if event.key == pygame.K_RIGHT and direction != 'Left':
            direction = 'Right'


    #Moves the snake according to the direction selected
    if direction == 'Up':
        snakePos[0] = (snakePos[0][0], snakePos[0][1] - 10)
    if direction == 'Down':
        snakePos[0] = (snakePos[0][0], snakePos[0][1] + 10)
    if direction == 'Right':
        snakePos[0] = (snakePos[0][0] + 10, snakePos[0][1])
    if direction == 'Left':
        snakePos[0] = (snakePos[0][0] - 10, snakePos[0][1])

    screen.blit(foodBlock, foodPos) #Inserts a food in a random location

    #Creates border
    screen.blit(borderX1Color, [0,0])
    screen.blit(borderY1Color, [0,0])
    screen.blit(borderX2Color, [0,590])
    screen.blit(borderY2Color, [590, 0])

    if eatFood(snakePos, foodPos):
        snakePos.append((700, 700))
        foodPos = randomizeFood()

    if gameOver():
        pygame.quit()


    pygame.display.update()


