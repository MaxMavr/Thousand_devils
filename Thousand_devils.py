# import math
# import random
import pygame
import time
from random import choice
from typing import Any

window_height = 800
window_width = window_height * 16 / 9

fps = 60
scope = 95
place_x = 110
place_y = -450
time_tap = 0.17
way_pawn = []

# Цвета
bg_color = (255, 255, 255)
text_color = (0, 0, 0)

# mark_step_color = (139, 0, 139, 255 / 2)
mark_step_color = (50, 205, 50, 255 / 2)
mark_select_color = (0, 255, 0, 255 / 1.5)
mark_frame_color = (0, 128, 0)

mark_block_color = (255, 0, 0)

pawn_yellow = (255, 215, 0)
pawn_black = (30, 30, 30)
pawn_white = (245, 245, 245)
pawn_red = (170, 0, 0)

pawn_select_color = (50, 205, 50)

# white = (255, 255, 255)
# dark_blue_a = (0, 0, 139, 255/2)
# dark_blue = (0, 0, 139, 255)
# deep_pink_a = (255, 20, 147, 255/2)


pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)
pygame.display.set_caption("Thousand devils")
pygame.display.set_icon(pygame.image.load("IMG/empty1.png"))

print("\033[36m{}\033[0m".format("\n☸ Игра началась ☸"))

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
boat_img = pygame.image.load("IMG/boat.png").convert()
sea = pygame.image.load("IMG/open.png").convert()
frame = pygame.image.load("IMG/frame.png").convert_alpha()

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
squares_img_name = {"e1": empty1, "e2": empty2, "e3": empty3, "e4": empty4,
                    "a1": arrow1, "a2": arrow2, "a3": arrow3, "a4": arrow4, "a5": arrow5, "a6": arrow6, "a7": arrow7,
                    "h": horse,
                    "t2": turntable2, "t3": turntable3, "t4": turntable4, "t5": turntable5,
                    "2": ice, "tc": trap, "c": crocodile, "w": ogre,
                    "f": fortress, "r": aborigine,
                    "m1": gold1, "m2": gold2, "m3": gold3, "m4": gold4, "m5": gold5, "mc": gold,
                    "tk": swearword, "p": plane,
                    "b": balloon, "g": gun, "l": lighthouse,
                    "F": friday, "B": bengunn, "M": missionary,
                    "v1": bottles1, "v2": bottles2, "v3": bottles3,
                    "d": cave, "tv": barrel,
                    "q": earthquake, "j": jungles, "m": grass
                    }


class Area:
    def __init__(self, name_file):
        self.opened, self.squares, self.moneys = [], [], []

        if not file2area(name_file):
            exit()

        setup_dict = file2area(name_file)

        area = setup_dict["area"]
        quantity_boats = setup_dict["quantity_boats"]
        quantity_pawns = setup_dict["quantity_pawns"]
        start_boat = setup_dict["start_boat"]
        pawn2color = setup_dict["pawn2color"]
        boat_start_coord_xy = setup_dict["boat_start_coord_xy"]
        squares = setup_dict["squares"]

        for y in range(0, length_y):
            x_opened, x_squares, x_moneys = [], [], []
            for x in range(0, length_x):
                x_opened.append(False)
                x_squares.append([])
                x_moneys.append(0)
            self.opened.append(x_opened)
            self.squares.append(x_squares)
            self.moneys.append(x_moneys)

    def inside_area(self, x: int, y: int) -> bool:
        # null = "n"
        return 0 <= y < len(self.squares) and \
               0 <= x < len(self.squares[y]) and \
               self.get_square(x, y)[0] != "n"

    def get_open(self, x: int, y: int) -> bool:
        return self.opened[y][x]

    def get_square(self, x: int, y: int) -> list:
        return self.squares[y][x]

    def get_money(self, x: int, y: int) -> int:
        return self.moneys[y][x]

    def set_open(self, x: int, y: int, value: bool):
        self.opened[y][x] = value

    def set_square(self, x: int, y: int, value: list):
        self.squares[y][x] = value

    def set_money(self, x: int, y: int, value: int):
        self.moneys[y][x] = value

    def clear_area(self):
        for y in range(0, len(self.squares)):
            for x in range(0, len(self.squares[y])):
                if self.squares[y][x][0] != "S":
                    self.set_square(x, y, [0])

    def fill_area(self, value: list):
        for y in range(0, len(self.squares)):
            for x in range(0, len(self.squares[y])):
                if self.squares[y][x][0] != "S":
                    self.set_square(x, y, value)

    def mix_area(self):
        self.clear_area()
        test_set_corners()

        temp_squares = squares.copy()
        den_coords_xy = []

        for y in range(0, len(self.squares)):
            for x in range(0, len(self.squares[y])):
                if self.squares[y][x][0] != "S" and self.squares[y][x][0] != "n":
                    while True:
                        chosen = choice(list(temp_squares.keys()))
                        if temp_squares[chosen] != 0:
                            temp_squares[chosen] -= 1
                            if chosen == "g":
                                self.squares[y][x] = ["g", choice([[2], [4], [5], [7]])]
                                break
                            elif chosen == "a1":
                                self.squares[y][x] = ["a1", choice([[1], [3], [6], [8]])]
                                break
                            elif chosen == "a2":
                                self.squares[y][x] = ["a2", choice([[2], [4], [5], [7]])]
                                break
                            elif chosen == "a3":
                                self.squares[y][x] = ["a3", choice([[4, 5], [2, 7]])]
                                break
                            elif chosen == "a4":
                                self.squares[y][x] = ["a4", choice([[1, 8], [3, 6]])]
                                break
                            elif chosen == "a5":
                                self.squares[y][x] = ["a5", [1, 3, 6, 8]]
                                break
                            elif chosen == "a6":
                                self.squares[y][x] = ["a6", [2, 4, 5, 7]]
                                break
                            elif chosen == "a7":
                                self.squares[y][x] = ["a7", choice([[1, 5, 7], [3, 4, 7], [6, 5, 2], [8, 4, 2]])]
                                break
                            elif chosen == "p":
                                self.squares[y][x] = ["p", True]
                                break
                            elif chosen == "q":
                                self.squares[y][x] = ["q", True]
                                break
                            elif chosen == "l":
                                self.squares[y][x] = ["l", 3]
                                break
                            elif chosen[0] == "v":
                                self.squares[y][x] = [chosen, True]
                                break
                            elif chosen == "d":
                                den_coords_xy.append((x, y))
                                break
                            else:
                                self.squares[y][x][0] = chosen
                                break
        for den_coord_xy in den_coords_xy:
            self.squares[den_coord_xy[1]][den_coord_xy[0]] = ["d", tuple(den_coords_xy)]

    def earthquake(self):
        quantity_swaps = 2
        closed = []
        print(f"☯ Землетрясение:")
        for y in range(0, len(self.squares)):
            for x in range(0, len(self.squares[y])):
                if not self.opened[y][x]:
                    closed.append((x, y))
        if len(closed) >= quantity_swaps * 2:
            for i in range(quantity_swaps):
                chosen1 = choice(closed)
                chosen2 = choice(closed)
                closed.remove(chosen1)
                closed.remove(chosen2)

                square1 = self.get_square(chosen1[0], chosen1[1])
                self.set_square(chosen1[0], chosen1[1], square1)
                square2 = self.get_square(chosen2[0], chosen2[1])
                self.set_square(chosen2[0], chosen2[1], square2)

                print(f"  {chosen1[0]}, {chosen1[1]}"
                      f"{' ' * (4 - (chosen1[0] // 10 + chosen1[1] // 10))}{square1}"
                      f"   ◀ ▶   "
                      f"{chosen2[0]}, {chosen2[1]}"
                      f"{' ' * (4 - (chosen1[0] // 10 + chosen1[1] // 10))}{square2}")

    def flight(self) -> set:
        allowed_steps = set()
        for y in range(0, len(self.squares)):
            for x in range(0, len(self.squares[y])):
                if self.opened and \
                        self.squares[y][x][0] != "S" and \
                        self.squares[y][x][0] != "c" and \
                        self.squares[y][x][0] != "2":
                    allowed_steps.add((x, y))
        return allowed_steps

    def loop_search(start_x: int, start_y: int) -> bool:
        def check_arrow(coord_xy: tuple):
            nonlocal used_steps

            x = coord_xy[0]
            y = coord_xy[1]

            # print(f"↗ Проверка стрелки:  "
            #       f"{x}, {y}{' ' * (4 - (x // 10 + y // 10))}{areaSquares[y][x][1]}")

            for digit in areaSquares[y][x][1]:
                new_x = x + digit2delta[digit][0]
                new_y = y + digit2delta[digit][1]
                if 0 <= new_x < len(areaSquares) and \
                        0 <= new_y < len(areaSquares) and \
                        (new_x, new_y) not in used_steps:
                    if areaOpen[new_y][new_x][0] == 1:
                        if "a" in areaSquares[new_y][new_x][0]:
                            used_steps.add((new_x, new_y))
                            check_arrow((new_x, new_y))
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

            if 0 <= coord_xy[0] < len(areaSquares) and \
                    0 <= coord_xy[1] < len(areaSquares):
                if areaOpen[coord_xy[1]][coord_xy[0]][0] == 1:
                    if areaSquares[y][x][0] == "2":
                        check_step((x + (x - old_x), y + (y - old_y)), (x, y))
                    elif "a" in areaSquares[y][x][0] and (x, y) not in used_steps:
                        used_steps.add((x, y))
                        check_arrow((x, y))
                    elif areaSquares[y][x][0] != "c" and (x, y) not in used_steps:
                        used_steps.add((x, y))
                elif areaOpen[y][x][0] == 0 and (x, y) not in used_steps:
                    used_steps.add((x, y))

            # print(f"☐ Проверка шага:     "
            #       f"{x}, {y}"
            #       f"{' ' * (4 - (x // 10 + y // 10))}{(x, y) in used_steps}")

        checked_digits = [1, 2, 3, 4, 5, 6, 7, 8]
        checked_steps = []
        used_steps = set()
        extra_quantity = 0
        if 0 <= start_x < len(areaSquares) and \
                0 <= start_y < len(areaSquares):

            if "a" in areaSquares[start_y][start_x][0]:
                checked_digits = areaSquares[start_y][start_x][1]

            for digit in checked_digits:  # Получаем из направлений координаты
                checked_steps.append((start_x + digit2delta[digit][0],
                                      start_y + digit2delta[digit][1]))

            for step in checked_steps:  # Проверяем координаты
                check_step(step, (start_x, start_y))

        for step in used_steps:
            if ("a" in areaSquares[step[1]][step[0]][0] or
                areaSquares[step[1]][step[0]][0] == "2") and \
                    areaOpen[step[1]][step[0]][0] == 1:
                extra_quantity += 1
        used_steps = list(used_steps)
        # print_area(used_steps, "Строка", ps="Координаты, куда можно сходить")
        # mark_fill_squares(list(used_steps), mark_select_color)
        # show_area(areaSquares, areaOpen)
        return len(used_steps) - extra_quantity == 0


class Boat:
    def __init__(self, curr: list, alco: int):
        self.curr = curr
        self.alco = alco

    def info(self) -> str:
        return f"{self.curr} {self.alco}"


class Pawn:
    def __init__(self, last: list, curr: list, skip: int):
        self.last = last
        self.curr = curr
        self.skip = skip

    def info(self) -> str:
        return f"{self.last} {self.curr} {self.skip}"


class TheGameCycle:
    def __init__(self, cycle: list, start_player: str):
        self.cycle = cycle
        self.active_player = cycle.index(start_player)

    def set_next(self):
        if self.active_player == len(self.cycle) - 1:
            self.active_player = 0
        else:
            self.active_player += 1

    def get_current(self) -> str:
        return self.cycle[self.active_player]


class Players:
    def __init__(self, colors: dict, quantity_pawns: int):
        self.quantity_pawns = quantity_pawns
        self.selected_pawn = {'color': "", 'pawn': -1}
        self.players = {}
        for color in colors.keys():
            player = {'boat': Boat(colors[color], 0)}
            pawns = []
            for i in range(quantity_pawns):
                pawns.append(Pawn(colors[color], colors[color], 0))
            player['pawns'] = pawns
            self.players[color] = player

    def select(self, x: int, y: int, color: str) -> bool:
        for pawn in self.players[color]['pawns']:
            if x == pawn.curr[0] and y == pawn.curr[1]:
                self.selected_pawn['color'] = color
                self.selected_pawn['pawn'] = self.players[color]['pawns'].index(pawn)
                return True
        return False

    def cancel_select(self):
        self.selected_pawn['color'] = ""
        self.selected_pawn['pawn'] = -1

    def get_pawn(self, path2pawn: dict) -> Pawn:
        return self.players[path2pawn['color']]['pawns'][path2pawn['pawn']]

    def get_boat(self, path2pawn: dict) -> Boat:
        return self.players[path2pawn['color']]['boat']

    def get_select(self) -> dict:
        return self.selected_pawn

    def kill_pawn(self):
        print("\033[31m{}\033[0m".format(f"☠ Убита пешка:        "
                                         f"{', '.join(self.get_pawn(self.selected_pawn).curr)}"
                                         f"{self.selected_pawn['color']}"))

        self.players[self.selected_pawn['color']]['pawns'].pop(self.selected_pawn['pawn'])

    def kick_pawn(self, kicked_pawn: dict):
        print("\033[35m{}\033[0m".format(f"⎋ Пешка на корабле:  "
                                         f"{', '.join(self.get_pawn(kicked_pawn).curr)}"
                                         f"{kicked_pawn['color']}"))

        self.get_pawn(kicked_pawn).curr = [self.get_boat(kicked_pawn).curr[0],
                                           self.get_boat(kicked_pawn).curr[1]]
        self.get_pawn(kicked_pawn).skip = 0

    def drunk(self, area: Area):
        global game_mode, way_pawn
        if self.selected_pawn != {'color': "", 'pawn': -1}:
            if self.get_pawn(self.selected_pawn).skip != 0 and \
                    self.get_boat(self.selected_pawn).alco > 0:
                self.get_pawn(self.selected_pawn).skip = 0
                self.get_boat(self.selected_pawn).alco -= 1

                print(f"☺ Пешка нажралась:     "
                      f"{', '.join(self.get_pawn(self.selected_pawn).curr)}"
                      f"{' ' * (4 - (self.get_pawn(self.selected_pawn).curr[0] // 10 + self.get_pawn(self.selected_pawn).curr[1] // 10))}"
                      f"{area.get_square(self.get_pawn(self.selected_pawn).curr[0], self.get_pawn(self.selected_pawn).curr[1])}")

                print(f"𝕽 Запасы рома:         "
                      f"{self.selected_pawn['color']} {self.get_boat(self.selected_pawn).alco}")

    def reborn_pawn(self, area: Area):
        global way_pawn, game_mode

        if area.get_square(self.get_pawn(self.selected_pawn).curr[0],
                           self.get_pawn(self.selected_pawn).curr[1])[0] == "r":

            if len(self.players[self.selected_pawn['color']]['pawns']) < self.quantity_pawns:
                self.players[self.selected_pawn['color']]['pawns'].append(
                    Pawn(self.get_pawn(self.selected_pawn).last,
                         self.get_pawn(self.selected_pawn).curr,
                         self.get_pawn(self.selected_pawn).skip))

                print("\033[32m{}\033[0m".format(f"☮ Возрождена пешка: "
                                                 f"{', '.join(self.get_pawn(self.selected_pawn).curr)}"
                                                 f"{self.selected_pawn['color']}"))

                print("\033[32m{}\033[0m".format(f"  Пешек {len(self.players[self.selected_pawn['color']]['pawns'])}"
                                                 f" {'♟' * len(self.players[self.selected_pawn['color']]['pawns'])}"))
                self.cancel_select()
                game_mode = "select"
                way_pawn = []
            else:
                print("\033[32m{}\033[0m".format(f"  Нельзя иметь больше"
                                                 f" {self.quantity_pawns} пешек "
                                                 f" {'♟' * self.quantity_pawns}"))
        else:
            print("\033[32m{}\033[0m".format(f"Пешка не стоит на клетке возрождения"))

    def gunshot(self, x: int, y: int, area: Area):
        new_x = x
        new_y = y

        if area.get_square(x, y)[1][0] == 2:
            while area.get_square(new_x, new_y)[0] != "S":
                new_y -= 1
            self.get_pawn(self.selected_pawn).curr = [x, new_y]
        elif area.get_square(x, y)[1][0] == 4:
            while area.get_square(new_x, new_y)[0] != "S":
                new_x -= 1
            self.get_pawn(self.selected_pawn).curr = [new_x, y]
        elif area.get_square(x, y)[1][0] == 5:
            while area.get_square(new_x, new_y)[0] != "S":
                new_x += 1
            self.get_pawn(self.selected_pawn).curr = [new_x, y]
        elif area.get_square(x, y)[1][0] == 7:
            while area.get_square(new_x, new_y)[0] != "S":
                new_y += 1
            self.get_pawn(self.selected_pawn).curr = [x, new_y]

    def info(self) -> str:
        result_line = ""
        for player in self.players.keys():
            line = ""
            for pawn in self.players[player][1]:
                line += f"{pawn.info()}\n         "
            result_line += f'{player} Лодка: {self.players[player][0].info()}\n' \
                           f'  Пешки: {line}\n'
        return result_line


def file2area(name_file: str):
    print(f'⎙ Создание поля из файла "{name_file[:-4]}"')
    try:
        file = open(name_file, 'r')
    except:
        print("\033[31m{}\033[0m".format(f"Файла {name_file} не существует\n"))
        return False

    uncleaned = file.read()

    n_uncleaned = ""
    a_uncleaned = ""
    f_uncleaned = ""
    s_uncleaned = ""

    n_flag = False
    a_flag = False
    f_flag = False
    s_flag = False

    for in_piece in range(len(uncleaned)):
        if uncleaned[in_piece] == "$":
            if uncleaned[in_piece + 1] == "n":
                n_flag = True
            elif uncleaned[in_piece + 1] == "a":
                a_flag = True
            elif uncleaned[in_piece + 1] == "f":
                f_flag = True
            elif uncleaned[in_piece + 1] == "s":
                s_flag = True
            else:
                n_flag = False
                a_flag = False
                f_flag = False
                s_flag = False

        if n_flag and \
                uncleaned[in_piece] != "\n":
            n_uncleaned += uncleaned[in_piece]
        if uncleaned[in_piece] != " ":
            if a_flag:
                a_uncleaned += uncleaned[in_piece]
            elif f_flag:
                f_uncleaned += uncleaned[in_piece]
            elif s_flag:
                if uncleaned[in_piece] != "\n":
                    s_uncleaned += uncleaned[in_piece]

    name_area = n_uncleaned[2:]
    a_cleaned = a_uncleaned[2:]
    f_cleaned = f_uncleaned[2:]
    s_cleaned = s_uncleaned[2:]

    if name_area == "":
        print("\033[31m{}\033[0m".format(f"Неполный файл"
                                         f"Нет блока $n$ (Название)"))
        return False
    if a_cleaned == "":
        print("\033[31m{}\033[0m".format(f"Неполный файл"
                                         f"Нет блока $a$ (Поле)"))
        return False
    if f_cleaned == "":
        print("\033[31m{}\033[0m".format(f"Неполный файл"
                                         f"Нет блока $f$ (Настройка)"))
        return False
    if s_cleaned == "":
        print("\033[31m{}\033[0m".format(f"Неполный файл"
                                         f"Нет блока $s$ (Значение клеток)"))
        return False

    empty_row = True
    waste_row = True
    area = []
    area_x = []

    quantity_square_area = 0

    for piece in a_cleaned:
        if piece == "\n":
            if not (empty_row or waste_row):
                area.append(area_x)
            area_x = []
        elif piece == "S":
            empty_row = False
            waste_row = False
            area_x.append(["S"])
        elif piece == "O":
            empty_row = False
            waste_row = False
            area_x.append([0])
            quantity_square_area += 1
        elif piece == "n":
            waste_row = False
            area_x.append(["n"])

    for y in area:
        if len(y) != len(area[0]):
            print("\033[31m{}\033[0m".format(f"Поле не прямоугольное\n"
                                             f"Блок $a$, Строка: {area.index(y)}"))
            return False

    flip_area = []

    for i in range(len(area[0])):
        flip_area.append([])

    for y in range(len(area)):
        for x in range(len(area[y])):
            flip_area[x].append(area[y][x])

    waste_cols = []

    for y in range(len(flip_area)):
        waste_col = True
        for x in range(len(flip_area[y])):
            if flip_area[y][x][0] == 0 or \
                    flip_area[y][x][0] == "S":
                waste_col = False
                break
        if waste_col:
            waste_cols.append(y)

    for deleted in waste_cols:
        for y in range(len(area)):
            area[y].pop(deleted - waste_cols.index(deleted))

    flag_boats = False
    flag_pawns = False
    flag_start = False

    for piece in f_cleaned:
        if piece == "\n":
            break
        elif piece == "b":
            flag_boats = True
        elif piece == "p":
            flag_pawns = True
        elif piece == "s":
            flag_start = True

    if not flag_boats:
        print("\033[31m{}\033[0m".format(f"Нет количества кораблей\n"
                                         f"Блок $f$, Переменная: b"))
        return False
    if not flag_pawns:
        print("\033[31m{}\033[0m".format(f"Нет количества пешек\n"
                                         f"Блок $f$, Переменная: p"))
        return False
    if not flag_start:
        print("\033[31m{}\033[0m".format(f"Нет начального игрока\n"
                                         f"Блок $f$, Переменная: s"))
        return False

    key = ""
    facilities = {}

    for in_piece in range(len(f_cleaned)):
        if f_cleaned[in_piece] == "\n":
            f_cleaned = f_cleaned[in_piece + 1:]
            break
        elif f_cleaned[in_piece] == ":":
            key = f_cleaned[in_piece - 1]
            facilities[key] = ""
        elif f_cleaned[in_piece] == ",":
            key = ""
        elif key != "":
            facilities[key] += f_cleaned[in_piece]

    quantity_boats = 0
    quantity_pawns = 0
    start_boat = ""

    try:
        quantity_boats = int(facilities["b"])
        quantity_pawns = int(facilities["p"])
        start_boat = facilities["s"]
    except:
        print("\033[31m{}\033[0m".format(f"Количество лодок или пешек не число\n"
                                         f"Блок $f$"))
        return False

    pawn2color = {}
    boat_start_coord_xy = {}
    color = 0

    for i in range(quantity_boats):
        pos_start = 0
        pos_finish = 0
        line = ""
        for in_piece in range(len(f_cleaned)):
            if f_cleaned[in_piece] == "\n":
                f_cleaned = f_cleaned[in_piece + 1:]
                break
            elif f_cleaned[in_piece] == ":":
                color = f_cleaned[in_piece - 1]
            elif f_cleaned[in_piece] == "(":
                pos_start = in_piece + 1
            elif f_cleaned[in_piece] == ")":
                line = f_cleaned[pos_start:in_piece]

                s = 0
                temp = []
                separator = 0
                for il in range(len(line)):
                    if line[il] == ",":
                        separator += 1
                        temp.append(line[s:il])
                        s = il + 1
                    elif il == len(line) - 1:
                        temp.append(line[s:il + 1])
                if separator == 1:
                    boat_start_coord_xy[color] = temp
                if separator == 2:
                    pawn2color[color] = temp

    if len(pawn2color) != len(boat_start_coord_xy):
        print("\033[31m{}\033[0m".format(f"Количество цветов и координат старта различны\n"
                                         f"Цвета: {pawn2color}\n"
                                         f"Координаты начала: {boat_start_coord_xy}"))
        return False

    for key in pawn2color.keys():
        for i in range(len(pawn2color[key])):
            try:
                pawn2color[key][i] = int(pawn2color[key][i])
            except:
                print("\033[31m{}\033[0m".format(f"В вектор цвета не числа\n"
                                                 f"Цвет {key}, Вектор: {pawn2color[key]}"))
                return False
        pawn2color[key] = tuple(pawn2color[key])

    for key in boat_start_coord_xy.keys():
        for i in range(len(boat_start_coord_xy[key])):
            try:
                boat_start_coord_xy[key][i] = int(boat_start_coord_xy[key][i])
            except:
                print("\033[31m{}\033[0m".format(f"В вектор цвета не числа\n"
                                                 f"Цвет {key}, Вектор: {boat_start_coord_xy[key]}"))
                return False
        boat_start_coord_xy[key] = tuple(boat_start_coord_xy[key])

    key = ""
    squares = {}
    flag = False
    value = ""

    for in_piece in range(len(s_cleaned)):
        if s_cleaned[in_piece] == ":":
            squares[key] = ""
            value = ""
            flag = True
        elif s_cleaned[in_piece] == "," and flag:
            squares[key] = value
            key = ""
            flag = False
        elif in_piece == len(s_cleaned) - 1:
            value += s_cleaned[in_piece]
            squares[key] = value
        elif flag:
            value += s_cleaned[in_piece]
        elif not flag:
            key += s_cleaned[in_piece]

    for key in squares.keys():
        try:
            squares[key] = int(squares[key])
        except:
            print("\033[31m{}\033[0m".format(f"Количество клеток не число\n"
                                             f"Блок $s$, Клетка: {key}"))
            return False

    quantity_square_value = 0

    for value in squares.values():
        quantity_square_value += value

    if quantity_square_area != quantity_square_value:
        print("\033[31m{}\033[0m".format(f"Количество клеток на поле и количество значений клеток различны\n"
                                         f"Блок $a$, Количество: {quantity_square_area}\n"
                                         f"Блок $s$, Количество: {quantity_square_value}"))
        return False

    print("\033[32m".format(f"  Название карты:\n  {name_area}"))
    print(f"  Каркас поля:")
    for y in range(len(area)):
        line = ''
        for x in range(len(area[y])):
            line = line + str(area[y][x][0]) + ' '
        print(f"  {line}")
    print(f"  Количество кораблей:\n  {quantity_boats}")
    print(f"  Количество пешек:\n  {quantity_pawns}")
    print(f"  Старт-корабль:\n  {start_boat}")
    print(f"  Цвета кораблей:\n  {pawn2color}")
    print(f"  Координаты кораблей:\n  {boat_start_coord_xy}")

    print("\033[32m{}\033[0m".format(f"  Карточки:\n  {squares}"))

    return {"area": area,
            "quantity_boats": quantity_boats,
            "quantity_pawns": quantity_pawns,
            "start_boat": start_boat,
            "pawn2color": pawn2color,
            "boat_start_coord_xy": boat_start_coord_xy,
            "squares": squares}


def print_area(area: list, mode: str, ps=""):
    if mode == "Поле":
        print("\033[34m{}\033[0m".format(f"\n▦ Просмотр поля: {ps}"))
        print("\033[34m{}\033[0m".format("     0  1  2  3  4  5  6  7  8  9 10 11 12"))
        for y in range(0, len(area)):
            line = "  " + str(y) \
                   + " " * (3 - len(str(y)))
            for x in range(0, len(area[y])):
                line = line \
                       + str(area[y][x][0]) \
                       + " " * (3 - len(str(area[y][x][0])))
            print("\033[34m{}\033[0m".format(f"{line}"))

    elif mode == "Массив":
        print("\033[34m{}\033[0m".format(f"\n▥ Просмотр массива: {ps}"))
        for y in range(0, len(area)):
            print("\033[34m{}\033[0m".format(f"  {area[y]}"))

    elif mode == "Список":
        print("\033[34m{}\033[0m".format(f"\n▤ Просмотр списка: {ps}"))
        for y in range(0, len(area)):
            for x in range(0, len(area[y])):
                print("\033[34m{}\033[0m".format(f"  {area[y][x]}"))

    elif mode == "Строка":
        print("\033[34m{}\033[0m".format(f"▧ Просмотр строки: {ps}\n  {area}"))


def print_window(text: str, coord_xy: tuple):
    line = RobotoRegular.render(text, True, text_color, bg_color)
    window.blit(line, coord_xy)


def illuminate(x: int, y: int):
    global game_mode, pawn_select
    if areaSquares[pawns[pawn_select].curr[1]][pawns[pawn_select].curr[0]][1] >= 1:
        if game_mode == "lighthouse":
            if inside_field(x, y) and \
                    areaOpen[y][x][0] == 0:
                print(f"☄ Маяк открыл:         "
                      f"{x}, {y}{' ' * (4 - (x // 10 + y // 10))}"
                      f"{areaSquares[y][x]}")
                open_square(x, y)
                areaSquares[pawns[pawn_select].curr[1]][pawns[pawn_select].curr[0]][1] -= 1
                if areaSquares[pawns[pawn_select].curr[1]][pawns[pawn_select].curr[0]][1] == 0:
                    game_mode = "select"
                    pawn_select = -1
        else:
            game_mode = "lighthouse"
    else:
        game_mode = "select"
        pawn_select = -1


def change_scope(delta: int):
    global scope, place_x, place_y
    if 20 <= scope + delta <= 190:
        scope += delta
        # Компенсация изменения (Поле рисуется слева направо)
        place_x -= delta * 7
        place_y -= delta * 7
    print("\033[3m\033[37m{}\033[0m".format(f"  Масштаб:   {scope}"))


def change_place(delta: tuple):
    global place_x, place_y
    place_x += delta[0]
    place_y += delta[1]
    print("\033[3m\033[37m{}\033[0m".format(f"  Положение: {place_x}, {place_y}"))


def mark_stroke_squares(coords_xy: list, color: tuple):
    for coord_xy in coords_xy:
        pygame.draw.rect(window, color,
                         (coord_xy[0] * scope + place_x,
                          coord_xy[1] * scope + place_y,
                          scope, scope), 4)


def mark_fill_squares(coords_xy: list, color: tuple):
    square = pygame.Surface((scope, scope), pygame.SRCALPHA)
    square.fill(color)
    for coord_xy in coords_xy:
        window.blit(square,
                    (coord_xy[0] * scope + place_x,
                     coord_xy[1] * scope + place_y))


def mouse_click_cancel_select(coord_xy: tuple, delay: float):
    global way_pawn, game_mode, pawn_select
    x = (coord_xy[0] - place_x) // scope
    y = (coord_xy[1] - place_y) // scope
    if inside_field(x, y) and \
            x == pawns[pawn_select].curr[0] and \
            y == pawns[pawn_select].curr[1] and \
            "a" not in areaSquares[pawns[pawn_select].curr[1]][pawns[pawn_select].curr[0]][0] and \
            areaSquares[pawns[pawn_select].curr[1]][pawns[pawn_select].curr[0]][0] != "2" and \
            (areaSquares[pawns[pawn_select].curr[1]][pawns[pawn_select].curr[0]][0] != "l" or
             areaSquares[pawns[pawn_select].curr[1]][pawns[pawn_select].curr[0]][1] == 0):
        pawn_select = -1
        game_mode = "select"
        way_pawn = []
        print("\033[35m{}\033[0m".format(f"  Отмена выбора пешки: "
                                         f"{x}, {y}{' ' * (4 - (x // 10 + y // 10))}{areaSquares[y][x]}"
                                         f"{' ' * (50 - len(str(areaSquares[y][x])))}"
                                         f"Δt {delay}"))
        show_area(areaSquares, areaOpen)


def mouse_click_select(x: int, y: int, delay: float) -> list:
    global game_mode, pawn_select

    if inside_field(x, y) and \
            pawn_select != -1:

        game_mode = "move"
        print("\033[35m{}\033[0m".format(f"\n  Выбрана пешка:       "
                                         f"{x}, {y}{' ' * (4 - (x // 10 + y // 10))}{areaSquares[y][x]}"
                                         f"{' ' * (50 - len(str(areaSquares[y][x])))}"
                                         f"Δt {delay}"))
        if loop_search(x, y):
            kill_pawn()
        else:
            return check_steps(x, y)
    return []


def check_steps(x: int, y: int) -> list:
    global pawn_select, game_mode, rebirth
    checked_steps = [1, 2, 3, 4, 5, 6, 7, 8]
    allowed_steps = set()
    mode = "Field"
    if 0 <= x < len(areaSquares) and 0 <= y < len(areaSquares):
        if areaSquares[y][x][0] == "S":
            checked_steps = []

            if [x, y] == boats[pawns[pawn_select].boat_index].curr:
                mode = "Boat"
                condition = "None"

                for step in [2, 4, 5, 7]:
                    new_x = x + digit2delta[step][0]
                    new_y = y + digit2delta[step][1]

                    if inside_field(new_x, new_y):
                        if areaSquares[new_y][new_x][0] == "S":
                            if step == 2 or step == 7:
                                condition = "vertical"
                            elif step == 4 or step == 5:
                                condition = "horizontal"

                if inside_field(x - 1, y - 1) and areaSquares[y - 1][x - 1][0] == "S":
                    if condition == "vertical":
                        checked_steps = [4, 7]
                    elif condition == "horizontal":
                        checked_steps = [2, 5]

                elif inside_field(x + 1, y + 1) and areaSquares[y + 1][x + 1][0] == "S":
                    if condition == "vertical":
                        checked_steps = [2, 5]
                    elif condition == "horizontal":
                        checked_steps = [4, 7]

                elif inside_field(x + 1, y - 1) and areaSquares[y - 1][x + 1][0] == "S":
                    if condition == "vertical":
                        checked_steps = [5, 7]
                    elif condition == "horizontal":
                        checked_steps = [2, 4]

                elif inside_field(x - 1, y + 1) and areaSquares[y + 1][x - 1][0] == "S":
                    if condition == "vertical":
                        checked_steps = [2, 4]
                    elif condition == "horizontal":
                        checked_steps = [5, 7]

                else:
                    checked_steps = [2, 4, 5, 7]

            else:
                mode = "Coast"
                for step in [2, 4, 5, 7]:
                    new_x = x + digit2delta[step][0]
                    new_y = y + digit2delta[step][1]

                    if inside_field(new_x, new_y) and areaSquares[new_y][new_x][0] == "S":
                        checked_steps.append(step)

        elif areaSquares[y][x][0] == "r":
            rebirth = pawns[pawn_select]

        elif areaSquares[y][x][0] == "h":
            checked_steps = [9, 10, 11, 12, 13, 14, 15, 16]

        elif areaSquares[y][x][0] == "p" and areaSquares[y][x][1]:
            allowed_steps = flight()

        elif "t" in areaSquares[y][x][0]:
            if areaSquares[y][x][0] != "tk" and \
                    areaSquares[y][x][0] != "tc" and \
                    areaSquares[y][x][0] != "tv":
                if pawns[pawn_select].skip != 0:
                    return [(x, y)]
            if pawns[pawn_select].skip != 0 and \
                    areaSquares[y][x][0] == "tc":
                return []

        elif "a" in areaSquares[y][x][0]:
            checked_steps = areaSquares[y][x][1]

        for step in checked_steps:
            new_x = x + digit2delta[step][0]
            new_y = y + digit2delta[step][1]
            if inside_field(new_x, new_y):
                if areaOpen[new_y][new_x][0] == 1:
                    if mode == "Field" and \
                            areaSquares[new_y][new_x][0] != "c" and \
                            (areaSquares[new_y][new_x][0] != "S" or
                             [new_x, new_y] == boats[pawns[pawn_select].boat_index].curr):
                        allowed_steps.add((new_x, new_y))
                    if mode == "Coast" or mode == "Boat":
                        allowed_steps.add((new_x, new_y))

                elif areaOpen[new_y][new_x][0] == 0:
                    allowed_steps.add((new_x, new_y))

                if areaSquares[new_y][new_x][0] == "f" or \
                        areaSquares[new_y][new_x][0] == "r":
                    for pawn in pawns:
                        if pawn.curr == [new_x, new_y] and \
                                pawn.color != pawns[pawn_select].color:
                            allowed_steps.remove((new_x, new_y))
                            break

        if areaSquares[y][x][0] == "d":
            quantity_open = []
            for step in areaSquares[y][x][1]:
                if areaOpen[step[1]][step[0]][0] == 1:
                    quantity_open.append(step)
                    if step != (x, y):
                        allowed_steps.add(step)

            if len(quantity_open) < 2:
                return []

    print_area(list(allowed_steps), "Строка", ps="Координаты, куда ходить")
    return list(allowed_steps)


def mouse_click_move(x: int, y: int, delay: float):
    global game_mode, way_pawn, pawn_select

    if inside_field(x, y) and \
            way_pawn and \
            pawn_select != -1:

        for step in way_pawn:
            if x == step[0] and y == step[1]:
                pawns[pawn_select].last = [pawns[pawn_select].curr[0], pawns[pawn_select].curr[1]]
                pawns[pawn_select].curr = [x, y]
                open_square(x, y)

                if pawns[pawn_select].last == boats[pawns[pawn_select].boat_index].curr:
                    boat = boats[pawns[pawn_select].boat_index]

                    if inside_field(x, y) and areaSquares[y][x][0] == "S":
                        for pawn in pawns:
                            if pawn.curr == boat.curr and \
                                    pawn.color == boat.color:
                                pawn.last[0] = pawn.curr[0]
                                pawn.last[1] = pawn.curr[1]
                                pawn.curr[0] = x
                                pawn.curr[1] = y
                        boat.curr[0] = x
                        boat.curr[1] = y

                way_pawn = check_second_steps(x, y)

                print("\033[35m{}\033[0m".format(f"  Ход пешки:           "
                                                 f"{x}, {y}{' ' * (4 - (x // 10 + y // 10))}{areaSquares[y][x]}"
                                                 f"{' ' * (50 - len(str(areaSquares[y][x])))}"
                                                 f"Δt {delay}"))
                break


def check_second_steps(x: int, y: int) -> list:
    global game_mode, pawn_select, rebirth

    rebirth = None

    print("\033[33m{}\033[0m".format(f"  Проверка клетки:     "
                                     f"{x}, {y}{' ' * (4 - (x // 10 + y // 10))}{areaSquares[y][x]}"
                                     f"{' ' * (50 - len(str(areaSquares[y][x])))}"))
    steps = []
    if loop_search(x, y):
        kill_pawn()
        pawn_select = -1
        game_mode = "select"
        return []

    if "a" in areaSquares[y][x][0]:
        for digit in areaSquares[y][x][1]:
            steps.append((x + digit2delta[digit][0],
                          y + digit2delta[digit][1]))
        return steps

    elif "t" in areaSquares[y][x][0]:
        if areaSquares[y][x][0] != "tk" and \
                areaSquares[y][x][0] != "tc" and \
                areaSquares[y][x][0] != "tv":

            if pawns[pawn_select].skip != 0:
                pawns[pawn_select].skip -= 1

            if pawns[pawn_select].last != [x, y]:
                pawns[pawn_select].skip = int(areaSquares[y][x][0][1]) - 1  # Волшебная единица

        elif areaSquares[y][x][0] == "tc":
            pawns[pawn_select].skip = -1
            for pawn in pawns:
                if pawn.curr == [x, y] and \
                        pawn is not pawns[pawn_select] and \
                        pawn.color == pawns[pawn_select].color:
                    pawn.skip = 0
                    pawns[pawn_select].skip = 0
                    break

        print(f"◮ Пешка в ловушке:     "
              f"{pawns[pawn_select].curr[0]}, {pawns[pawn_select].curr[1]}{' ' * (4 - (x // 10 + y // 10))}"
              f"{areaSquares[pawns[pawn_select].curr[1]][pawns[pawn_select].curr[0]]}   "
              f"Нужно пройти: ∞" if pawns[pawn_select].skip == -1
              else f"◮ Пешка в ловушке:     "
                   f"{pawns[pawn_select].curr[0]}, {pawns[pawn_select].curr[1]}{' ' * (4 - (x // 10 + y // 10))}"
                   f"{areaSquares[pawns[pawn_select].curr[1]][pawns[pawn_select].curr[0]]}   "
                   f"Нужно пройти: {pawns[pawn_select].skip}")

    elif areaSquares[y][x][0] == "q" and \
            areaSquares[y][x][1]:
        earthquake()
        areaSquares[y][x][1] = False

    elif areaSquares[y][x][0] == "w":
        kill_pawn()

    elif areaSquares[y][x][0] == "b":
        kick_pawn(pawn_select)

    elif areaSquares[y][x][0][0] == "v" and \
            areaSquares[y][x][1]:
        boats[pawns[pawn_select].boat_index].alco += int(areaSquares[y][x][0][1])
        areaSquares[y][x][1] = False
        print(f"𝕽 Запасы рома:        "
              f"{boats[pawns[pawn_select].boat_index].alco} {pawns[pawn_select].color}")

    elif areaSquares[y][x][0] == "l":
        illuminate(-1, -1)
        return []

    elif areaSquares[y][x][0] == "2":
        if areaSquares[pawns[pawn_select].last[1]][pawns[pawn_select].last[0]][0] == "h":
            for digit in [9, 10, 11, 12, 13, 14, 15, 16]:
                steps.append((x + digit2delta[digit][0], y + digit2delta[digit][1]))
            return steps
        else:
            delta_x = pawns[pawn_select].curr[0] - pawns[pawn_select].last[0]
            delta_y = pawns[pawn_select].curr[1] - pawns[pawn_select].last[1]
            pawns[pawn_select].last[0] = pawns[pawn_select].curr[0]
            pawns[pawn_select].last[1] = pawns[pawn_select].curr[1]
            pawns[pawn_select].curr[0] += delta_x
            pawns[pawn_select].curr[1] += delta_y
            open_square(pawns[pawn_select].curr[0], pawns[pawn_select].curr[1])
            return check_second_steps(pawns[pawn_select].curr[0], pawns[pawn_select].curr[1])

    elif areaSquares[y][x][0] == "d":
        quantity_open = []
        for step in areaSquares[y][x][1]:
            if areaOpen[step[1]][step[0]][0] == 1:
                quantity_open.append(step)

        if len(quantity_open) == 2 and \
                quantity_open != areaSquares[y][x][1]:
            for step in quantity_open:
                if step[0] != x and step[1] != y:
                    for pawn in pawns:
                        if pawn.curr[0] == step[0] and \
                                pawn.curr[1] == step[1]:
                            if pawn.color != pawns[pawn_select].color:
                                kick_pawn(pawn_select)
                            pawn.last[0] = pawn.curr[0]
                            pawn.last[1] = pawn.curr[1]
                            pawn.curr[0] = x
                            pawn.curr[1] = y
                            break
                    break

        for step in quantity_open:
            areaSquares[step[1]][step[0]][1] = quantity_open

    elif areaSquares[y][x][0] == "g":
        pawns[pawn_select].curr = gunshot(x, y)

    elif areaSquares[y][x][0] == "c":
        pawns[pawn_select].curr = [pawns[pawn_select].last[0], pawns[pawn_select].last[1]]
        return check_second_steps(pawns[pawn_select].curr[0], pawns[pawn_select].curr[1])

    if areaSquares[pawns[pawn_select].last[1]][pawns[pawn_select].last[0]][0] == "p":
        areaSquares[pawns[pawn_select].last[1]][pawns[pawn_select].last[0]][1] = False

    quantity_pawns = 0
    for pawn in pawns:
        if pawn.curr == [x, y] and \
                pawn.color != pawns[pawn_select].color and \
                pawn.skip == pawns[pawn_select].skip and \
                pawn is not pawns[pawn_select] and \
                areaSquares[y][x][0] != "j":
            quantity_pawns += 1
            if quantity_pawns == 1:
                kick_pawn(pawns.index(pawn))
            else:
                kick_pawn(pawn_select)
                break

    for boat in boats:
        if pawns[pawn_select].curr == boat.curr and boat.color != pawns[pawn_select].color:
            kill_pawn()
            break

    pawn_select = -1
    game_mode = "select"
    return []


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
                        [x, y] == pawn.curr:
                    pawn_select = pawns.index(pawn)
            way_pawn = mouse_click_select(x, y, delay)
        elif game_mode == "move":
            mouse_click_move(x, y, delay)
    show_area(areaSquares, areaOpen)
    if 0 <= x < len(areaSquares) and 0 <= y < len(areaSquares):
        print_area_window(f"{areaSquares[y][x]}\n{x}, {y}", coord_xy)


def update_window():
    global scope, way_pawn
    window.fill(bg_color)  # Очистить окно

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

    square_temp = pygame.transform.scale(boat_img, (scope, scope))

    for boat in boats:
        square = pygame.Surface((scope, scope), pygame.SRCALPHA)
        square.fill(pawn2color[boat.color])
        square.set_alpha(40)
        window.blit(square_temp,
                    (boat.curr[0] * scope + place_x,
                     boat.curr[1] * scope + place_y))
        window.blit(square,
                    (boat.curr[0] * scope + place_x,
                     boat.curr[1] * scope + place_y))

        window.blit(pygame.font.Font("font/RobotoMono-Bold.ttf",
                                     int(scope / 8)).render(f"Рома: {boat.alco}",
                                                            True,
                                                            bg_color),
                    (boat.curr[0] * scope + place_x,
                     boat.curr[1] * scope + place_y))

    def draw_pawn(item: Pawn, pawn_x, pawn_y, radius, select: bool):
        pygame.draw.circle(window, pawn2color[item.color],
                           (item.curr[0] * scope + place_x + pawn_x,
                            item.curr[1] * scope + place_y + pawn_y),
                           radius)
        if select:
            pygame.draw.circle(window, pawn_select_color,
                               (item.curr[0] * scope + place_x + pawn_x,
                                item.curr[1] * scope + place_y + pawn_y),
                               radius, 4)

    for pawn in pawns:
        if pawn_select != -1:
            mark = pawn == pawns[pawn_select]
        else:
            mark = False

        if pawn.skip <= 0:
            if areaSquares[pawn.curr[1]][pawn.curr[0]][0] == "t5":
                draw_pawn(pawn, scope * 5 / 6, scope * 5 / 6, scope / 6, mark)

            elif areaSquares[pawn.curr[1]][pawn.curr[0]][0] == "t4":
                draw_pawn(pawn, scope / 3, scope / 6, scope / 6, mark)

            elif areaSquares[pawn.curr[1]][pawn.curr[0]][0] == "t3":
                draw_pawn(pawn, scope * 5 / 6, scope / 6, scope / 6, mark)

            elif areaSquares[pawn.curr[1]][pawn.curr[0]][0] == "t2":
                draw_pawn(pawn, scope * 2 / 3, scope / 6, scope / 6, mark)

            else:
                draw_pawn(pawn, scope / 2, scope / 2, scope / 4, mark)

                if pawn.skip == -1:
                    pygame.draw.line(window, mark_block_color,
                                     (pawn.curr[0] * scope + place_x + scope / 4,
                                      pawn.curr[1] * scope + place_y + scope / 4),
                                     (pawn.curr[0] * scope + place_x + 3 * scope / 4,
                                      pawn.curr[1] * scope + place_y + 3 * scope / 4), 4)

                    pygame.draw.line(window, mark_block_color,
                                     (pawn.curr[0] * scope + place_x + 3 * scope / 4,
                                      pawn.curr[1] * scope + place_y + scope / 4),
                                     (pawn.curr[0] * scope + place_x + scope / 4,
                                      pawn.curr[1] * scope + place_y + 3 * scope / 4), 4)

        elif pawn.skip == 1:
            if areaSquares[pawn.curr[1]][pawn.curr[0]][0] == "t5":
                draw_pawn(pawn, scope / 3, scope * 5 / 6, scope / 6, mark)

            elif areaSquares[pawn.curr[1]][pawn.curr[0]][0] == "t4":
                draw_pawn(pawn, scope * 2 / 3, scope / 3, scope / 6, mark)

            elif areaSquares[pawn.curr[1]][pawn.curr[0]][0] == "t3":
                draw_pawn(pawn, scope / 3, scope / 2, scope / 6, mark)

            elif areaSquares[pawn.curr[1]][pawn.curr[0]][0] == "t2":
                draw_pawn(pawn, scope / 6, scope * 5 / 6, scope / 6, mark)

        elif pawn.skip == 2:
            if areaSquares[pawn.curr[1]][pawn.curr[0]][0] == "t5":
                draw_pawn(pawn, scope / 6, scope / 2, scope / 6, mark)

            elif areaSquares[pawn.curr[1]][pawn.curr[0]][0] == "t4":
                draw_pawn(pawn, scope / 6, scope * 2 / 3, scope / 6, mark)

            elif areaSquares[pawn.curr[1]][pawn.curr[0]][0] == "t3":
                draw_pawn(pawn, scope * 5 / 6, scope * 5 / 6, scope / 6, mark)

        elif pawn.skip == 3:

            if areaSquares[pawn.curr[1]][pawn.curr[0]][0] == "t5":
                draw_pawn(pawn, scope / 2, scope / 6, scope / 6, mark)

            elif areaSquares[pawn.curr[1]][pawn.curr[0]][0] == "t4":
                draw_pawn(pawn, scope * 5 / 6, scope * 5 / 6, scope / 6, mark)

        elif pawn.skip == 4:
            draw_pawn(pawn, scope * 5 / 6, scope / 6, scope / 6, mark)

    mark_stroke_squares(way_pawn, pawn_select_color)


#
def set_1test_area():
    clear_area(areaOpen)
    clear_area(areaSquares)
    fill_area(areaSquares, "e2")
    areaSquares[3][6] = ["a2", [5]]
    areaSquares[3][7] = ["a2", [4]]
    areaSquares[6][6] = ["h"]
    areaSquares[7][8] = ["2"]

    areaSquares[7][2] = ["a2", [2]]
    areaSquares[8][2] = ["a2", [2]]
    areaSquares[9][2] = ["a2", [2]]
    areaSquares[9][1] = ["f"]
    areaSquares[9][3] = ["f"]

    areaSquares[8][7] = ["a7", [3, 4, 7]]
    areaSquares[2][2] = ["p", True]
    areaSquares[3][3] = ["f"]
    areaSquares[5][4] = ["c"]
    areaSquares[7][9] = ["r"]
    areaSquares[4][1] = ["j"]
    areaSquares[10][6] = ["g", [4]]
    areaSquares[3][10] = ["q", True]

    # areaSquares[5][8] = ["d", [(8, 5), (8, 10), (2, 7), (6, 2)]]
    # areaSquares[10][8] = ["d", [(8, 5), (8, 10), (2, 7), (6, 2)]]
    # areaSquares[7][2] = ["d", [(8, 5), (8, 10), (2, 7), (6, 2)]]
    # areaSquares[2][6] = ["d", [(8, 5), (8, 10), (2, 7), (6, 2)]]

    areaSquares[10][9] = ["a1", [3]]
    areaSquares[9][10] = ["c"]

    areaSquares[11][2] = ["a2", [5]]
    areaSquares[11][3] = ["2"]
    areaSquares[11][4] = ["a2", [4]]

    # areaSquares[11][4] = ["a3", [4, 5]]
    # areaSquares[11][6] = ["a3", [4, 5]]
    areaSquares[6][9] = ["2"]
    # areaSquares[3][4] = ["2"]
    areaSquares[3][4] = ["a2", [4]]
    areaSquares[2][10] = ["l", 3]
    areaSquares[1][4] = ["2"]

    areaSquares[6][11] = ["a2", [4]]

    areaSquares[11][5] = ["tc"]
    areaSquares[11][6] = ["t2"]
    areaSquares[11][7] = ["t3"]
    areaSquares[11][8] = ["t4"]
    areaSquares[11][9] = ["t5"]


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


#


clear_area(areaOpen)
clear_area(areaSquares)
clear_area(areaMoney)

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

            elif event.key == pygame.K_v:
                drunk()

            elif event.key == pygame.K_r:
                reborn_pawn(rebirth)

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
