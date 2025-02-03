import pygame  # Импортируем библиотеку Pygame для разработки игр
# from main import GAME_WINDOW, PURPLE  # Импортируем окно и цвет


class Level2:
    def __init__(self, game_window, purple):
        self.GAME_WINDOW = game_window  # передаем это значение
        self.flag = False  # Флаг активности уровня
        self.PURPLE = purple  # цвет тоже
    # Метод для проверки столкновений тела змеи с преградами
    def checkcol(self, body):
        if 100 <= body[0][0] < 550 and \
                (body[0][1] == 200 and body[1][1] == 150 or body[0][1] == 150 and body[1][1] == 200):
            return True
        if (body[0][0] == 600 and body[1][0] == 650 or body[0][0] == 650 and body[1][0] == 600) and \
                100 <= body[0][1] < 250:
            return True
        if 100 <= body[0][0] < 350 and \
                (body[0][1] == 600 and body[1][1] == 550 or body[0][1] == 550 and body[1][1] == 600):
            return True
        if (body[0][0] == 300 and body[1][0] == 350 or body[0][0] == 350 and body[1][0] == 300) and \
                500 <= body[0][1] < 600:
            return True
        if (body[0][0] == 650 and body[1][0] == 700 or body[0][0] == 700 and body[1][0] == 650) and \
                500 < body[0][1] <= 850:
            return True

    def activate(self):
        self.flag = True  # Устанавливаем флаг активности уровня

    def deactivate(self):
        self.flag = False  # Устанавливаем флаг активности уровня

    # Метод для проверки активности уровня
    def isactive(self):
        return self.flag

    # Метод для отрисовки препятствий уровня 2
    def render(self):
        game_window = self.GAME_WINDOW
        purple = self.PURPLE
        pygame.draw.rect(game_window, purple,
                         pygame.Rect(100, 195, 455, 10))  # Рисуем первое препятствие
        pygame.draw.rect(game_window, purple,
                         pygame.Rect(645, 100, 10, 155))  # Рисуем второе препятствие
        pygame.draw.rect(game_window, purple,
                         pygame.Rect(100, 595, 255, 10))  # Рисуем третье препятствие
        pygame.draw.rect(game_window, purple,
                         pygame.Rect(345, 495, 10, 105))  # Рисуем четвёртое препятствие
        pygame.draw.rect(game_window, purple,
                         pygame.Rect(695, 545, 10, 305))  # Рисуем пятое препятствие