# import math
# import random
import pygame
import time
from random import choice
from typing import Any

window_height = 800
window_width = window_height * 16 / 9
fps = 60

scope = 50
place_x = 500
place_y = 500
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

way_pawn = []

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
RobotoBold = pygame.font.Font("font/RobotoMono-Bold.ttf", 24)
RobotoRegular = pygame.font.Font("font/RobotoMono-Regular.ttf", 24)

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

boats = [["R", [3, 3], False], ["W", [6, 11], False], ["Y", [7, 7], False], ["B", [7, 7], False]]

pawns = [{"color": "R", "last": [3, 3], "current": [3, 3], "select": False},
         {"color": "W", "last": [6, 11], "current": [12, 6], "select": False},
         {"color": "W", "last": [7, 7], "current": [7, 7], "select": False},
         ]


def kill_pawn(x: int, y: int, color: str) -> bool:
    for pawn in pawns:
        if pawn["color"] == color and \
                pawn["current"][0] == x and \
                pawn["current"][1] == y:
            pawns.remove(pawn)
            return True
    return False


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
                line = line \
                       + str(area[y][x][0]) \
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
    set_corners()
    temp_squares = squares.copy()
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
                        else:
                            area[y][x][0] = chosen
                            break


def print_area_window(text: str, coord_xy: tuple):
    line = RobotoBold.render(text, True, text_color, bg_color)
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
    global scope, place_x, place_y
    print(f"stroke: {coords_xy}")
    for coord_xy in coords_xy:
        pygame.draw.rect(window, color,
                         (coord_xy[0] * scope + place_x,
                          coord_xy[1] * scope + place_y,
                          scope, scope), 2)


def mark_fill_squares(coords_xy: list, color: tuple):
    global scope, place_x, place_y
    print(f"fill: {coords_xy}")
    square = pygame.Surface((scope, scope), pygame.SRCALPHA)
    square.fill(color)
    for coord_xy in coords_xy:
        window.blit(square,
                    (coord_xy[0] * scope + place_x,
                     coord_xy[1] * scope + place_y))


def quantity_step_arrow(x: int, y: int, used_steps: set, directions: list):
    print(f"↗ Проверка стрелки:  "
          f"{x}, {y}{' ' * (4 - (x // 10 + y // 10))}{used_steps}")

    for digit in directions:
        new_x = x + digit2delta[digit][0]
        new_y = y + digit2delta[digit][1]
        if 0 <= new_x < len(areaSquares) and \
                0 <= new_y < len(areaSquares):
            if areaOpen[new_y][new_x][0] == 1:
                if "a" in areaSquares[new_y][new_x][0] and (new_x, new_y) not in used_steps:
                    used_steps.add((new_x, new_y))
                    quantity_step_arrow(new_x, new_y, used_steps, areaSquares[new_y][new_x][1])
                elif areaSquares[new_y][new_x][0] == "S" and (new_x, new_y) not in used_steps:
                    used_steps.add((new_x, new_y))
                elif (new_x, new_y) not in used_steps:
                    quantity_step(new_x, new_y, digit, used_steps)
            else:
                used_steps.add((new_x, new_y))


def quantity_step(x: int, y: int, digit: int, used_steps: set, mode="Field"):  # Field — Поле, Coast — берег
    print(f"☐ Проверка шага:     "
          f"{x}, {y}{' ' * (4 - (x // 10 + y // 10))}{used_steps}")

    if 0 <= x < len(areaSquares) and 0 <= y < len(areaSquares):
        if areaOpen[y][x][0] == 1:
            if areaSquares[y][x][0] == "2":
                new_x = x + digit2delta[digit][0]
                new_y = y + digit2delta[digit][1]
                quantity_step(new_x, new_y, digit, used_steps)
            elif "a" in areaSquares[y][x][0]:
                quantity_step_arrow(x, y, used_steps, areaSquares[y][x][1])
            elif (x, y) not in used_steps and \
                    areaSquares[y][x][0] == "S" and \
                    mode == "Coast":
                used_steps.add((x, y))
            elif (x, y) not in used_steps and \
                    areaSquares[y][x][0] != "c" and \
                    areaSquares[y][x][0] != "S" and \
                    mode == "Field":
                used_steps.add((x, y))
        elif areaOpen[y][x][0] == 0 and mode == "Field":
            used_steps.add((x, y))


def quantity_steps(x: int, y: int) -> int:
    mode = "Field"
    checked_steps = [1, 2, 3, 4, 5, 6, 7, 8]
    used_steps = set()
    extra_quantity = 0
    if 0 <= x < len(areaSquares) and 0 <= y < len(areaSquares):
        if areaSquares[y][x][0] == "S":
            mode = "Coast"  # True, если не использовали
        elif areaSquares[y][x][0] == "p" and areaSquares[y][x][1]:
            for p_y in range(0, len(areaOpen)):
                for p_x in range(0, len(areaOpen)):
                    if areaOpen[p_y][p_x][0] == 1 and \
                            areaSquares[p_y][p_x][0] != "S":
                        used_steps.add((p_x, p_y))
        elif areaSquares[y][x][0] == "h":
            checked_steps = [9, 10, 11, 12, 13, 14, 15, 16]
        elif "a" in areaSquares[y][x][0]:
            checked_steps = areaSquares[y][x][1]
        for step in checked_steps:
            quantity_step(x + digit2delta[step][0],
                          y + digit2delta[step][1],
                          step, used_steps, mode=mode)
    for step in used_steps:
        if "a" in areaSquares[step[1]][step[0]][0] and \
                areaOpen[step[1]][step[0]][0] == 1:
            extra_quantity += 1
    used_steps = list(used_steps)
    print_area(used_steps, "Строка", ps="Координаты, куда ходить")
    mark_fill_squares(used_steps, mark_select_color)
    return len(used_steps) - extra_quantity


def check_steps(x: int, y: int):
    mode = "Field"
    checked_steps = [1, 2, 3, 4, 5, 6, 7, 8]
    allowed_steps = set()
    extra_steps = set()
    if 0 <= x < len(areaSquares) and 0 <= y < len(areaSquares):
        if areaSquares[y][x][0] == "S":
            mode = "Coast"
        elif areaSquares[y][x][0] == "h":
            checked_steps = [9, 10, 11, 12, 13, 14, 15, 16]
        elif areaSquares[y][x][0] == "p":
            if areaSquares[y][x][1]:  # True, если не использовали
                for p_y in range(0, len(areaOpen)):
                    for p_x in range(0, len(areaOpen)):
                        if areaOpen[p_y][p_x][0] == 1 and \
                                areaSquares[p_y][p_x][0] != "S":
                            allowed_steps.add((p_x, p_y))
        elif "a" in areaSquares[y][x][0]:
            checked_steps = areaSquares[y][x][1]
        for step in checked_steps:
            if 0 <= x + digit2delta[step][0] < len(areaSquares) and \
                    0 <= y + digit2delta[step][1] < len(areaSquares):
                allowed_steps.add((x + digit2delta[step][0], y + digit2delta[step][1]))
    for step in allowed_steps:
        if "a" in areaSquares[step[1]][step[0]][0] and \
                areaOpen[step[1]][step[0]][0] == 1:
            extra_steps.add(step)
    allowed_steps -= extra_steps
    allowed_steps = list(allowed_steps)
    print_area(allowed_steps, "Строка", ps="Координаты, куда ходить")
    return allowed_steps


def mouse_click_cancel_select(coord_xy: tuple, delay: float):
    global way_pawn, scope, place_x, place_y, game_mode, pawns, way_pawn
    x = (coord_xy[0] - place_x) // scope
    y = (coord_xy[1] - place_y) // scope
    if 0 <= x < len(areaSquares) and 0 <= y < len(areaSquares):
        for pawn in pawns:
            if pawn["select"] and \
                    x == pawn["current"][0] and \
                    y == pawn["current"][1]:
                pawn["select"] = False
                game_mode = "select"
                way_pawn = []
                print("\033[35m{}\033[0m".format(f"Отмена выбора пешки:         "
                                                 f"{x}, {y}{' ' * (4 - (x // 10 + y // 10))}{areaSquares[y][x]}"
                                                 f"{' ' * (30 - len(str(areaSquares[y][x])))}"
                                                 f"Δt {delay}"))
        show_area(areaSquares, areaOpen)


def mouse_click_select(x: int, y: int, color: str, delay: float) -> list:
    global game_mode, pawns
    if 0 <= x < len(areaSquares) and 0 <= y < len(areaSquares):
        for pawn in pawns:
            if pawn["color"] == color and \
                    x == pawn["current"][0] and \
                    y == pawn["current"][1]:
                pawn["select"] = True
                game_mode = "move"
                print("\033[35m{}\033[0m".format(f"Выбрана пешка:         "
                                                 f"{x}, {y}{' ' * (4 - (x // 10 + y // 10))}{areaSquares[y][x]}"
                                                 f"{' ' * (30 - len(str(areaSquares[y][x])))}"
                                                 f"Δt {delay}"))
                if quantity_steps(x, y) == 0:
                    kill_pawn(x, y, color)
                else:
                    return check_steps(x, y)


def mouse_click_move(x: int, y: int, delay: float):
    global game_mode, pawns, way_pawn
    if 0 <= x < len(areaSquares) and 0 <= y < len(areaSquares) and way_pawn:
        for step in way_pawn:
            if x == step[0] and y == step[1]:
                for pawn in pawns:
                    if pawn["select"]:
                        pawn["select"] = False
                        pawn["last"] = [pawn["current"][0], pawn["current"][1]]
                        pawn["current"] = [x, y]
                        game_mode = "select"
                        open_square(x, y)
                        way_pawn = []
                        print("\033[35m{}\033[0m".format(f"Ход пешки:           "
                                                         f"{x}, {y}{' ' * (4 - (x // 10 + y // 10))}{areaSquares[y][x]}"
                                                         f"{' ' * (30 - len(str(areaSquares[y][x])))}"
                                                         f"Δt {delay}"))


def mouse_click(coord_xy: tuple, color: str, delay: float):
    global way_pawn, scope, place_x, place_y, game_mode
    x = (coord_xy[0] - place_x) // scope
    y = (coord_xy[1] - place_y) // scope
    if game_mode == "select":
        way_pawn = mouse_click_select(x, y, color, delay)
    elif game_mode == "move":
        mouse_click_move(x, y, delay)


def show_area(area: list, opened: list):
    global scope, way_pawn
    clear_window()
    square_temp = pygame.transform.scale(frame, (scope * 13, scope * 13))
    window.blit(square_temp, (place_x, place_y))
    for y in range(0, len(area)):
        for x in range(0, len(area[y])):
            if opened[y][x][0] == 1 and area[y][x][0] != "S":
                square_temp = pygame.transform.scale(squares_img_name[area[y][x][0]], (scope, scope))
                if area[y][x][0] == "g" or "a" in area[y][x][0]:
                    square_temp = pygame.transform.rotate(square_temp,
                                                          int(digit2degrees[area[y][x][1][0]]))
                window.blit(square_temp, (x * scope + place_x, y * scope + place_y))
            elif opened[y][x][0] == 0 and area[y][x][0] != "S":
                square_temp = pygame.transform.scale(empty, (scope, scope))
                window.blit(square_temp, (x * scope + place_x, y * scope + place_y))
    mark_stroke_squares(way_pawn, mark_step_color)

    square_temp = pygame.transform.scale(boat, (scope, scope))
    window.blit(square_temp, (0 * scope + place_x, 6 * scope + place_y))
    square_temp = pygame.transform.scale(boat, (scope, scope))
    window.blit(square_temp, (6 * scope + place_x, 0 * scope + place_y))
    square_temp = pygame.transform.scale(boat, (scope, scope))
    window.blit(square_temp, (12 * scope + place_x, 6 * scope + place_y))
    square_temp = pygame.transform.scale(boat, (scope, scope))
    window.blit(square_temp, (6 * scope + place_x, 12 * scope + place_y))

    for pawn in pawns:
        pygame.draw.circle(window, pawn2color[pawn["color"]],
                           (pawn["current"][0] * scope + scope / 2 + place_x,
                            pawn["current"][1] * scope + scope / 2 + place_y),
                           scope / 4)


pygame.display.set_caption("Thousand devils")
pygame.display.set_icon(pygame.image.load("IMG/empty1.png"))

clear_area(areaOpen)
clear_area(areaSquares)

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
                    mouse_click(event.pos, "W", time.time() - temp_time)
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
    clock.tick(fps)
