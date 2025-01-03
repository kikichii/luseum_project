import pygame
import time
import random


class Snake:
    def __init__(self):
        self.snake_pos = [250, 100]
        self.snake_body = [[250, 100],
                      [200, 100],
                      [150, 100],
                      [100, 100]]

    def pos(self):
        return self.snake_pos

    def body(self):
        return self.snake_body

    def render(self, direction):
        if direction == 'UP':
            self.snake_pos[1] -= 50
        if direction == 'DOWN':
            self.snake_pos[1] += 50
        if direction == 'LEFT':
            self.snake_pos[0] -= 50
        if direction == 'RIGHT':
            self.snake_pos[0] += 50
        self.snake_body.insert(0, list(self.snake_pos))
        for pos in self.snake_body:
            pygame.draw.rect(game_window, pink,
                             pygame.Rect(pos[0], pos[1], 50, 50))



class Fruit:
    def __init__(self, fruit_spawn):
        self.fruit_spawn = fruit_spawn
        self.fruit_pos = [random.randrange(100, window_x - 150, 50),
                          random.randrange(100, window_y - 150, 50)]

    def isspawn(self):
        if self.fruit_spawn:
            return True
        else:
            return False

    def spawn(self, tf):
        self.fruit_spawn = tf

    def getpos(self):
        return self.fruit_pos

    def setpos(self, x, y):
        self.fruit_pos = [x, y]

    def render(self):
        pygame.draw.rect(game_window, red, pygame.Rect(
            fruit.getpos()[0], fruit.getpos()[1], 50, 50))

class Level1:
    def __init__(self):
        self.active = False

    def isactive(self):
        return self.active

    def active(self, tf):
        self.active = tf

    def render(self):
        pass


def show_score(choice, color, font, size):
    # creating font object score_font
    score_font = pygame.font.SysFont(font, size)
    # create the display surface object
    # score_surface
    score_surface = score_font.render('Score : ' + str(score), True, color)
    # create a rectangular object for the text
    # surface object
    score_rect = score_surface.get_rect()
    # displaying text
    game_window.blit(score_surface, score_rect)


def game_over():
    # creating font object my_font
    my_font = pygame.font.SysFont('Corbel', 50)
    # creating a text surface on which text
    # will be drawn
    game_over_surface = my_font.render(
        'Apples:' + str(score), True, white)
    # create a rectangular object for the text
    # surface object
    game_over_rect = game_over_surface.get_rect()
    # setting position of the text
    game_over_rect.midtop = (window_x / 2, window_y / 4)
    # blit will draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    # after 2 seconds we will quit the program
    time.sleep(2)
    # deactivating pygame library
    pygame.quit()
    # quit the program
    quit()


if __name__ == '__main__':
    pygame.init()
    size = window_x, window_y = 850, 850
    white = pygame.Color(255, 255, 255)
    red = pygame.Color(255, 0, 0)
    pink = pygame.Color(255, 80, 155)
    pygame.display.set_caption('Snake')
    game_window = pygame.display.set_mode((window_x, window_y))
    fps = pygame.time.Clock()
    snake = Snake()
    fruit = Fruit(True)
    direction = 'RIGHT'
    change_to = direction
    score = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'
        if snake.pos()[0] == fruit.getpos()[0] and snake.pos()[1] == fruit.getpos()[1]:
            score += 1
            fruit.spawn(False)
        else:
            snake.body().pop()
        if not fruit.isspawn():
            fruit.setpos(random.randrange(100, window_x - 100, 50),
                          random.randrange(100, window_y - 100, 50))
        fruit.spawn(True)
        game_window.fill((15, 220, 30))
        pygame.draw.rect(game_window, pygame.Color(10, 150, 20), pygame.Rect(100, 100, window_x - 200, window_y - 200))
        snake.render(direction)
        fruit.render()
        if snake.pos()[0] < 100 or snake.pos()[0] > window_x - 150:
            game_over()
        if snake.pos()[1] < 100 or snake.pos()[1] > window_y - 150:
            game_over()
        for block in snake.body()[1:]:
            if snake.pos()[0] == block[0] and snake.pos()[1] == block[1]:
                game_over()
        pygame.display.update()
        fps.tick(7)
