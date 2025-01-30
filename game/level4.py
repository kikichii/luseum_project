import pygame  # Импортируем библиотеку Pygame для разработки игр
# from main import GAME_WINDOW, PURPLE  # Импортируем окно и цвет


class Level4:
    def __init__(self, game_window, purple):
        self.flag = False  # Флаг активности уровня
        self.game_window = game_window  # передаем это значение
        self.PURPLE = purple  # цвет тоже

    # Метод для проверки столкновений тела змеи с преградами уровня 3
    def checkcol(self, body):
        if 100 <= body[0][0] < 250 and 200 <= body[0][1] < 250:
            return True
        if 200 <= body[0][0] < 250 and 250 <= body[0][1] < 300:
            return True
        if 200 <= body[0][0] < 300 and 300 <= body[0][1] < 350:
            return True
        if 400 <= body[0][0] < 450 and 100 <= body[0][1] < 400:
            return True
        if 400 <= body[0][0] < 550 and 350 <= body[0][1] < 400:
            return True
        if 500 <= body[0][0] < 550 and 400 <= body[0][1] < 450:
            return True
        if 500 <= body[0][0] < 700 and 450 <= body[0][1] < 500:
            return True
        if 650 <= body[0][0] < 700 and 250 <= body[0][1] < 500:
            return True
        if 700 <= body[0][0] < 750 and 250 <= body[0][1] < 300:
            return True
        if 300 <= body[0][0] < 400 and 500 <= body[0][1] < 550:
            return True
        if 100 <= body[0][0] < 350 and 550 <= body[0][1] < 600:
            return True
        if 300 <= body[0][0] < 350 and 600 <= body[0][1] < 650:
            return True
        if 300 <= body[0][0] < 450 and 650 <= body[0][1] < 700:
            return True
        if 400 <= body[0][0] < 450 and 700 <= body[0][1] < 750:
            return True
        if 600 <= body[0][0] < 650 and 600 <= body[0][1] < 650:
            return True
        if 600 <= body[0][0] < 750 and 650 <= body[0][1] < 700:
            return True
        if 700 <= body[0][0] < 750 and 700 <= body[0][1] < 850:
            return True

    def activate(self):
        self.flag = True  # Устанавливаем флаг активности уровня

    def deactivate(self):
        self.flag = True  # Устанавливаем флаг активности уровня

    # Метод для проверки активности уровня
    def isactive(self):
        return self.flag

    # Метод для отрисовки препятствий уровня 3
    def render(self):
        game_window = self.game_window
        purple = self.PURPLE
        pygame.draw.rect(game_window, purple,
                         pygame.Rect(100, 200, 150, 50))  # Рисуем первое препятствие
        pygame.draw.rect(game_window, purple,
                         pygame.Rect(200, 250, 50, 50))  # Рисуем второе препятствие
        pygame.draw.rect(game_window, purple,
                         pygame.Rect(200, 300, 100, 50))  # Рисуем третье препятствие
        pygame.draw.rect(game_window, purple,
                         pygame.Rect(400, 100, 50, 250))  # Рисуем четвёртое препятствие
        pygame.draw.rect(game_window, purple,
                         pygame.Rect(400, 350, 150, 50))  # Рисуем пятого препятствие
        pygame.draw.rect(game_window, purple,
                         pygame.Rect(500, 400, 50, 50))  # Рисуем шестое препятствие
        pygame.draw.rect(game_window, purple,
                         pygame.Rect(500, 450, 200, 50))  # Рисуем седьмое препятствие
        pygame.draw.rect(game_window, purple,
                         pygame.Rect(650, 250, 50, 200))  # Рисуем восьмое препятствие
        pygame.draw.rect(game_window, purple,
                         pygame.Rect(700, 250, 50, 50))  # Рисуем девятое препятствие
        pygame.draw.rect(game_window, purple,
                         pygame.Rect(100, 550, 250, 50))  # Рисуем десятую препятствие
        pygame.draw.rect(game_window, purple,
                         pygame.Rect(300, 500, 100, 50))
        pygame.draw.rect(game_window, purple,
                         pygame.Rect(300, 600, 50, 50))
        pygame.draw.rect(game_window, purple,
                         pygame.Rect(300, 650, 150, 50))
        pygame.draw.rect(game_window, purple,
                         pygame.Rect(400, 700, 50, 50))
        pygame.draw.rect(game_window, purple,
                         pygame.Rect(600, 600, 50, 50))
        pygame.draw.rect(game_window, purple,
                         pygame.Rect(600, 650, 150, 50))
        pygame.draw.rect(game_window, purple,
                         pygame.Rect(700, 700, 50, 150))
        pygame.draw.circle(game_window, (255, 255, 0),
                           (715, 265), 8)
        pygame.draw.circle(game_window, (255, 255, 255),
                           (718, 262), 3)
