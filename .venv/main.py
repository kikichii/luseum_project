import pygame  # Импортируем библиотеку Pygame для разработки игр
import time  # Импортируем библиотеку time для работы со временем
import random  # Импортируем библиотеку random для генерации случайных чисел
import os  # Импортируем библиотеку os для работы с операционной системой
import sys  # Импортируем библиотеку sys для доступа к параметрам и функциям Python


# Класс для управления змеёй
class Snake:
    def __init__(self):
        # Инициализация позиции змеи и её тела
        self.snake_pos = [250, 100]  # Начальная позиция головы змеи
        self.snake_body = [[250, 100],  # Тело змеи как список координат
                           [200, 100],
                           [150, 100],
                           [100, 100]]

    # Метод для установки позиции змеи
    def setpos(self, x, y):
        self.snake_pos = [x, y]

    # Метод для получения текущей позиции головы змеи
    def pos(self):
        return self.snake_pos

    # Метод для получения текущего тела змеи
    def body(self):
        return self.snake_body

    # Метод для отрисовки змеи
    def render(self, direction):
        # Обновление позиции головы змея в зависимости от направления
        if direction == 'UP':
            self.snake_pos[1] -= 50
        if direction == 'DOWN':
            self.snake_pos[1] += 50
        if direction == 'LEFT':
            self.snake_pos[0] -= 50
        if direction == 'RIGHT':
            self.snake_pos[0] += 50
        # Добавление новой позиции головы в тело змеи
        self.snake_body.insert(0, list(self.snake_pos))
        # Отрисовка каждого сегмента тела змеи
        for pos in self.snake_body:
            pygame.draw.rect(game_window, pink,
                             pygame.Rect(pos[0], pos[1], 50, 50))


# Класс для управления фруктами
class Fruit:
    def __init__(self, fruit_spawn):
        self.fruit_spawn = fruit_spawn  # Определяет, нужно ли спавнить фрукт
        # Генерация случайной позиции фрукта
        self.fruit_pos = [random.randrange(100, window_x - 150, 50),
                          random.randrange(100, window_y - 150, 50)]

    # Метод проверки, спавнится ли фрукт
    def isspawn(self):
        if self.fruit_spawn:
            return True
        else:
            return False

    # Метод для установки состояния спавна фрукта
    def spawn(self, tf):
        self.fruit_spawn = tf

    # Метод для получения текущей позиции фрукта
    def getpos(self):
        return self.fruit_pos

    # Метод для установки новой позиции фрукта
    def setpos(self, x, y):
        self.fruit_pos = [x, y]

    # Метод для отрисовки фрукта на экране
    def render(self):
        apple = load_image("apple.png")  # Загрузка изображения фрукта
        game_window.blit(apple, (fruit.getpos()[0], fruit.getpos()[1]))  # Отрисовка фрукта на экране


# Класс для управления уровнем 2
class Level2:

    # Метод для проверки столкновений тела змеи с преградами
    def checkcol(self, body):
        if 100 <= body[0][0] < 550 and \
                (body[0][1] == 100 and body[1][1] == 150 or body[0][1] == 150 and body[1][1] == 100):
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

    # Метод для отрисовки препятствий уровня 2
    def render(self):
        pygame.draw.rect(game_window, purple,
                         pygame.Rect(100, 145, 455, 10))  # Рисуем первое препятствие
        pygame.draw.rect(game_window, purple,
                         pygame.Rect(645, 100, 10, 155))  # Рисуем второе препятствие
        pygame.draw.rect(game_window, purple,
                         pygame.Rect(100, 595, 255, 10))  # Рисуем третье препятствие
        pygame.draw.rect(game_window, purple,
                         pygame.Rect(345, 495, 10, 105))  # Рисуем четвёртое препятствие
        pygame.draw.rect(game_window, purple,
                         pygame.Rect(695, 545, 10, 305))  # Рисуем пятое препятствие


# Класс для управления уровнем 3
class Level3:

    def __init__(self):
        self.flag = False  # Флаг активности уровня

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


# Функция для загрузки изображений
def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)  # Полный путь к изображению
    if not os.path.isfile(fullname):  # Проверяем, существует ли файл
        print(f"Файл с изображением '{fullname}' не найден")  # Если файл не найден, выводим сообщение
        sys.exit()  # Завершаем программу
    image = pygame.image.load(fullname)  # Загружаем изображение
    return image  # Возвращаем изображение


# Функция для отображения счёта
def show_score(choice, color, font, size):
    # Создаем объект шрифта для отображения счёта
    score_font = pygame.font.SysFont(font, size)
    # Создаем поверхность для отображения текста счёта
    score_surface = score_font.render('Score : ' + str(score), True, color)
    # Создаем прямоугольный объект для текста
    score_rect = score_surface.get_rect()
    # Отображаем текст на экране
    game_window.blit(score_surface, score_rect)


# Функция, срабатывающая при окончании игры
def game_over():
    # Создаем объект шрифта для отображения текста "Game Over"
    my_font = pygame.font.SysFont('Corbel', 50)
    # Создаем поверхность для отображения текста счёта
    game_over_surface = my_font.render(
        'Apples:' + str(score), True, white)
    # Создаем прямоугольный объект для текста
    game_over_rect = game_over_surface.get_rect()
    # Устанавливаем позицию текста на экране
    game_over_rect.midtop = (window_x / 2, window_y / 4)
    # Отрисовка текста на экране
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()  # Обновляем экран
    time.sleep(2)  # Задержка перед выходом
    pygame.quit()  # Деактивируем Pygame
    quit()  # Завершаем программу


# Главный блок программы
if __name__ == '__main__':
    pygame.init()  # Инициализируем Pygame
    size = window_x, window_y = 950, 950  # Устанавливаем размер окна
    white = pygame.Color(255, 255, 255)  # Определяем цвет белый
    red = pygame.Color(255, 0, 0)  # Определяем цвет красный
    pink = pygame.Color(255, 106, 170)  # Определяем цвет розовый
    orange = pygame.Color(255, 135, 57)  # Определяем цвет оранжевый
    purple = pygame.Color(117, 106, 255)  # Определяем цвет фиолетовый
    pygame.display.set_caption('Snake')  # Устанавливаем заголовок окна
    game_window = pygame.display.set_mode((window_x, window_y))  # Создаем игровое окно
    fps = pygame.time.Clock()  # Создаем объект для управления частотой кадров
    snake = Snake()  # Создаем объект змеи
    fruit = Fruit(True)  # Создаем объект фрукта
    level2 = Level2()  # Создаем объект для второго уровня
    level3 = Level3()  # Создаем объект для третьего уровня
    all_sprites = pygame.sprite.Group()  # Создаем группу для всех спрайтов
    cur = pygame.sprite.Sprite(all_sprites)  # Создаем спрайт для фона
    cur.image = load_image("background_image.png")  # Загружаем изображение фона
    cur.rect = cur.image.get_rect()  # Получаем прямоугольник для спрайта фона
    cur.rect.topleft = 100, 100  # Устанавливаем позицию спрайта фона
    direction = 'RIGHT'  # Устанавливаем начальное направление движения змеи
    change_to = direction  # Переменная для изменения направления
    score = 0  # Начальный счёт

    # Главный игровой цикл
    while True:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Если событие выхода
                game_over()  # Вызвать функцию game_over
            if event.type == pygame.KEYDOWN:  # Если нажата клавиша
                if event.key == pygame.K_UP:  # Если нажата клавиша вверх
                    change_to = 'UP'  # Меняем направление на вверх
                if event.key == pygame.K_DOWN:  # Если нажата клавиша вниз
                    change_to = 'DOWN'  # Меняем направление на вниз
                if event.key == pygame.K_LEFT:  # Если нажата клавиша влево
                    change_to = 'LEFT'  # Меняем направление на влево
                if event.key == pygame.K_RIGHT:  # Если нажата клавиша вправо
                    change_to = 'RIGHT'  # Меняем направление на вправо

        # Проверяем и обновляем направление движения змеи
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'  # Меняем направление на вверх
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'  # Меняем направление на вниз
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'  # Меняем направление на влево
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'  # Меняем направление на вправо

        # Проверяем, не съела ли змея фрукт
        if snake.pos()[0] == fruit.getpos()[0] and snake.pos()[1] == fruit.getpos()[1]:
            score += 1  # Увеличиваем счёт
            fruit.spawn(False)  # Отключаем спавн фрукта
        else:
            snake.body().pop()  # Удаляем последний сегмент тела змеи

        # Проверяем, нужен ли новый фрукт
        if not fruit.isspawn():
            # Если активен третий уровень, генерируем фрукт с учётом препятствий
            if level3.isactive():
                x, y = random.randrange(100, window_x - 100, 50), random.randrange(100, window_y - 100, 50)
                while level3.checkcol([[x, y]]):  # Проверяем, не попадает ли фрукт в препятствие
                    x, y = random.randrange(100, window_x - 100, 50), random.randrange(100, window_y - 100, 50)
                fruit.setpos(x, y)  # Устанавливаем позицию фрукта
            else:
                # Генерация погодности для 2 уровня
                fruit.setpos(random.randrange(100, window_x - 100, 50),
                             random.randrange(100, window_y - 100, 50))

        fruit.spawn(True)  # Активируем спавн фрукта
        game_window.fill((168, 255, 136))  # Заполняем игровой экран цветом
        all_sprites.draw(game_window)  # Отрисовка всех спрайтов
        fruit.render()  # Отрисовка фрукта

        # Условия для уровня 2 и 3
        if 5 <= score < 25:
            level3.render()  # Отрисовка уровня 3
            if level3.checkcol(snake.body()):  # Проверка на столкновение
                game_over()  # Вызвать функцию game_over
        elif 2 <= score < 5:
            level2.render()  # Отрисовка уровня 2
            if level2.checkcol(snake.body()):  # Проверка на столкновение
                game_over()  # Вызвать функцию game_over

        snake.render(direction)  # Отрисовка змеи

        # Проверка границ окна
        if snake.pos()[0] < 100 or snake.pos()[0] > window_x - 150:
            game_over()  # Вызвать функцию game_over
        if snake.pos()[1] < 100 or snake.pos()[1] > window_y - 150:
            game_over()  # Вызвать функцию game_over

        # Проверка столкновений змеи с её собственным телом
        for block in snake.body()[1:]:
            if snake.pos()[0] == block[0] and snake.pos()[1] == block[1]:
                game_over()  # Вызвать функцию game_over

        pygame.display.update()  # Обновляем экран
        fps.tick(5)  # Ограничиваем количество кадров в секунду