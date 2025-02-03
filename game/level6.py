import pygame

class Level6:
    def __init__(self, game_window, color):
        self.flag = False  # Флаг активности уровня
        self.game_window = game_window  # Окно игры
        self.color = color  # Цвет стен

    # Метод для проверки столкновений тела змеи с преградами уровня 6
    def checkcol(self, body):
        # Координаты стен на уровне
        walls = [
            (100, 100, 400, 300),
            (400, 100, 850, 150),
            (500, 250, 850, 350),
            (350, 300, 400, 550),
            (400, 450, 700, 550),
            (800, 350, 850, 850),
            (600, 550, 700, 700),
            (500, 800, 800, 850),
            (250, 650, 500, 850),
            (100, 300, 250, 850)
        ]

        # Проверка столкновений с каждой стеной
        for wall in walls:
            wall_rect = pygame.Rect(wall)
            if wall_rect.collidepoint(body[0][0], body[0][1]):
                return True
        return False

    # Метод для активации уровня
    def activate(self):
        self.flag = True

    # Метод для деактивации уровня
    def deactivate(self):
        self.flag = False

    # Метод для проверки активности уровня
    def isactive(self):
        return self.flag

    # Метод для отрисовки препятствий уровня 6
    def render(self):
        # Отрисовка стен
        walls = [
            (100, 100, 400, 300),
            (400, 100, 850, 150),
            (500, 250, 850, 350),
            (350, 300, 400, 550),
            (400, 450, 700, 550),
            (800, 350, 850, 850),
            (600, 550, 700, 700),
            (500, 800, 800, 850),
            (250, 650, 500, 850),
            (100, 300, 250, 850)
        ]

        for wall in walls:
            pygame.draw.rect(self.game_window, self.color, pygame.Rect(wall))