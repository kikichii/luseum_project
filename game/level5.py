import pygame  # Импортируем библиотеку Pygame для разработки игр
# from main import GAME_WINDOW, PURPLE  # Импортируем окно и цвет


class Level5:
    def __init__(self, game_window, purple):
        self.flag = False  # Флаг активности уровня
        self.game_window = game_window  # передаем это значение
        self.PURPLE = purple  # цвет тоже

    # Метод для проверки столкновений тела змеи с преградами уровня 3
    def checkcol(self, body):
        if 100 <= body[0][0] < 300 and 200 <= body[0][1] < 250:
            return True
        if 250 <= body[0][0] < 400 and 250 <= body[0][1] < 300:
            return True
        if 100 <= body[0][1] < 450 and \
                (body[0][0] == 550 and body[1][0] == 600 or body[0][0] == 600 and body[1][0] == 550):
            return True
        if 750 <= body[0][0] < 850 and \
                (body[0][1] == 200 and body[1][1] == 250 or body[0][1] == 250 and body[1][1] == 200):
            return True
        if 100 <= body[0][0] < 350 and \
                (body[0][1] == 400 and body[1][1] == 450 or body[0][1] == 450 and body[1][1] == 400):
            return True
        if 100 <= body[0][0] < 250 and 700 <= body[0][1] < 750:
            return True
        if 100 <= body[0][0] < 150 and 750 <= body[0][1] < 850:
            return True
        if 250 <= body[0][0] < 450 and \
                (body[0][1] == 700 and body[1][1] == 650 or body[0][1] == 650 and body[1][1] == 700):
            return True
        if 500 <= body[0][1] < 700 and \
                (body[0][0] == 500 and body[1][0] == 450 or body[0][0] == 450 and body[1][0] == 500):
            return True
        if 600 <= body[0][0] < 750 and 550 <= body[0][1] < 600:
            return True
        if 600 <= body[0][0] < 650 and 550 <= body[0][1] < 750:
            return True
        if 600 <= body[0][0] < 850 and 700 <= body[0][1] < 750:
            return True

    def activate(self):
        self.flag = True  # Устанавливаем флаг активности уровня

    def deactivate(self):
        self.flag = False  # Устанавливаем флаг активности уровня

    # Метод для проверки активности уровня
    def isactive(self):
        return self.flag

    # Метод для отрисовки препятствий уровня 5
    def render(self):
        game_window = self.game_window
        purple = self.PURPLE
        pygame.draw.rect(game_window, purple,
                         pygame.Rect(100, 200, 200, 50))  # Рисуем первое препятствие
        pygame.draw.rect(game_window, purple,
                         pygame.Rect(250, 250, 150, 50))  # Рисуем второе препятствие
        pygame.draw.rect(game_window, purple,
                         pygame.Rect(595, 100, 10, 355))  # Рисуем третье препятствие
        pygame.draw.rect(game_window, purple,
                         pygame.Rect(745, 245, 105, 10))  # Рисуем четвёртое препятствие
        pygame.draw.rect(game_window, purple,
                         pygame.Rect(100, 445, 255, 10))  # Рисуем пятого препятствие
        pygame.draw.rect(game_window, purple,
                         pygame.Rect(445, 495, 10, 210))  # Рисуем шестое препятствие
        pygame.draw.rect(game_window, purple,
                         pygame.Rect(100, 695, 355, 10))  # Рисуем седьмое препятствие
        pygame.draw.rect(game_window, purple,
                         pygame.Rect(100, 700, 150, 50))  # Рисуем восьмое препятствие
        pygame.draw.rect(game_window, purple,
                         pygame.Rect(100, 750, 50, 100))  # Рисуем девятое препятствие
        pygame.draw.rect(game_window, purple,
                         pygame.Rect(600, 550, 150, 50))  # Рисуем десятое препятствие
        pygame.draw.rect(game_window, purple,
                         pygame.Rect(600, 600, 50, 100))
        pygame.draw.rect(game_window, purple,
                         pygame.Rect(600, 700, 250, 50))
        pygame.draw.circle(game_window, (255, 255, 0),
                           (725, 575), 8)
        pygame.draw.circle(game_window, (255, 255, 255),
                           (727, 572), 3)