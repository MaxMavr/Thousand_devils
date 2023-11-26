# import math
# import random
import pygame
import time
from random import choice
from typing import Any

window_height = 800
window_width = window_height * 16 / 9

fps = 60
scope = 60
place_x = 340
place_y = 0
time_tap = 0.17

# Цвета
bg_color = (255, 255, 255)
text_color = (0, 0, 0)
mark_step_color = (139, 0, 139, 255 / 2)
mark_select_color = (0, 255, 0, 255 / 1.5)
mark_frame_color = (0, 128, 0)

pawn_yellow = (255, 215, 0)
pawn_black = (30, 30, 30)
pawn_white = (245, 245, 245)
pawn_red = (170, 0, 0)

# white = (255, 255, 255)
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
boat_img = pygame.image.load("IMG/boat.png").convert()
sea = pygame.image.load("IMG/open.png").convert()

# Загрузка шрифтов
RobotoBold = pygame.font.Font("font/RobotoMono-Bold.ttf", 12)
RobotoRegular = pygame.font.Font("font/RobotoMono-Regular.ttf", 12)

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

pawn2color = {
    "R": pawn_red,
    "W": pawn_white,
    "B": pawn_black,
    "Y": pawn_yellow
}

pawnsColor = ["R", "W", "B", "Y"]

squares_img_name = {"e1": empty1,
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


class Boat:
    def __init__(self, color: str, current: list, select: bool):
        self.color = color
        self.current = current
        self.select = select

    def info(self):
        print(f"{self.color}\n"
              f"{self.current}\n"
              f"{self.select}")


class Pawn:
    def __init__(self, color: str, last: list, current: list, skip: int):
        self.color = color
        self.last = last
        self.current = current
        self.skip = skip

    def info(self):
        print(f"{self.color}\n"
              f"{self.last}\n"
              f"{self.current}\n"
              f"{self.skip}\n")


boats = [Boat("R", [6, 0], False),
         Boat("W", [0, 6], False),
         Boat("Y", [6, 12], False),
         Boat("B", [12, 6], False)]

pawn_select = -1
pawns = [Pawn("R", [3, 5], [3, 3], 0),
         # Pawn("Y", [6, 11], [2, 3]),
         Pawn("Y", [6, 11], [12, 6], 0),
         Pawn("Y", [6, 11], [12, 6], 0),
         Pawn("Y", [6, 11], [12, 6], 0),
         Pawn("Y", [6, 11], [12, 6], 0),
         Pawn("Y", [6, 11], [12, 6], 0),
         Pawn("Y", [6, 11], [12, 6], 0),
         Pawn("Y", [6, 11], [12, 6], 0),
         Pawn("Y", [6, 11], [12, 6], 0)]


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


def file2area(name_file: str):
    open(name_file, 'r')
    pass


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
        print("\033[32m{}\033[0m".format(f"\n▦ Просмотр поля: {ps}"))
        print("\033[32m{}\033[0m".format("   0  1  2  3  4  5  6  7  8  9 10 11 12"))
        for y in range(0, len(area)):
            line = str(y) \
                   + " " * (3 - len(str(y)))
            for x in range(0, len(area[y])):
                line = line \
                       + str(area[y][x][0]) \
                       + " " * (3 - len(str(area[y][x][0])))
            print("\033[32m{}\033[0m".format(f"{line}"))

    elif mode == "Массив":
        print("\033[32m{}\033[0m".format(f"\n▥ Просмотр массива: {ps}"))
        for y in range(0, len(area)):
            print("\033[32m{}\033[0m".format(f"{area[y]}"))

    elif mode == "Список":
        print("\033[32m{}\033[0m".format(f"\n▤ Просмотр списка: {ps}"))
        for y in range(0, len(area)):
            for x in range(0, len(area[y])):
                print("\033[32m{}\033[0m".format(f"{area[y][x]}"))

    elif mode == "Строка":
        print("\033[32m{}\033[0m".format(f"▧ Просмотр строки: {ps}\n{area}"))


def mix_area(area: list):
    clear_area(area)
    set_corners()
    temp_squares = squares.copy()
    den_coords_xy = []
    for y in range(0, len(area)):
        for x in range(0, len(area[y])):
            if area[y][x][0] != "S":
                while True:
                    chosen = choice(list(temp_squares.keys()))
                    if temp_squares[chosen] != 0:
                        temp_squares[chosen] -= 1
                        if chosen == "g":
                            area[y][x] = ["g", choice([[2], [4], [5], [7]])]
                            break
                        elif chosen == "a1":
                            area[y][x] = ["a1", choice([[1], [3], [6], [8]])]
                            break
                        elif chosen == "a2":
                            area[y][x] = ["a2", choice([[2], [4], [5], [7]])]
                            break
                        elif chosen == "a3":
                            area[y][x] = ["a3", choice([[4, 5], [2, 7]])]
                            break
                        elif chosen == "a4":
                            area[y][x] = ["a4", choice([[1, 8], [3, 6]])]
                            break
                        elif chosen == "a5":
                            area[y][x] = ["a5", [1, 3, 6, 8]]
                            break
                        elif chosen == "a6":
                            area[y][x] = ["a6", [2, 4, 5, 7]]
                            break
                        elif chosen == "a7":
                            area[y][x] = ["a7", choice([[1, 5, 7], [3, 4, 7], [6, 5, 2], [8, 4, 2]])]
                            break
                        elif chosen == "p":
                            area[y][x] = ["p", True]
                            break
                        elif chosen == "q":
                            area[y][x] = ["q", True]
                            break
                        elif chosen == "l":
                            area[y][x] = ["l", 3]
                            break
                        elif chosen == "d":
                            den_coords_xy.append((x, y))
                            break
                        else:
                            area[y][x][0] = chosen
                            break
    for den_coord_xy in den_coords_xy:
        area[den_coord_xy[1]][den_coord_xy[0]] = ["d", den_coords_xy]


def print_area_window(text: str, coord_xy: tuple):
    line = RobotoRegular.render(text, True, text_color, bg_color)
    window.blit(line, coord_xy)


def clear_window():
    window.fill(bg_color)


def open_square(x: int, y: int):
    if 0 <= x < len(areaOpen) and 0 <= y < len(areaOpen):
        areaOpen[y][x][0] = 1
    show_area(areaSquares, areaOpen)


def close_square(x: int, y: int):
    if 0 <= x < len(areaOpen) and 0 <= y < len(areaOpen):
        areaOpen[y][x][0] = 0
    show_area(areaSquares, areaOpen)


def earthquake():
    closed = []
    print(f"☯ Землетрясение:")
    for y in range(0, len(areaOpen)):
        for x in range(0, len(areaOpen)):
            if areaOpen[y][x][0] != 1:
                closed.append((x, y))
    if len(closed) >= 4:
        for i in range(2):
            chosen1 = choice(closed)
            closed.remove(chosen1)
            chosen2 = choice(closed)
            closed.remove(chosen2)
            temp_square1 = areaSquares[chosen1[1]][chosen1[0]]
            temp_square2 = areaSquares[chosen2[1]][chosen2[0]]
            areaSquares[chosen1[1]][chosen1[0]] = temp_square2
            areaSquares[chosen2[1]][chosen2[0]] = temp_square1
            print(f"Поменяли клетки:     "
                  f"{chosen1[0]}, {chosen1[1]} "
                  f"{temp_square1}"
                  f" ⇄ "
                  f"{chosen2[0]}, {chosen2[1]} "
                  f"{temp_square2}")


def illuminate(x: int, y: int):
    global game_mode, pawn_select
    print(f"Пешка на маяке: {pawn_select}")
    if areaSquares[pawns[pawn_select].current[1]][pawns[pawn_select].current[0]][1] >= 1:
        if game_mode == "lighthouse":
            if areaOpen[y][x][0] == 0 and \
                    0 <= x < len(areaOpen) and 0 <= y < len(areaOpen):
                print(f"☄ Маяк открыл клетку:"
                      f"{x}, {y}{' ' * (4 - (x // 10 + y // 10))}"
                      f"{areaSquares[y][x]}")
                open_square(x, y)
                areaSquares[pawns[pawn_select].current[1]][pawns[pawn_select].current[0]][1] -= 1
                if areaSquares[pawns[pawn_select].current[1]][pawns[pawn_select].current[0]][1] == 0:
                    print("Маяк сломался")
                    game_mode = "select"
                    pawn_select = -1
        else:
            game_mode = "lighthouse"
    else:
        print("Маяк не работает")
        game_mode = "select"
        pawn_select = -1


def flight() -> set:
    allowed_steps = set()
    for y in range(0, len(areaOpen)):
        for x in range(0, len(areaOpen)):
            if areaOpen[y][x][0] == 1 and \
                    areaSquares[y][x][0] != "S" and \
                    areaSquares[y][x][0] != "c":
                allowed_steps.add((x, y))
    return allowed_steps


def change_scope(delta: int):
    global scope, place_x, place_y
    if 20 <= scope + delta <= 190:
        scope += delta
        # Компенсация изменения (Поле рисуется слева направо)
        place_x -= delta * 7
        place_y -= delta * 7
    show_area(areaSquares, areaOpen)
    print("\033[34m{}\033[0m".format(f"Масштаб:   {scope}"))


def change_place(delta: tuple):
    global place_x, place_y
    place_x += delta[0]
    place_y += delta[1]
    show_area(areaSquares, areaOpen)
    print("\033[34m{}\033[0m".format(f"Положение: {place_x}, {place_y}"))


def mark_stroke_squares(coords_xy: list, color: tuple):
    for coord_xy in coords_xy:
        pygame.draw.rect(window, color,
                         (coord_xy[0] * scope + place_x,
                          coord_xy[1] * scope + place_y,
                          scope, scope), 2)


def mark_fill_squares(coords_xy: list, color: tuple):
    square = pygame.Surface((scope, scope), pygame.SRCALPHA)
    square.fill(color)
    for coord_xy in coords_xy:
        window.blit(square,
                    (coord_xy[0] * scope + place_x,
                     coord_xy[1] * scope + place_y))


def kill_pawn():
    print("\033[31m{}\033[0m".format(f"☠ Убита пешка:      "
                                     f"{pawns[pawn_select].current[0]}, "
                                     f"{pawns[pawn_select].current[1]} "
                                     f"{pawns[pawn_select].color}"))
    pawns.remove(pawns[pawn_select])


def kick_pawn():
    print("\033[35m{}\033[0m".format(f"⎋ Пешка на корабле:  "
                                     f"{pawns[pawn_select].current[0]}, "
                                     f"{pawns[pawn_select].current[1]} "
                                     f"{pawns[pawn_select].color}"))
    for boat in boats:
        if boat.color == pawns[pawn_select].color:
            pawns[pawn_select].current[0] = boat.current[0]
            pawns[pawn_select].current[1] = boat.current[1]


def loop_search(start_x: int, start_y: int) -> bool:
    def check_arrow(x: int, y: int):
        nonlocal used_steps

        print(f"↗ Проверка стрелки:  "
              f"{x}, {y}{' ' * (4 - (x // 10 + y // 10))}{used_steps}")

        for digit in areaSquares[y][x][1]:
            new_x = x + digit2delta[digit][0]
            new_y = y + digit2delta[digit][1]
            if 0 <= new_x < len(areaSquares) and \
                    0 <= new_y < len(areaSquares) and \
                    (new_x, new_y) not in used_steps:
                if areaOpen[new_y][new_x][0] == 1:
                    if "a" in areaSquares[new_y][new_x][0]:
                        used_steps.add((new_x, new_y))
                        check_arrow(new_x, new_y)
                    else:
                        check_step((new_x, new_y), (x, y))
                else:
                    used_steps.add((new_x, new_y))

    def check_step(coord_xy: tuple, last_coord_xy: tuple):
        nonlocal used_steps, checked_steps
        x = coord_xy[0]
        y = coord_xy[1]
        old_x = last_coord_xy[0]
        old_y = last_coord_xy[1]

        print(f"☐ Проверка шага:     "
              f"{x}, {y}"
              f"{' ' * (4 - (x // 10 + y // 10))}{used_steps}   {checked_steps}")

        if 0 <= coord_xy[0] < len(areaSquares) and \
                0 <= coord_xy[1] < len(areaSquares):
            if areaOpen[coord_xy[1]][coord_xy[0]][0] == 1:
                if areaSquares[y][x][0] == "2":
                    check_step((x + (x - old_x), y + (y - old_y)), (x, y))
                elif "a" in areaSquares[y][x][0] and (x, y) not in used_steps:
                    used_steps.add((x, y))
                    check_arrow(x, y)
                elif areaSquares[y][x][0] != "c" and (x, y) not in used_steps:
                    used_steps.add((x, y))
            elif areaOpen[y][x][0] == 0 and (x, y) not in used_steps:
                used_steps.add((x, y))

    checked_digits = [1, 2, 3, 4, 5, 6, 7, 8]
    checked_steps = []
    used_steps = set()
    extra_quantity = 0
    if 0 <= start_x < len(areaSquares) and \
            0 <= start_y < len(areaSquares):

        if "a" in areaSquares[start_y][start_x][0]:
            checked_digits = areaSquares[start_y][start_x][1]

        # Получаем из направлений координаты
        for digit in checked_digits:
            checked_steps.append((start_x + digit2delta[digit][0],
                                  start_y + digit2delta[digit][1]))
        # Проверяем координаты
        for step in checked_steps:
            check_step(step, (start_x, start_y))

    for step in used_steps:
        if ("a" in areaSquares[step[1]][step[0]][0] or
            areaSquares[step[1]][step[0]][0] == "2") and \
                areaOpen[step[1]][step[0]][0] == 1:
            extra_quantity += 1
    used_steps = list(used_steps)
    print_area(used_steps, "Строка", ps="Координаты, куда можно сходить")
    # mark_fill_squares(list(used_steps), mark_select_color)
    # show_area(areaSquares, areaOpen)
    return len(used_steps) - extra_quantity == 0


def check_steps(x: int, y: int) -> list:
    checked_steps = [1, 2, 3, 4, 5, 6, 7, 8]
    allowed_steps = set()
    if 0 <= x < len(areaSquares) and 0 <= y < len(areaSquares):
        if areaSquares[y][x][0] == "S":
            checked_steps = [2, 4, 5, 7]
        elif areaSquares[y][x][0] == "h":
            checked_steps = [9, 10, 11, 12, 13, 14, 15, 16]
        # elif areaSquares[y][x][0] == "d":
        #     quantity_open = 0
        #     for step in areaSquares[y][x][1]:
        #         if areaOpen[step[1]][step[0]][0] == 1:
        #             quantity_open += 1
        #             allowed_steps.add(step)
        #     if quantity_open < 2:
        #         return []
        elif areaSquares[y][x][0] == "p" and areaSquares[y][x][1]:
            allowed_steps = flight()
        elif "a" in areaSquares[y][x][0]:
            checked_steps = areaSquares[y][x][1]
        for step in checked_steps:
            new_x = x + digit2delta[step][0]
            new_y = y + digit2delta[step][1]
            if 0 <= new_x < len(areaSquares) and 0 <= new_y < len(areaSquares):
                if areaOpen[new_y][new_x][0] == 1 and \
                        areaSquares[new_y][new_x][0] != "c":
                    allowed_steps.add((new_x, new_y))
                elif areaOpen[new_y][new_x][0] == 0:
                    allowed_steps.add((new_x, new_y))
    print_area(list(allowed_steps), "Строка", ps="Координаты, куда ходить")
    return list(allowed_steps)


def mouse_click_cancel_select(coord_xy: tuple, delay: float):
    global way_pawn, game_mode, pawn_select
    x = (coord_xy[0] - place_x) // scope
    y = (coord_xy[1] - place_y) // scope
    if 0 <= x < len(areaSquares) and 0 <= y < len(areaSquares) and \
            x == pawns[pawn_select].current[0] and \
            y == pawns[pawn_select].current[1] and \
            "a" not in areaSquares[pawns[pawn_select].current[1]][pawns[pawn_select].current[0]][0]:
        pawn_select = -1
        game_mode = "select"
        way_pawn = []
        print("\033[35m{}\033[0m".format(f"Отмена выбора пешки: "
                                         f"{x}, {y}{' ' * (4 - (x // 10 + y // 10))}{areaSquares[y][x]}"
                                         f"{' ' * (30 - len(str(areaSquares[y][x])))}"
                                         f"Δt {delay}"))
        show_area(areaSquares, areaOpen)


def check_second_steps(x: int, y: int) -> list:
    global game_mode, pawn_select
    if 0 <= x < len(areaSquares) and 0 <= y < len(areaSquares) and pawn_select != -1:
        print("\033[33m{}\033[0m".format(f"Проверка клетки:     "
                                         f"{x}, {y}{' ' * (4 - (x // 10 + y // 10))}{areaSquares[y][x]}"
                                         f"{' ' * (30 - len(str(areaSquares[y][x])))}"))
        steps = []
        if loop_search(pawns[pawn_select].current[0], pawns[pawn_select].current[1]):
            kill_pawn()
            pawn_select = -1
            game_mode = "select"
            return []

        if "a" in areaSquares[pawns[pawn_select].current[1]][pawns[pawn_select].current[0]][0]:
            for digit in areaSquares[pawns[pawn_select].current[1]][pawns[pawn_select].current[0]][1]:
                steps.append((pawns[pawn_select].current[0] + digit2delta[digit][0],
                              pawns[pawn_select].current[1] + digit2delta[digit][1]))
            return steps

        if areaSquares[pawns[pawn_select].current[1]][pawns[pawn_select].current[0]][0] == "q" and \
                areaSquares[pawns[pawn_select].current[1]][pawns[pawn_select].current[0]][1]:
            earthquake()
            areaSquares[pawns[pawn_select].current[1]][pawns[pawn_select].current[0]][1] = False

        if areaSquares[pawns[pawn_select].current[1]][pawns[pawn_select].current[0]][0] == "w":
            kill_pawn()
            pawn_select = -1
            game_mode = "select"
            return []

        if areaSquares[pawns[pawn_select].current[1]][pawns[pawn_select].current[0]][0] == "b":
            kick_pawn()

        if areaSquares[y][x][0] == "2":
            if areaSquares[pawns[pawn_select].last[1]][pawns[pawn_select].last[0]][0] == "p" and \
                    areaSquares[pawns[pawn_select].last[1]][pawns[pawn_select].last[0]][1]:
                areaSquares[pawns[pawn_select].last[1]][pawns[pawn_select].last[0]][1] = False
                return list(flight())
            elif areaSquares[pawns[pawn_select].last[1]][pawns[pawn_select].last[0]][0] == "h":
                for digit in [9, 10, 11, 12, 13, 14, 15, 16]:
                    steps.append((x + digit2delta[digit][0], y + digit2delta[digit][1]))
                return steps
            else:
                delta_x = pawns[pawn_select].current[0] - pawns[pawn_select].last[0]
                delta_y = pawns[pawn_select].current[1] - pawns[pawn_select].last[1]
                pawns[pawn_select].last[0] = pawns[pawn_select].current[0]
                pawns[pawn_select].last[1] = pawns[pawn_select].current[1]
                pawns[pawn_select].current[0] += delta_x
                pawns[pawn_select].current[1] += delta_y
                open_square(pawns[pawn_select].current[0], pawns[pawn_select].current[1])
                return check_second_steps(pawns[pawn_select].current[0], pawns[pawn_select].current[1])

        if areaSquares[pawns[pawn_select].last[1]][pawns[pawn_select].last[0]][0] == "p":
            areaSquares[pawns[pawn_select].last[1]][pawns[pawn_select].last[0]][1] = False

        if areaSquares[pawns[pawn_select].current[1]][pawns[pawn_select].current[0]][0] == "l":
            illuminate(-1, -1)
            return []

        if areaSquares[y][x][0] == "g":
            if areaSquares[y][x][1][0] == 2:
                pawns[pawn_select].current[1] = 0
            if areaSquares[y][x][1][0] == 4:
                pawns[pawn_select].current[0] = 0
            if areaSquares[y][x][1][0] == 5:
                pawns[pawn_select].current[0] = 12
            if areaSquares[y][x][1][0] == 7:
                pawns[pawn_select].current[1] = 12

        if areaSquares[y][x][0] == "c":
            pawns[pawn_select].current = [pawns[pawn_select].last[0], pawns[pawn_select].last[1]]
            return check_second_steps(pawns[pawn_select].current[0], pawns[pawn_select].current[1])
        pawn_select = -1
        game_mode = "select"
        return []


def mouse_click_select(x: int, y: int, delay: float) -> list:
    global game_mode, pawn_select
    if 0 <= x < len(areaSquares) and 0 <= y < len(areaSquares) and pawn_select != -1:
        game_mode = "move"
        print("\033[35m{}\033[0m".format(f"\nВыбрана пешка:       "
                                         f"{x}, {y}{' ' * (4 - (x // 10 + y // 10))}{areaSquares[y][x]}"
                                         f"{' ' * (30 - len(str(areaSquares[y][x])))}"
                                         f"Δt {delay}"))
        if loop_search(x, y):
            kill_pawn()
        else:
            return check_steps(x, y)
    pawn_select = -1
    game_mode = "select"
    return []


def mouse_click_move(x: int, y: int, delay: float):
    global game_mode, way_pawn, pawn_select
    if 0 <= x < len(areaSquares) and 0 <= y < len(areaSquares) and way_pawn and pawn_select != -1:
        for step in way_pawn:
            if x == step[0] and y == step[1]:
                pawns[pawn_select].last = [pawns[pawn_select].current[0], pawns[pawn_select].current[1]]
                pawns[pawn_select].current = [x, y]
                open_square(x, y)
                way_pawn = check_second_steps(x, y)
                print("\033[35m{}\033[0m".format(f"Ход пешки:           "
                                                 f"{x}, {y}{' ' * (4 - (x // 10 + y // 10))}{areaSquares[y][x]}"
                                                 f"{' ' * (30 - len(str(areaSquares[y][x])))}"
                                                 f"Δt {delay}"))


def mouse_click(coord_xy: tuple, color: str, delay: float):
    global way_pawn, game_mode, pawn_select
    x = (coord_xy[0] - place_x) // scope
    y = (coord_xy[1] - place_y) // scope
    if game_mode == "lighthouse":
        illuminate(x, y)
    else:
        if game_mode == "select":
            for pawn in pawns:
                if pawn.color == color and \
                        x == pawn.current[0] and \
                        y == pawn.current[1]:
                    pawn_select = pawns.index(pawn)
            way_pawn = mouse_click_select(x, y, delay)
        elif game_mode == "move":
            mouse_click_move(x, y, delay)
    show_area(areaSquares, areaOpen)
    if 0 <= x < len(areaSquares) and 0 <= y < len(areaSquares):
        print_area_window(f"{areaSquares[y][x]}\n{x}, {y}", coord_xy)


def show_area(area: list, opened: list):
    global scope, way_pawn
    clear_window()
    square_temp = pygame.transform.scale(frame, (scope * 13, scope * 13))
    window.blit(square_temp, (place_x, place_y))
    for y in range(0, len(area)):
        for x in range(0, len(area[y])):
            if opened[y][x][0] == 1 and area[y][x][0] != "S":
                square_temp = pygame.transform.scale(squares_img_name[area[y][x][0]], (scope, scope))
                if "a" in area[y][x][0] or "g" in area[y][x][0]:
                    square_temp = pygame.transform.rotate(square_temp,
                                                          int(digit2degrees[area[y][x][1][0]]))
                window.blit(square_temp, (x * scope + place_x, y * scope + place_y))
            elif opened[y][x][0] == 0 and area[y][x][0] != "S":
                square_temp = pygame.transform.scale(empty, (scope, scope))
                window.blit(square_temp, (x * scope + place_x, y * scope + place_y))
    mark_stroke_squares(way_pawn, mark_step_color)

    square_temp = pygame.transform.scale(boat_img, (scope, scope))
    for boat in boats:
        square = pygame.Surface((scope, scope), pygame.SRCALPHA)
        square.fill(pawn2color[boat.color])
        square.set_alpha(20)
        window.blit(square_temp,
                    (boat.current[0] * scope + place_x,
                     boat.current[1] * scope + place_y))
        window.blit(square,
                    (boat.current[0] * scope + place_x,
                     boat.current[1] * scope + place_y))

    for pawn in pawns:
        pygame.draw.circle(window, pawn2color[pawn.color],
                           (pawn.current[0] * scope + scope / 2 + place_x,
                            pawn.current[1] * scope + scope / 2 + place_y),
                           scope / 4)


def set_1test_area():
    clear_area(areaOpen)
    clear_area(areaSquares)
    fill_area(areaSquares, "e2")
    areaSquares[3][6] = ["a2", [5]]
    areaSquares[3][7] = ["a2", [4]]
    areaSquares[6][6] = ["h"]
    areaSquares[7][8] = ["2"]

    areaSquares[7][3] = ["a2", [2]]
    areaSquares[8][3] = ["a2", [2]]
    areaSquares[9][3] = ["a2", [2]]
    areaSquares[8][7] = ["a7", [3, 4, 7]]

    areaSquares[9][2] = ["f"]
    areaSquares[9][4] = ["f"]
    areaSquares[3][3] = ["p", True]
    areaSquares[5][4] = ["c"]
    areaSquares[11][8] = ["g", [4]]
    areaSquares[6][11] = ["q", True]

    areaSquares[10][9] = ["a1", [3]]
    areaSquares[9][10] = ["c"]

    areaSquares[11][4] = ["a2", [5]]
    areaSquares[11][6] = ["a2", [4]]

    # areaSquares[11][4] = ["a3", [4, 5]]
    # areaSquares[11][6] = ["a3", [4, 5]]
    areaSquares[11][5] = ["2"]
    areaSquares[6][9] = ["2"]
    areaSquares[3][4] = ["2"]
    areaSquares[2][10] = ["l", 3]


def set_2test_area():
    clear_area(areaOpen)
    clear_area(areaSquares)
    fill_area(areaSquares, "e2")
    areaSquares[5][3] = ["2"]
    areaSquares[6][3] = ["2"]
    areaSquares[7][3] = ["2"]
    areaSquares[8][3] = ["2"]

    areaSquares[6][4] = ["2"]
    areaSquares[7][4] = ["2"]
    areaSquares[8][4] = ["2"]

    areaSquares[7][5] = ["2"]
    areaSquares[8][5] = ["2"]

    areaSquares[8][6] = ["2"]

    areaSquares[5][2] = ["a2", [5]]
    areaSquares[6][2] = ["a2", [5]]
    areaSquares[7][2] = ["a2", [5]]
    areaSquares[8][2] = ["a2", [5]]

    areaSquares[5][4] = ["a2", [4]]
    areaSquares[6][5] = ["a2", [4]]
    areaSquares[7][6] = ["a2", [4]]
    areaSquares[8][7] = ["a2", [4]]

    areaSquares[3][2] = ["a1", [3]]
    areaSquares[2][3] = ["a1", [6]]

    areaSquares[2][5] = ["a1", [8]]
    areaSquares[3][6] = ["a1", [1]]

    areaSquares[2][8] = ["a2", [5]]
    areaSquares[2][9] = ["a2", [4]]


def set_3test_area():
    clear_area(areaOpen)
    clear_area(areaSquares)
    fill_area(areaSquares, "e2")
    areaSquares[3][1] = ["a1", [3]]
    areaSquares[4][1] = ["a1", [3]]
    areaSquares[5][1] = ["a1", [3]]
    areaSquares[6][1] = ["a1", [3]]

    areaSquares[1][3] = ["a1", [6]]
    areaSquares[1][4] = ["a1", [6]]
    areaSquares[1][5] = ["a1", [6]]
    areaSquares[1][6] = ["a1", [6]]

    areaSquares[6][5] = ["a1", [8]]
    areaSquares[6][6] = ["a1", [8]]
    areaSquares[6][7] = ["a1", [8]]
    areaSquares[6][8] = ["a1", [8]]

    areaSquares[8][10] = ["a1", [1]]
    areaSquares[9][10] = ["a1", [1]]
    areaSquares[10][10] = ["a1", [1]]
    areaSquares[11][10] = ["a1", [1]]

    areaSquares[2][2] = ["2"]
    areaSquares[3][2] = ["2"]
    areaSquares[4][2] = ["2"]
    areaSquares[5][2] = ["2"]

    areaSquares[2][3] = ["2"]
    areaSquares[3][3] = ["2"]
    areaSquares[4][3] = ["2"]

    areaSquares[2][4] = ["2"]
    areaSquares[3][4] = ["2"]

    areaSquares[2][5] = ["2"]

    areaSquares[7][9] = ["2"]
    areaSquares[8][9] = ["2"]
    areaSquares[9][9] = ["2"]
    areaSquares[10][9] = ["2"]

    areaSquares[7][8] = ["2"]
    areaSquares[8][8] = ["2"]
    areaSquares[9][8] = ["2"]

    areaSquares[7][7] = ["2"]
    areaSquares[8][7] = ["2"]

    areaSquares[7][6] = ["2"]


def set_4test_area():
    clear_area(areaOpen)
    clear_area(areaSquares)
    fill_area(areaSquares, "e2")

    areaSquares[2][3] = ["a2", [5]]
    areaSquares[2][4] = ["a2", [4]]
    areaSquares[2][5] = ["a2", [4]]
    areaSquares[2][7] = ["a2", [5]]
    areaSquares[2][8] = ["a2", [5]]
    areaSquares[2][9] = ["a2", [4]]

    areaSquares[3][2] = ["a2", [5]]
    areaSquares[3][3] = ["a2", [4]]
    areaSquares[3][4] = ["a2", [4]]
    areaSquares[3][5] = ["a2", [4]]
    areaSquares[3][7] = ["a2", [5]]
    areaSquares[3][8] = ["a2", [5]]
    areaSquares[3][9] = ["a2", [5]]
    areaSquares[3][10] = ["a2", [4]]

    areaSquares[4][1] = ["a2", [5]]
    areaSquares[4][2] = ["a2", [4]]
    areaSquares[4][3] = ["a2", [4]]
    areaSquares[4][4] = ["a2", [4]]
    areaSquares[4][5] = ["a2", [4]]
    areaSquares[4][7] = ["a2", [5]]
    areaSquares[4][8] = ["a2", [5]]
    areaSquares[4][9] = ["a2", [5]]
    areaSquares[4][10] = ["a2", [5]]
    areaSquares[4][11] = ["a2", [4]]

    areaSquares[7][6] = ["a1", [6]]
    areaSquares[7][8] = ["a1", [6]]
    areaSquares[7][10] = ["a1", [6]]

    areaSquares[8][5] = ["a1", [6]]
    areaSquares[8][7] = ["a1", [6]]
    areaSquares[8][9] = ["a1", [6]]

    areaSquares[9][4] = ["a1", [6]]
    areaSquares[9][6] = ["a1", [6]]
    areaSquares[9][8] = ["a1", [3]]

    areaSquares[10][3] = ["a1", [6]]
    areaSquares[10][5] = ["a1", [3]]

    areaSquares[11][2] = ["a1", [3]]


def set_5test_area():
    clear_area(areaOpen)
    clear_area(areaSquares)
    fill_area(areaSquares, "e2")

    areaSquares[2][1] = ["a2", [7]]
    areaSquares[3][1] = ["a2", [5]]
    areaSquares[3][2] = ["a1", [1]]

    areaSquares[2][4] = ["a2", [7]]
    areaSquares[2][5] = ["a2", [4]]
    areaSquares[3][4] = ["a1", [3]]

    areaSquares[2][7] = ["a2", [5]]
    areaSquares[2][8] = ["a2", [7]]
    areaSquares[3][8] = ["a1", [1]]

    areaSquares[2][11] = ["a1", [6]]
    areaSquares[3][11] = ["a2", [2]]
    areaSquares[3][10] = ["a2", [5]]

    areaSquares[9][9] = ["a2", [5]]
    areaSquares[10][10] = ["a2", [4]]
    areaSquares[9][10] = ["a2", [7]]
    areaSquares[10][9] = ["a2", [2]]

    areaSquares[5][1] = ["a2", [7]]
    areaSquares[6][1] = ["2"]
    areaSquares[6][2] = ["2"]
    areaSquares[7][1] = ["a2", [5]]
    areaSquares[7][2] = ["2"]
    areaSquares[7][3] = ["a1", [1]]

    areaSquares[5][5] = ["a2", [7]]
    areaSquares[5][6] = ["2"]
    areaSquares[5][7] = ["a2", [4]]
    areaSquares[6][5] = ["2"]
    areaSquares[6][6] = ["2"]
    areaSquares[7][5] = ["a1", [3]]

    areaSquares[9][1] = ["a1", [8]]
    areaSquares[9][2] = ["2"]
    areaSquares[9][3] = ["a2", [4]]
    areaSquares[10][2] = ["2"]
    areaSquares[10][3] = ["2"]
    areaSquares[11][3] = ["a2", [2]]

    areaSquares[9][7] = ["a1", [6]]
    areaSquares[10][7] = ["2"]
    areaSquares[10][6] = ["2"]
    areaSquares[11][7] = ["a2", [2]]
    areaSquares[11][6] = ["2"]
    areaSquares[11][5] = ["a2", [5]]


def set_6test_area():
    clear_area(areaOpen)
    clear_area(areaSquares)
    fill_area(areaSquares, "e2")

    areaSquares[1][3] = ["a1", [6]]
    areaSquares[2][2] = ["a1", [8]]
    areaSquares[2][4] = ["a1", [1]]
    areaSquares[3][3] = ["a1", [3]]

    areaSquares[5][1] = ["a2", [5]]
    areaSquares[5][2] = ["2"]
    areaSquares[5][3] = ["a2", [7]]
    areaSquares[6][1] = ["2"]

    areaSquares[6][3] = ["2"]
    areaSquares[7][1] = ["a2", [2]]
    areaSquares[7][2] = ["2"]
    areaSquares[7][3] = ["a2", [4]]

    areaSquares[5][7] = ["a1", [8]]
    areaSquares[6][8] = ["2"]
    areaSquares[7][9] = ["a1", [6]]
    areaSquares[8][8] = ["2"]
    areaSquares[9][7] = ["a1", [1]]
    areaSquares[8][6] = ["2"]
    areaSquares[7][5] = ["a1", [3]]
    areaSquares[6][6] = ["2"]


def set_7test_area():
    clear_area(areaOpen)
    clear_area(areaSquares)
    fill_area(areaSquares, "e2")

    areaSquares[2][2] = ["a2", [5]]
    areaSquares[2][3] = ["a3", [4, 5]]
    areaSquares[2][4] = ["a2", [4]]

    areaSquares[1][6] = ["a2", [7]]
    areaSquares[2][6] = ["a3", [2, 7]]
    areaSquares[3][6] = ["a2", [2]]

    areaSquares[4][3] = ["a1", [6]]
    areaSquares[5][2] = ["a4", [3, 6]]
    areaSquares[6][1] = ["a1", [3]]

    areaSquares[8][1] = ["a1", [8]]
    areaSquares[9][2] = ["a4", [1, 8]]
    areaSquares[10][3] = ["a1", [1]]

    areaSquares[5][6] = ["a2", [7]]
    areaSquares[6][5] = ["a2", [5]]
    areaSquares[6][6] = ["a6", [2, 4, 5, 7]]
    areaSquares[6][7] = ["a2", [4]]
    areaSquares[7][6] = ["a2", [2]]

    areaSquares[9][5] = ["a1", [8]]
    areaSquares[9][7] = ["a1", [6]]
    areaSquares[10][6] = ["a5", [1, 3, 6, 8]]
    areaSquares[11][5] = ["a1", [3]]
    areaSquares[11][7] = ["a1", [1]]


def set_8test_area():
    clear_area(areaOpen)
    clear_area(areaSquares)
    fill_area(areaSquares, "e2")

    areaSquares[2][4] = ["a1", [6]]
    areaSquares[3][2] = ["a2", [5]]
    areaSquares[3][3] = ["a7", [3, 4, 7]]
    areaSquares[4][3] = ["a2", [2]]

    areaSquares[2][7] = ["a1", [8]]
    areaSquares[3][8] = ["a7", [1, 7, 5]]
    areaSquares[3][9] = ["a2", [4]]
    areaSquares[4][8] = ["a2", [2]]

    areaSquares[7][3] = ["a2", [7]]
    areaSquares[8][2] = ["a2", [5]]
    areaSquares[8][3] = ["a7", [8, 2, 4]]
    areaSquares[9][4] = ["a1", [1]]

    areaSquares[7][8] = ["a2", [7]]
    areaSquares[8][8] = ["a7", [6, 2, 5]]
    areaSquares[8][9] = ["a2", [4]]
    areaSquares[9][7] = ["a1", [3]]


def set_9test_area():
    clear_area(areaOpen)
    clear_area(areaSquares)
    fill_area(areaSquares, "e2")

    areaSquares[2][2] = ["a6", [2, 4, 5, 7]]
    areaSquares[3][3] = ["a6", [2, 4, 5, 7]]
    areaSquares[2][3] = ["a6", [2, 4, 5, 7]]
    areaSquares[3][2] = ["a6", [2, 4, 5, 7]]

    areaSquares[2][6] = ["a7", [6, 2, 5]]
    areaSquares[3][5] = ["a7", [3, 4, 7]]

    areaSquares[5][2] = ["a2", [5]]
    areaSquares[5][3] = ["a3", [4, 5]]

    areaSquares[6][5] = ["a4", [3, 6]]
    areaSquares[5][6] = ["a4", [3, 6]]

    areaSquares[7][3] = ["a3", [4, 5]]
    areaSquares[7][2] = ["a3", [2, 7]]
    areaSquares[8][2] = ["a3", [4, 5]]
    areaSquares[8][3] = ["a3", [2, 7]]

    areaSquares[8][5] = ["a3", [4, 5]]
    areaSquares[8][6] = ["a3", [4, 5]]

    areaSquares[10][2] = ["a7", [1, 5, 7]]
    areaSquares[10][3] = ["a7", [3, 4, 7]]
    areaSquares[11][2] = ["a7", [6, 2, 5]]
    areaSquares[11][3] = ["a7", [8, 2, 4]]

    areaSquares[2][9] = ["a5", [1, 3, 6, 8]]
    areaSquares[2][11] = ["a5", [1, 3, 6, 8]]
    areaSquares[3][10] = ["a5", [1, 3, 6, 8]]
    areaSquares[4][9] = ["a5", [1, 3, 6, 8]]
    areaSquares[4][11] = ["a5", [1, 3, 6, 8]]


def set_10test_area():
    clear_area(areaOpen)
    clear_area(areaSquares)
    fill_area(areaSquares, "e2")

    areaSquares[2][2] = ["a6", [2, 4, 5, 7]]
    areaSquares[2][3] = ["2"]
    areaSquares[2][4] = ["a6", [2, 4, 5, 7]]
    areaSquares[3][2] = ["2"]

    areaSquares[3][4] = ["2"]
    areaSquares[4][2] = ["a6", [2, 4, 5, 7]]
    areaSquares[4][3] = ["2"]
    areaSquares[4][4] = ["a6", [2, 4, 5, 7]]

    areaSquares[6][2] = ["a7", [1, 5, 7]]
    areaSquares[6][3] = ["2"]
    areaSquares[6][4] = ["a7", [3, 4, 7]]
    areaSquares[7][2] = ["2"]

    areaSquares[7][4] = ["2"]
    areaSquares[8][2] = ["a7", [6, 2, 5]]
    areaSquares[8][3] = ["2"]
    areaSquares[8][4] = ["a7", [8, 2, 4]]

    areaSquares[10][2] = ["a2", [5]]
    areaSquares[10][3] = ["2"]
    areaSquares[10][4] = ["a3", [4, 5]]

    areaSquares[1][8] = ["a7", [6, 2, 5]]
    areaSquares[2][7] = ["2"]
    areaSquares[3][6] = ["a7", [3, 4, 7]]

    areaSquares[5][8] = ["a4", [3, 6]]
    areaSquares[6][7] = ["2"]
    areaSquares[7][6] = ["a4", [3, 6]]

    areaSquares[10][6] = ["a3", [4, 5]]
    areaSquares[10][7] = ["2"]
    areaSquares[10][8] = ["a3", [4, 5]]


def set_11test_area():
    clear_area(areaOpen)
    clear_area(areaSquares)
    fill_area(areaSquares, "e2")

    areaSquares[4][4] = ["a5", [1, 3, 6, 8]]
    areaSquares[5][5] = ["2"]
    areaSquares[6][6] = ["a5", [1, 3, 6, 8]]
    areaSquares[7][7] = ["2"]
    areaSquares[8][8] = ["a5", [1, 3, 6, 8]]

    areaSquares[4][8] = ["a5", [1, 3, 6, 8]]
    areaSquares[5][7] = ["2"]
    areaSquares[7][5] = ["2"]
    areaSquares[8][4] = ["a5", [1, 3, 6, 8]]


print("\033[36m{}\033[0m".format("\n☸ Игра началась ☸"))

way_pawn = []

pygame.display.set_caption("Thousand devils")
pygame.display.set_icon(pygame.image.load("IMG/empty1.png"))

clear_area(areaOpen)
clear_area(areaSquares)

set_1test_area()

print_area(areaSquares, "Массив", ps="Поле")
print_area(areaSquares, "Поле", ps="Поле")
show_area(areaSquares, areaOpen)

game_mode = "select"  # select — выбор пешки, move — ход пешкой
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
            if time.time() - temp_time < time_tap:
                if event.button == 1:
                    mouse_click(event.pos, "Y", time.time() - temp_time)
                if event.button == 3:
                    mouse_click_cancel_select(event.pos, time.time() - temp_time)
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

            elif event.key == pygame.K_0:
                set_2test_area()
            elif event.key == pygame.K_1:
                set_3test_area()
            elif event.key == pygame.K_2:
                set_4test_area()
            elif event.key == pygame.K_3:
                set_5test_area()
            elif event.key == pygame.K_4:
                set_6test_area()
            elif event.key == pygame.K_5:
                set_7test_area()
            elif event.key == pygame.K_6:
                set_8test_area()
            elif event.key == pygame.K_7:
                set_9test_area()
            elif event.key == pygame.K_8:
                set_10test_area()
            elif event.key == pygame.K_9:
                set_11test_area()

    clock.tick(fps)
