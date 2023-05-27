import pygame
import random
pygame.init()
screen = pygame.display.set_mode((500, 500))
seg_size = 20
head_size = 25
clock = pygame.time.Clock()
current_position = [[100, 100], [80, 100], [60, 100]]
food = [(random.randint(0, 24) * 20), (random.randint(3, 24) * 20), seg_size, seg_size]
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
direction = RIGHT
def drawBoard():
    global current_position, food, direction
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, 500, 500))
    #pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(0, 270, 30, 200))
    for pos in current_position:
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(int(pos[0]), int(pos[1]), seg_size, seg_size))
    pygame.draw.circle(screen, (255, 0, 0), [int(current_position[-1][0] + 25), int(current_position[-1][1] + 25)], head_size)
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(int(food[0]), int(food[1]), seg_size, seg_size))
    if current_position[-1][0] > 500 or current_position[-1][0] < 0 or current_position[-1][1] > 500 or current_position[-1][1] < 0:
        font = pygame.font.Font(None, 36)
        text = font.render("GAME OVER", 1, (255, 255, 255))
        text_rect = text.get_rect(center=(250, 250))
        screen.blit(text, text_rect)
        pygame.display.update()
        pygame.time.wait(2000)
        direction = RIGHT
        current_position.clear()
        current_position.append([100, 100])
        current_position.append([80, 100])
        current_position.append([60, 100])
        food[0] = (random.randint(0, 24) * 20)
        food[1] = (random.randint(3, 24) * 20)
    pygame.display.flip()
    if current_position[-1] in current_position[:-1]:
        font = pygame.font.Font(None, 36)
        text = font.render("GAME OVER", 1, (255, 255, 255))
        text_rect = text.get_rect(center=(250, 250))
        screen.blit(text, text_rect)
        pygame.display.update()
        pygame.time.wait(2000)
        direction = RIGHT
        current_position.clear()
        current_position.append([100, 100])
        current_position.append([80, 100])
        current_position.append([60, 100])
        food[0] = (random.randint(0, 24) * 20)
        food[1] = (random.randint(3, 24) * 20)
while True:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != DOWN:
                direction = UP
            elif event.key == pygame.K_DOWN and direction != UP:
                direction = DOWN
            elif event.key == pygame.K_LEFT and direction != RIGHT:
                direction = LEFT
            elif event.key == pygame.K_RIGHT and direction != LEFT:
                direction = RIGHT
    if direction == RIGHT:
        current_position.append([current_position[-1][0] + seg_size, current_position[-1][1]])
    elif direction == LEFT:
        current_position.append([current_position[-1][0] - seg_size, current_position[-1][1]])
    elif direction == UP:
        current_position.append([current_position[-1][0], current_position[-1][1] - seg_size])
    elif direction == DOWN:
        current_position.append([current_position[-1][0], current_position[-1][1] + seg_size])
    if current_position[-1][0] == food[0] and current_position[-1][1] == food[1]:
        food = [(random.randint(0, 24) * 20), (random.randint(3, 24) * 20), seg_size, seg_size]
    else:
        current_position.pop(0)
    drawBoard()
    if direction == RIGHT and not current_position:
        direction = RIGHT
        current_position.append([100, 100])
        current_position.append([80, 100])
        current_position.append([60, 100])
        food[0] = (random.randint(0, 24) * 20)
        food[1] = (random.randint(3, 24) * 20)
    pygame.display.update()
    if current_position[-1][0] > 500 or current_position[-1][0] < 0 or current_position[-1][1] > 500 or current_position[-1][1] < 0:
        font = pygame.font.Font(None, 36)
        text = font.render("GAME OVER", 1, (255, 255, 255))
        text_rect = text.get_rect(center=(250, 250))
        screen.blit(text, text_rect)
        pygame.display.update()
        pygame.time.wait(2000)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                direction = RIGHT
                current_position.clear()
                current_position.append([100, 100])
                current_position.append([80, 100])
                current_position.append([60, 100])
                food[0] = (random.randint(0, 24) * 20)
                food[1] = (random.randint(3, 24) * 20)