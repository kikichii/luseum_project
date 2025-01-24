import pygame  # Импортируем библиотеку Pygame для разработки игр
import time  # Импортируем библиотеку time для работы со временем
import random  # Импортируем библиотеку random для генерации случайных чисел
import os  # Импортируем библиотеку os для работы с операционной системой
import sys  # Импортируем библиотеку sys для доступа к параметрам и функциям Python
import level2  # Импортируем второй уровень
import level3  # Импортируем третий уровень


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
            pygame.draw.rect(GAME_WINDOW, PINK,
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
        GAME_WINDOW.blit(apple, (fruit.getpos()[0], fruit.getpos()[1]))  # Отрисовка фрукта на экране


# Функция для загрузки изображений
def load_image(name, colorkey=None):
    fullname = os.path.join('../data', name)  # Полный путь к изображению
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
    GAME_WINDOW.blit(score_surface, score_rect)


# Функция, срабатывающая при окончании игры
def game_over():
    # Создаем объект шрифта для отображения текста "Game Over"
    my_font = pygame.font.SysFont('Corbel', 50)
    # Создаем поверхность для отображения текста счёта
    game_over_surface = my_font.render(
        'Apples:' + str(score), True, WHITE)
    # Создаем прямоугольный объект для текста
    game_over_rect = game_over_surface.get_rect()
    # Устанавливаем позицию текста на экране
    game_over_rect.midtop = (window_x / 2, window_y / 4)
    # Отрисовка текста на экране
    GAME_WINDOW.blit(game_over_surface, game_over_rect)
    pygame.display.flip()  # Обновляем экран
    time.sleep(2)  # Задержка перед выходом
    pygame.quit()  # Деактивируем Pygame
    quit()  # Завершаем программу


# Главный блок программы
if __name__ == '__main__':
    pygame.init()  # Инициализируем Pygame
    size = window_x, window_y = 950, 950  # Устанавливаем размер окна
    WHITE = pygame.Color(255, 255, 255)  # Определяем цвет белый
    RED = pygame.Color(255, 0, 0)  # Определяем цвет красный
    PINK = pygame.Color(255, 106, 170)  # Определяем цвет розовый
    ORANGE = pygame.Color(255, 135, 57)  # Определяем цвет оранжевый
    PURPLE = pygame.Color(117, 106, 255)  # Определяем цвет фиолетовый
    pygame.display.set_caption('Snake')  # Устанавливаем заголовок окна
    GAME_WINDOW = pygame.display.set_mode((window_x, window_y))  # Создаем игровое окно
    fps = pygame.time.Clock()  # Создаем объект для управления частотой кадров
    snake = Snake()  # Создаем объект змеи
    fruit = Fruit(True)  # Создаем объект фрукта
    level2 = level2.Level2(GAME_WINDOW, PURPLE)  # Создаем объект для второго уровня
    level3 = level3.Level3(GAME_WINDOW, PURPLE)  # Создаем объект для третьего уровня
    all_sprites = pygame.sprite.Group()  # Создаем группу для всех спрайтов
    cur = pygame.sprite.Sprite(all_sprites)  # Создаем спрайт для фона
    cur.image = load_image("background_image.png")  # Загружаем изображение фона
    cur.rect = cur.image.get_rect()  # Получаем прямоугольник для спрайта фона
    cur.rect.topleft = 100, 100  # Устанавливаем позицию спрайта фона
    DIRECTION = 'RIGHT'  # Устанавливаем начальное направление движения змеи
    change_to = DIRECTION  # Переменная для изменения направления
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
        if change_to == 'UP' and DIRECTION != 'DOWN':
            DIRECTION = 'UP'  # Меняем направление на вверх
        if change_to == 'DOWN' and DIRECTION != 'UP':
            DIRECTION = 'DOWN'  # Меняем направление на вниз
        if change_to == 'LEFT' and DIRECTION != 'RIGHT':
            DIRECTION = 'LEFT'  # Меняем направление на влево
        if change_to == 'RIGHT' and DIRECTION != 'LEFT':
            DIRECTION = 'RIGHT'  # Меняем направление на вправо

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
        GAME_WINDOW.fill((168, 255, 136))  # Заполняем игровой экран цветом
        all_sprites.draw(GAME_WINDOW)  # Отрисовка всех спрайтов
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

        snake.render(DIRECTION)  # Отрисовка змеи

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