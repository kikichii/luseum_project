import pygame  # Импортируем библиотеку Pygame для разработки игр
# from main import GAME_WINDOW, PURPLE  # Импортируем окно и цвет


class Level3:
    def __init__(self, game_window, purple):
        self.flag = False  # Флаг активности уровня
        self.game_window = game_window  # передаем это значение
        self.PURPLE = purple  # цвет тоже

    # Метод для проверки столкновений тела змеи с преградами уровня 3
    def checkcol(self, body):
        if 100 <= body[0][0] < 250 and 100 <= body[0][1] < 250:
            return True
        if 250 <= body[0][0] < 400 and 200 <= body[0][1] < 250:
            return True
        if 600 <= body[0][0] < 750 and 300 <= body[0][1] < 350:
            return True
        if 650 <= body[0][0] < 850 and 350 <= body[0][1] < 400:
            return True
        if 100 <= body[0][0] < 450 and 500 <= body[0][1] < 550:
            return True
        if 350 <= body[0][0] < 450 and 550 <= body[0][1] < 600:
            return True
        if 400 <= body[0][0] < 450 and 600 <= body[0][1] < 650:
            return True
        if 650 <= body[0][0] < 750 and 650 <= body[0][1] < 700:
            return True
        if 600 <= body[0][0] < 750 and 700 <= body[0][1] < 750:
            return True
        if 700 <= body[0][0] < 750 and 750 <= body[0][1] < 850:
            return True

    # Метод для проверки активности уровня
    def isactive(self):
        return self.flag

    # Метод для отрисовки препятствий уровня 3
    def render(self):
        game_window = self.game_window
        purple = self.PURPLE
        pygame.draw.rect(game_window, purple,
                         pygame.Rect(100, 100, 150, 150))  # Рисуем первое препятствие
        pygame.draw.rect(game_window, purple,
                         pygame.Rect(250, 200, 150, 50))  # Рисуем второе препятствие
        pygame.draw.rect(game_window, purple,
                         pygame.Rect(600, 300, 150, 50))  # Рисуем третье препятствие
        pygame.draw.rect(game_window, purple,
                         pygame.Rect(650, 350, 200, 50))  # Рисуем четвёртое препятствие
        pygame.draw.rect(game_window, purple,
                         pygame.Rect(100, 500, 350, 50))  # Рисуем пятого препятствие
        pygame.draw.rect(game_window, purple,
                         pygame.Rect(350, 550, 100, 50))  # Рисуем шестое препятствие
        pygame.draw.rect(game_window, purple,
                         pygame.Rect(400, 600, 50, 50))  # Рисуем седьмое препятствие
        pygame.draw.rect(game_window, purple,
                         pygame.Rect(650, 650, 100, 50))  # Рисуем восьмое препятствие
        pygame.draw.rect(game_window, purple,
                         pygame.Rect(600, 700, 150, 50))  # Рисуем девятое препятствие
        pygame.draw.rect(game_window, purple,
                         pygame.Rect(700, 750, 50, 100))  # Рисуем десятую препятствие
        self.Flag = True  # Устанавливаем флаг активности уровня