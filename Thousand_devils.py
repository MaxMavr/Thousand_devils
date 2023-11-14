# import math
# import time
import random
import time
from typing import Any

import pygame

# Нужно сделать:
# 1) починить выбор клеток (Иногда не выбираются клетки после стрелок)
# {Функции: check_step, check_step_arrow}

window_height = 800
window_width = window_height * 16 / 9
fps = 60

scope = 50
place_y = 100
place_x = 300
holdup = 0.17

# Цвета
white = (255, 255, 255)
black = (0, 0, 0)
mark = (139, 0, 139, 255/2)
select = (255, 255, 255, 255/1.5)
out = (128, 128, 128)
# dark_blue_a = (0, 0, 139, 255/2)
# dark_blue = (0, 0, 139, 255)
# deep_pink_a = (255, 20, 147, 255/2)


pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)

# Загрузка изображений
empty1 = pygame.image.load("IMG/empty1.png").convert()
empty2 = pygame.image.load("IMG/empty2.png").convert()
empty3 = pygame.image.load("IMG/empty3.png").convert()
empty4 = pygame.image.load("IMG/empty4.png").convert()
arrow1 = pygame.image.load("IMG/arrow1.png").convert()
arrow2 = pygame.image.load("IMG/arrow2.png").convert()
arrow3 = pygame.image.load("IMG/arrow3.png").convert()
arrow4 = pygame.image.load("IMG/arrow4.png").convert()
arrow5 = pygame.image.load("IMG/arrow5.png").convert()
arrow6 = pygame.image.load("IMG/arrow6.png").convert()
arrow7 = pygame.image.load("IMG/arrow7.png").convert()
horse = pygame.image.load("IMG/horse.png").convert()
turntable2 = pygame.image.load("IMG/turntable2.png").convert()
turntable3 = pygame.image.load("IMG/turntable3.png").convert()
turntable4 = pygame.image.load("IMG/turntable4.png").convert()
turntable5 = pygame.image.load("IMG/turntable5.png").convert()
ice = pygame.image.load("IMG/ice.png").convert()
trap = pygame.image.load("IMG/trap.png").convert()
crocodile = pygame.image.load("IMG/crocodile.png").convert()
ogre = pygame.image.load("IMG/ogre.png").convert()
fortress = pygame.image.load("IMG/fortress.png").convert()
aborigine = pygame.image.load("IMG/aborigine.png").convert()
gold = pygame.image.load("IMG/gold.png").convert()
gold1 = pygame.image.load("IMG/gold1.png").convert()
gold2 = pygame.image.load("IMG/gold2.png").convert()
gold3 = pygame.image.load("IMG/gold3.png").convert()
gold4 = pygame.image.load("IMG/gold4.png").convert()
gold5 = pygame.image.load("IMG/gold5.png").convert()
swearword = pygame.image.load("IMG/swearword.png").convert()
plane = pygame.image.load("IMG/plane.png").convert()
balloon = pygame.image.load("IMG/balloon.png").convert()
gun = pygame.image.load("IMG/gun.png").convert()
lighthouse = pygame.image.load("IMG/lighthouse.png").convert()
friday = pygame.image.load("IMG/friday.png").convert()
bengunn = pygame.image.load("IMG/bengunn.png").convert()
missionary = pygame.image.load("IMG/missionary.png").convert()
bottles1 = pygame.image.load("IMG/bottles1.png").convert()
bottles2 = pygame.image.load("IMG/bottles2.png").convert()
bottles3 = pygame.image.load("IMG/bottles3.png").convert()
cave = pygame.image.load("IMG/cave.png").convert()
barrel = pygame.image.load("IMG/barrel.png").convert()
earthquake = pygame.image.load("IMG/earthquake.png").convert()
jungles = pygame.image.load("IMG/jungles.png").convert()
grass = pygame.image.load("IMG/grass.png").convert()
empty = pygame.image.load("IMG/empty.png").convert()
frame = pygame.image.load("IMG/frame.png").convert_alpha()
boat = pygame.image.load("IMG/boat.png").convert()
sea = pygame.image.load("IMG/open.png").convert()

# Загрузка шрифтов
roboto_Bold = pygame.font.Font("font/RobotoMono-Bold.ttf", 24)
roboto_Regular = pygame.font.Font("font/RobotoMono-Regular.ttf", 24)

# Нормализация картинок
gun = pygame.transform.rotate(gun, 270)
arrow7 = pygame.transform.rotate(arrow7, 270)

digit2delta = {
    1: (-1, -1),
    2: (0, -1),
    3: (1, -1),
    4: (-1, 0),
    5: (1, 0),
    6: (-1, 1),
    7: (0, 1),
    8: (1, 1),
    9: (-1, -2),
    10: (1, -2),
    11: (-2, -1),
    12: (2, -1),
    13: (-2, 1),
    14: (2, 1),
    15: (-1, 2),
    16: (1, 2)
}

digit2degrees = {
    1: "-270",
    2: "-270",
    3: "-0",
    4: "-180",
    5: "-0",
    6: "-180",
    7: "-90",
    8: "-90"
}

squares_name_img = {"e1": empty1,
                    "e2": empty2,
                    "e3": empty3,
                    "e4": empty4,

                    "a1": arrow1,
                    "a2": arrow2,
                    "a3": arrow3,
                    "a4": arrow4,
                    "a5": arrow5,
                    "a6": arrow6,
                    "a7": arrow7,

                    "h": horse,

                    "t2": turntable2,
                    "t3": turntable3,
                    "t4": turntable4,
                    "t5": turntable5,

                    "2": ice,
                    "tc": trap,
                    "c": crocodile,
                    "w": ogre,

                    "f": fortress,
                    "r": aborigine,

                    "m1": gold1,
                    "m2": gold2,
                    "m3": gold3,
                    "m4": gold4,
                    "m5": gold5,
                    "mc": gold,

                    "tk": swearword,
                    "p": plane,

                    "b": balloon,
                    "g": gun,
                    "l": lighthouse,

                    "F": friday,
                    "B": bengunn,
                    "M": missionary,

                    "v1": bottles1,
                    "v2": bottles2,
                    "v3": bottles3,

                    "d": cave,
                    "tv": barrel,

                    "q": earthquake,
                    "j": jungles,
                    "m": grass
                    }

squares = {"e1": 5, "e2": 4, "e3": 5, "e4": 4,
           "a1": 3, "a2": 3, "a3": 3, "a4": 3, "a5": 3, "a6": 3, "a7": 3,
           "h": 2,
           "t5": 1, "t4": 2, "t3": 4, "t2": 5,
           "2": 6, "tc": 3, "c": 4, "w": 1,
           "f": 2, "r": 1,
           "m5": 1, "m4": 2, "m3": 3, "m2": 5, "m1": 5, "mc": 1,
           "p": 1, "tk": 1,
           "b": 2, "g": 2, "l": 1,
           "F": 1, "B": 1, "M": 1,
           "v3": 1, "v2": 2, "v1": 3,
           "d": 4, "tv": 4,
           "q": 1, "j": 3, "m": 2
           }

areaOpen = [[[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13]],
            [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13]],
            [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13]],
            [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13]],
            [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13]],
            [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13]],
            [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13]],
            [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13]],
            [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13]],
            [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13]],
            [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13]],
            [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13]],
            [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13]]
            ]

areaSquares: list[list[list[Any]]] = [[[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13]],
                                      [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13]],
                                      [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13]],
                                      [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13]],
                                      [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13]],
                                      [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13]],
                                      [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13]],
                                      [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13]],
                                      [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13]],
                                      [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13]],
                                      [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13]],
                                      [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13]],
                                      [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13]]
                                      ]

areaPawns = [[[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13]],
             [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13]],
             [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13]],
             [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13]],
             [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13]],
             [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13]],
             [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13]],
             [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13]],
             [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13]],
             [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13]],
             [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13]],
             [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13]],
             [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13]]
             ]


def own_rand(start: int, end: int) -> int:
    return random.randrange(start, end)


def set_corners():
    for i in range(0, len(areaSquares[0])):
        areaSquares[0][i][0] = "S"
        areaOpen[0][i][0] = 1

    for i in range(1, len(areaSquares) - 1):
        areaSquares[i][0][0] = "S"
        areaOpen[i][0][0] = 1
        areaSquares[i][len(areaSquares[i]) - 1][0] = "S"
        areaOpen[i][len(areaSquares[i]) - 1][0] = 1

        areaSquares[1][1][0] = "S"
        areaSquares[1][11][0] = "S"
        areaSquares[11][1][0] = "S"
        areaSquares[11][11][0] = "S"

        areaOpen[1][1][0] = 1
        areaOpen[1][11][0] = 1
        areaOpen[11][1][0] = 1
        areaOpen[11][11][0] = 1

    for i in range(0, len(areaSquares[len(areaSquares) - 1])):
        areaSquares[len(areaSquares) - 1][i][0] = "S"
        areaOpen[len(areaSquares) - 1][i][0] = 1


def clear_area(area: list):
    for y in range(0, len(area)):
        for x in range(0, len(area[y])):
            area[x][y] = [0]


def fill_area(area: list, value):
    set_corners()
    for y in range(0, len(area)):
        for x in range(0, len(area[y])):
            if area[y][x][0] != "S":
                area[x][y][0] = value


def print_area(area: list, mode: str, ps=""):
    if mode == "Поле":
        print("\033[32m{}\033[0m".format(f"▦ Просмотр поля: {ps}"))
        line = ""
        for y in range(0, len(area)):
            for x in range(0, len(area[y])):
                line = line\
                       + str(area[y][x][0])\
                       + " " * (3 - len(str(area[y][x][0])))
            print("\033[32m{}\033[0m".format(f"{line}"))
            line = ""
        print("\n")

    elif mode == "Массив":
        print("\033[32m{}\033[0m".format(f"▥ Просмотр массива: {ps}"))
        for y in range(0, len(area)):
            print("\033[32m{}\033[0m".format(f"{area[y]}"))
        print("\n")

    elif mode == "Список":
        print("\033[32m{}\033[0m".format(f"▤ Просмотр списка: {ps}"))
        for y in range(0, len(area)):
            for x in range(0, len(area[y])):
                print("\033[32m{}\033[0m".format(f"{area[y][x]}"))
        print("\n")
    elif mode == "Строка":
        print("\033[32m{}\033[0m".format(f"▧ Просмотр строки: {ps}\n{area}"))
        print("\n")


def mix_area(area: list):
    clear_area(area)
    squares_ = squares.copy()
    set_corners()
    for y in range(0, len(area)):
        for x in range(0, len(area[y])):
            if area[y][x][0] != "S":
                while True:
                    # print(sum(squares_.values()))
                    choose = random.choice(list(squares_.keys()))
                    if squares_[choose] != 0:
                        squares_[choose] -= 1
                        if choose == "g":
                            area[y][x] = ["g", random.choice([[2], [4], [5], [7]])]
                            break
                        elif choose == "a1":
                            area[y][x] = ["a1", random.choice([[1], [3], [6], [8]])]
                            break
                        elif choose == "a2":
                            area[y][x] = ["a2", random.choice([[2], [4], [5], [7]])]
                            break
                        elif choose == "a3":
                            area[y][x] = ["a3", random.choice([[4, 5], [2, 7]])]
                            break
                        elif choose == "a4":
                            area[y][x] = ["a4", random.choice([[1, 8], [3, 6]])]
                            break
                        elif choose == "a5":
                            area[y][x] = ["a5", [1, 3, 6, 8]]
                            break
                        elif choose == "a6":
                            area[y][x] = ["a6", [2, 4, 5, 7]]
                            break
                        elif choose == "a7":
                            area[y][x] = ["a7", random.choice([[1, 5, 7], [3, 4, 7], [6, 5, 2], [8, 4, 2]])]
                            break
                        elif choose == "p":
                            area[y][x] = ["p", True]
                            break
                        else:
                            area[y][x][0] = choose
                            break


def print_window(text: str):
    line = roboto_Bold.render(text, True, black)
    window.blit(line, (100, 50))


def clear_window():
    window.fill(white)


def open_square(opened: list, x: int, y: int,):
    if 0 <= x < len(opened) and 0 <= y < len(opened):
        opened[y][x][0] = 1
    show_area(areaSquares, areaOpen)


def close_square(opened: list, x: int, y: int,):
    if 0 <= x < len(opened) and 0 <= y < len(opened):
        opened[y][x][0] = 0
    show_area(areaSquares, areaOpen)


def change_scope(delta: int):
    global scope
    if 20 <= scope + delta <= 190:
        scope += delta
    show_area(areaSquares, areaOpen)
    print("\033[34m{}\033[0m".format(f"Масштаб:   {scope}"))


def change_place(delta: tuple):
    global place_x, place_y
    place_x = place_x + delta[0]
    place_y = place_y + delta[1]
    show_area(areaSquares, areaOpen)
    print("\033[34m{}\033[0m".format(f"Положение: {place_x}, {place_y}"))


def mark_outline_rectangle(x, y, color: tuple):
    pygame.draw.rect(window, color, (x * scope + place_x, y * scope + place_y, scope, scope), 2)


def mark_fill_squares(x_y: list, color: tuple):
    square = pygame.Surface((scope, scope), pygame.SRCALPHA)
    square.fill(color)
    for c in x_y:
        window.blit(square, (c[0] * scope + place_x, c[1] * scope + place_y))


def check_step_arrow(x: int, y: int, array: set, directions: list):
    mark_outline_rectangle(x, y, out)
    pygame.display.flip()

    print(f"↗ Проверка стрелки:  "
          f"{x}, {y}{' ' * (4 - (x // 10 + y // 10))}{array}")
    for delta in directions:
        new_x = x + digit2delta[delta][0]
        new_y = y + digit2delta[delta][1]
        if 0 <= new_x < len(areaSquares) and \
           0 <= new_y < len(areaSquares):
            if areaOpen[new_y][new_x][0] == 1:
                if areaSquares[new_y][new_x][0] == "a1" and (new_x, new_y) not in array:
                    array.add((new_x, new_y))
                    check_step_arrow(new_x, new_y, array, areaSquares[new_y][new_x][1])
                    array.discard((new_x, new_y))
                elif areaSquares[new_y][new_x][0] == "a2" and (new_x, new_y) not in array:
                    array.add((new_x, new_y))
                    check_step_arrow(new_x, new_y, array, areaSquares[new_y][new_x][1])
                    array.discard((new_x, new_y))
                elif areaSquares[new_y][new_x][0] == "a3" and (new_x, new_y) not in array:
                    array.add((new_x, new_y))
                    check_step_arrow(new_x, new_y, array, areaSquares[new_y][new_x][1])
                    array.discard((new_x, new_y))
                elif areaSquares[new_y][new_x][0] == "a4" and (new_x, new_y) not in array:
                    array.add((new_x, new_y))
                    check_step_arrow(new_x, new_y, array, areaSquares[new_y][new_x][1])
                    array.discard((new_x, new_y))
                elif areaSquares[new_y][new_x][0] == "a5" and (new_x, new_y) not in array:
                    array.add((new_x, new_y))
                    check_step_arrow(new_x, new_y, array, areaSquares[new_y][new_x][1])
                    array.discard((new_x, new_y))
                elif areaSquares[new_y][new_x][0] == "a6" and (new_x, new_y) not in array:
                    array.add((new_x, new_y))
                    check_step_arrow(new_x, new_y, array, areaSquares[new_y][new_x][1])
                    array.discard((new_x, new_y))
                elif areaSquares[new_y][new_x][0] == "a7" and (new_x, new_y) not in array:
                    array.add((new_x, new_y))
                    check_step_arrow(new_x, new_y, array, areaSquares[new_y][new_x][1])
                    array.discard((new_x, new_y))
                elif areaSquares[new_y][new_x][0] == "S" and (new_x, new_y) not in array:
                    array.add((new_x, new_y))
                elif (new_x, new_y) not in array:
                    check_step(new_x, new_y, delta, array)
            else:
                array.add((new_x, new_y))


def check_step(x: int, y: int, delta: int, array: set):
    mark_outline_rectangle(x, y, out)
    pygame.display.flip()

    print(f"☐ Проверка шага:     "
          f"{x}, {y}{' ' * (4 - (x // 10 + y // 10))}{array}")

    if 0 <= x < len(areaSquares) and \
            0 <= y < len(areaSquares):
        if areaOpen[y][x][0] == 1:
            if areaSquares[y][x][0] == "2":
                new_x = x + digit2delta[delta][0]
                new_y = y + digit2delta[delta][1]
                check_step(new_x, new_y, delta, array)
            elif "a" in areaSquares[y][x][0]:
                check_step_arrow(x, y, array, areaSquares[y][x][1])
            elif (x, y) not in array and \
                    areaSquares[y][x][0] != "c" and \
                    areaSquares[y][x][0] != "S":
                array.add((x, y))
        else:
            array.add((x, y))


def check_steps(x: int, y: int):
    steps = [1, 2, 3, 4, 5, 6, 7, 8]
    array = set()
    if 0 <= x < len(areaSquares) and 0 <= y < len(areaSquares):
        mark_fill_squares([(x, y)], select)
        if areaSquares[y][x][0] == "p":
            if areaSquares[y][x][1]:  # True, если не использовали
                for y_ in range(0, len(areaOpen)):
                    for x_ in range(0, len(areaOpen)):
                        if areaOpen[y_][x_][0] == 1 and areaSquares[y_][x_][0] != "S":
                            array.add((x_, y_))
        elif areaSquares[y][x][0] == "h":
            steps = [9, 10, 11, 12, 13, 14, 15, 16]
        elif "a" in areaSquares[y][x][0]:
            check_step_arrow(x, y, array, areaSquares[y][x][1])
            print_area(list(array), "Строка", ps="Координаты, куда ходить")
            mark_fill_squares(list(array), mark)
            return
        for delta in steps:
            check_step(x + digit2delta[delta][0], y + digit2delta[delta][1], delta, array)
    array = list(array)
    print_area(array, "Строка", ps="Координаты, куда ходить")
    mark_fill_squares(array, mark)


def mouse_click(x_y: tuple, mode: int, delay: float):
    if mode == 1 or mode == 3:
        global scope
        x = (x_y[0] - place_x) // scope
        y = (x_y[1] - place_y) // scope
        if mode == 1:
            open_square(areaOpen, x, y)
        elif mode == 3:
            close_square(areaOpen, x, y)
        if 0 <= x < len(areaSquares) and 0 <= y < len(areaSquares):
            print("\033[35m{}\033[0m".format(f"Координаты квадрата: "
                                             f"{x}, {y}{' ' * (4 - (x//10 + y//10))}{areaSquares[y][x]}"
                                             f"{' ' * (30 - len(str(areaSquares[y][x])))}"
                                             f"Δt {delay}"))
            print_window(f"{areaSquares[y][x]}\n{x}, {y}")
        check_steps(x, y)


def show_area(area: list, opened: list):
    global scope
    clear_window()
    square_temp = pygame.transform.scale(frame, (scope * 13, scope * 13))
    window.blit(square_temp, (place_x, place_y))
    for y in range(0, len(area)):
        for x in range(0, len(area[y])):
            if opened[y][x][0] == 1 and area[y][x][0] != "S":
                square_temp = pygame.transform.scale(squares_name_img[area[y][x][0]], (scope, scope))
                if area[y][x][0] == "g":
                    square_temp = pygame.transform.rotate(square_temp,
                                                          int(digit2degrees[area[y][x][1][0]]))
                elif area[y][x][0] == "a1":
                    square_temp = pygame.transform.rotate(square_temp,
                                                          int(digit2degrees[area[y][x][1][0]]))
                elif area[y][x][0] == "a2":
                    square_temp = pygame.transform.rotate(square_temp,
                                                          int(digit2degrees[area[y][x][1][0]]))
                elif area[y][x][0] == "a3":
                    square_temp = pygame.transform.rotate(square_temp,
                                                          int(digit2degrees[area[y][x][1][0]]))
                elif area[y][x][0] == "a4":
                    square_temp = pygame.transform.rotate(square_temp,
                                                          int(digit2degrees[area[y][x][1][0]]))
                elif area[y][x][0] == "a7":
                    square_temp = pygame.transform.rotate(square_temp,
                                                          int(digit2degrees[area[y][x][1][0]]))
                window.blit(square_temp, (x * scope + place_x, y * scope + place_y))
            elif opened[y][x][0] == 0 and area[y][x][0] != "S":
                square_temp = pygame.transform.scale(empty, (scope, scope))
                window.blit(square_temp, (x * scope + place_x, y * scope + place_y))

    square_temp = pygame.transform.scale(boat, (scope, scope))
    window.blit(square_temp, (0 * scope + place_x, 6 * scope + place_y))
    square_temp = pygame.transform.scale(boat, (scope, scope))
    window.blit(square_temp, (6 * scope + place_x, 0 * scope + place_y))
    square_temp = pygame.transform.scale(boat, (scope, scope))
    window.blit(square_temp, (12 * scope + place_x, 6 * scope + place_y))
    square_temp = pygame.transform.scale(boat, (scope, scope))
    window.blit(square_temp, (6 * scope + place_x, 12 * scope + place_y))


pygame.display.set_caption("Thousand devils")
pygame.display.set_icon(pygame.image.load("IMG/empty1.png"))


clear_area(areaOpen)
clear_area(areaSquares)
clear_area(areaPawns)

set_corners()
print_area(areaSquares, "Поле", ps="Рамка")

# Строчки для теста цикл: —> <—
fill_area(areaSquares, "e2")
areaSquares[3][6] = ["a2", [5]]
areaSquares[3][7] = ["a2", [4]]
areaSquares[6][6] = ["h"]
areaSquares[7][8] = ["2"]

areaSquares[7][3] = ["a2", [2]]
areaSquares[8][3] = ["a2", [2]]
areaSquares[9][3] = ["a2", [2]]

areaSquares[9][2] = ["f"]
areaSquares[9][4] = ["f"]
areaSquares[3][3] = ["p", True]


print_area(areaSquares, "Массив", ps="Поле")
print_area(areaSquares, "Поле", ps="Поле")
show_area(areaSquares, areaOpen)


flag_holdup = False
temp_time = 0.0
running = True
while running:

    pygame.display.update()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            flag_holdup = True
            temp_time = time.time()

        elif event.type == pygame.MOUSEBUTTONUP:
            if time.time() - temp_time < holdup:
                flag_holdup = False
                mouse_click(event.pos, event.button, time.time() - temp_time)
            else:
                flag_holdup = False

        elif event.type == pygame.MOUSEWHEEL:
            change_scope(event.y)

        elif event.type == pygame.MOUSEMOTION and flag_holdup:
            change_place(event.rel)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                clear_area(areaSquares)
                clear_area(areaOpen)
                mix_area(areaSquares)
                print_area(areaSquares, "Поле", ps="Поле")
                show_area(areaSquares, areaOpen)

            elif event.key == pygame.K_o:
                fill_area(areaOpen, 1)
                show_area(areaSquares, areaOpen)
    clock.tick(fps)
