# import math
# import random
import pygame
import time
from random import choice

pygame.init()
print("\033[36m{}\033[0m".format("\n  Подготовка игры"))


class TheGameCycle:
    def __init__(self, cycle: dict, start_player: str):
        self.__cycle = []
        # Построение цикла по часовой стрелке
        for i in cycle.keys():
            for j in cycle.keys():
                if (cycle[i][0] - cycle[j][0]) * (cycle[i][1] - cycle[j][1]) > 0:
                    self.__cycle.append(j)
                    break

        # Если один/два элемента, то верхний алгоритм не сработает
        if len(self.__cycle) != len(cycle):
            for i in cycle.keys():
                self.__cycle.append(i)

        self.__active_player = self.__cycle.index(start_player)

    def set_next(self):
        if self.__active_player == len(self.__cycle) - 1:
            self.__active_player = 0
        else:
            self.__active_player += 1

    def get_current(self) -> str:
        return self.__cycle[self.__active_player]


class Area:
    def __init__(self, area, quantity_squares):
        self.quantity_squares = quantity_squares
        self.__opened, self.__moneys, self.__squares = [], [], []
        self.__len_y = len(area)
        self.__len_x = len(area[0])
        for y in range(self.__len_y):
            x_opened, x_moneys, x_squares = [], [], []
            for x in range(self.__len_x):
                if area[y][x] == "S" or area[y][x] == "n":
                    x_opened.append(True)
                    x_squares.append([area[y][x]])
                else:
                    x_opened.append(False)
                    x_squares.append([0])
                x_moneys.append(0)
            self.__squares.append(x_squares)
            self.__opened.append(x_opened)
            self.__moneys.append(x_moneys)

    def inside_area(self, x: int, y: int) -> bool:
        return 0 <= y < len(self.__squares) and \
               0 <= x < len(self.__squares[y]) and \
               self.get_square(x, y)[0] != "n"  # null = "n"

    def get_open(self, x: int, y: int) -> bool:
        return self.__opened[y][x]

    def get_square(self, x: int, y: int) -> list:
        return self.__squares[y][x]

    def get_money(self, x: int, y: int) -> int:
        return self.__moneys[y][x]

    def set_open(self, x: int, y: int, value: bool):
        self.__opened[y][x] = value

    def set_square(self, x: int, y: int, value: list):
        self.__squares[y][x] = value

    def set_money(self, x: int, y: int, value: int):
        self.__moneys[y][x] = value

    def clear_area(self):
        for y in range(self.__len_y):
            for x in range(self.__len_x):
                if self.__squares[y][x][0] != "S" and self.__squares[y][x][0] != "n":
                    self.set_square(x, y, [0])
                    self.set_open(x, y, False)
                    self.set_money(x, y, 0)

    def fill_area(self, value: list):
        for y in range(0, len(self.__squares)):
            for x in range(0, len(self.__squares[y])):
                if self.__squares[y][x][0] != "S" and self.__squares[y][x][0] != "n":
                    self.set_square(x, y, value)

    def open_area(self):
        for y in range(0, len(self.__squares)):
            for x in range(0, len(self.__squares[y])):
                if self.__squares[y][x][0] != "S" and self.__squares[y][x][0] != "n":
                    self.set_open(x, y, True)

    def get_len_area(self) -> tuple:
        return self.__len_x, self.__len_y

    def mix_area(self):
        self.clear_area()

        temp_squares = self.quantity_squares.copy()
        den_coords_xy = []

        for y in range(0, len(self.__squares)):
            for x in range(0, len(self.__squares[y])):
                if self.__squares[y][x][0] != "S" and self.__squares[y][x][0] != "n":
                    while True:
                        chosen = choice(list(temp_squares.keys()))
                        if temp_squares[chosen] != 0:
                            temp_squares[chosen] -= 1
                            if chosen == "g":
                                self.__squares[y][x] = ["g", choice([[2], [4], [5], [7]])]
                                break
                            elif chosen == "a1":
                                self.__squares[y][x] = ["a1", choice([[1], [3], [6], [8]])]
                                break
                            elif chosen == "a2":
                                self.__squares[y][x] = ["a2", choice([[2], [4], [5], [7]])]
                                break
                            elif chosen == "a3":
                                self.__squares[y][x] = ["a3", choice([[4, 5], [2, 7]])]
                                break
                            elif chosen == "a4":
                                self.__squares[y][x] = ["a4", choice([[1, 8], [3, 6]])]
                                break
                            elif chosen == "a5":
                                self.__squares[y][x] = ["a5", [1, 3, 6, 8]]
                                break
                            elif chosen == "a6":
                                self.__squares[y][x] = ["a6", [2, 4, 5, 7]]
                                break
                            elif chosen == "a7":
                                self.__squares[y][x] = ["a7", choice([[1, 5, 7], [3, 4, 7], [6, 5, 2], [8, 4, 2]])]
                                break
                            elif chosen == "p":
                                self.__squares[y][x] = ["p", True]
                                break
                            elif chosen == "q":
                                self.__squares[y][x] = ["q", True]
                                break
                            elif chosen == "l":
                                self.__squares[y][x] = ["l", 3]
                                break
                            elif chosen[0] == "v":
                                self.__squares[y][x] = [chosen, True]
                                break
                            elif chosen == "d":
                                den_coords_xy.append((x, y))
                                break
                            elif "m" in chosen and chosen != "m":
                                self.__squares[y][x] = [chosen, True]
                                break
                            else:
                                self.__squares[y][x][0] = chosen
                                break
        for den_coord_xy in den_coords_xy:
            self.__squares[den_coord_xy[1]][den_coord_xy[0]] = ["d", tuple(den_coords_xy)]

    def earthquake(self):
        quantity_swaps = 2
        closed = []
        print(f"☯ Землетрясение:")
        for y in range(0, len(self.__squares)):
            for x in range(0, len(self.__squares[y])):
                if not self.__opened[y][x]:
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
        for y in range(0, len(self.__squares)):
            for x in range(0, len(self.__squares[y])):
                if self.__opened[y][x] and \
                        self.__squares[y][x][0] != "S" and \
                        self.__squares[y][x][0] != "c" and \
                        self.__squares[y][x][0] != "2":
                    allowed_steps.add((x, y))
        return allowed_steps

    def print_area(self, name_area: str, mode: str, ps=""):
        area = self.__squares
        if name_area == "opened":
            area = self.__opened
        elif name_area == "moneys":
            area = self.__moneys
        elif name_area == "squares":
            area = self.__squares
        else:
            print("\033[31m{}\033[0m".format(f"Поля {name_area} не существует\n"))
            return

        if mode == "Поле":
            print("\033[34m{}\033[0m".format(f"\n▦ Просмотр поля: {ps}"))
            line = "   "
            for y in range(0, len(area)):
                line = line \
                       + " " * (3 - len(str(y))) \
                       + str(y)
            print("\033[34m{}\033[0m".format(line + "  x →"))

            if name_area == "opened":
                for y in range(0, len(area)):
                    line = "  " + str(y) \
                           + " " * (3 - len(str(y)))
                    for x in range(0, len(area[y])):
                        icon = "♦"
                        if area[y][x]:
                            icon = "♢"
                        if self.__squares[y][x][0] == "S":
                            icon = " "
                        if self.__squares[y][x][0] == "n":
                            icon = "x"
                        line = line + icon + "  "
                    print("\033[34m{}\033[0m".format(f"{line}"))
            elif name_area == "moneys":
                for y in range(0, len(area)):
                    line = "  " + str(y) \
                           + " " * (3 - len(str(y)))
                    for x in range(0, len(area[y])):
                        line = line \
                               + str(area[y][x]) \
                               + " " * (3 - len(str(area[y][x])))
                    print("\033[34m{}\033[0m".format(f"{line}"))
            elif name_area == "squares":
                for y in range(0, len(area)):
                    line = "  " + str(y) \
                           + " " * (3 - len(str(y)))
                    for x in range(0, len(area[y])):
                        line = line \
                               + str(area[y][x][0]) \
                               + " " * (3 - len(str(area[y][x][0])))
                    print("\033[34m{}\033[0m".format(f"{line}"))
            print("\033[34m{}\033[0m".format("  y"))
            print("\033[34m{}\033[0m".format("  ↓"))





        elif mode == "Массив":
            print("\033[34m{}\033[0m".format(f"\n▥ Просмотр массива: {ps}"))
            for y in range(0, len(area)):
                print("\033[34m{}\033[0m".format(f"  {area[y]}"))

        elif mode == "Список":
            print("\033[34m{}\033[0m".format(f"\n▤ Просмотр списка: {ps}"))
            for y in range(0, len(area)):
                for x in range(0, len(area[y])):
                    print("\033[34m{}\033[0m".format(f"  {area[y][x]}"))


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


class Players:
    def __init__(self, colors: dict, quantity_pawns: int):
        self.quantity_pawns = quantity_pawns
        self.selected_color = {'color': "", 'pawn': -1}
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
                self.selected_color['color'] = color
                self.selected_color['pawn'] = self.players[color]['pawns'].index(pawn)
                return True
        return False

    def is_selected(self) -> bool:
        return self.selected_color['color'] != "" and self.selected_color['pawn'] != -1

    def cancel_select(self):
        self.selected_color['color'] = ""
        self.selected_color['pawn'] = -1

    def set_pawn_curr(self, value: list):
        self.players[self.selected_color['color']]['pawns'][self.selected_color['pawn']].curr = value

    def set_pawn_last(self, value: list):
        self.players[self.selected_color['color']]['pawns'][self.selected_color['pawn']].last = value

    def get_pawn(self, path2pawn: dict) -> Pawn:
        return self.players[path2pawn['color']]['pawns'][path2pawn['pawn']]

    def get_select_pawn(self) -> Pawn:
        return self.get_pawn(self.get_select())

    def get_boat(self, path2pawn: dict) -> Boat:
        return self.players[path2pawn['color']]['boat']

    def get_select(self) -> dict:
        return self.selected_color

    def kill_pawn(self):
        print("\033[31m{}\033[0m".format(f"☠ Убита пешка:        "
                                         f"{', '.join(map(str, self.get_pawn(self.selected_color).curr))} "
                                         f"{self.selected_color['color']}"))

        self.players[self.selected_color['color']]['pawns'].pop(self.selected_color['pawn'])

    def kick_pawn(self, kicked_pawn: dict):
        print("\033[35m{}\033[0m".format(f"⎋ Пешка на корабле:    "
                                         f"{', '.join(map(str, self.get_pawn(kicked_pawn).curr))} "
                                         f"{kicked_pawn['color']}"))

        self.get_pawn(kicked_pawn).curr = [self.get_boat(kicked_pawn).curr[0],
                                           self.get_boat(kicked_pawn).curr[1]]
        self.get_pawn(kicked_pawn).skip = 0

    def check_other_pawns(self, x: int, y: int) -> int:
        quantity = 0
        for player in self.players.keys():
            if player != self.selected_color['color']:
                for pawn in self.players[player]['pawns']:
                    if pawn.curr == [x, y]:
                        quantity += 1
        return quantity

    def take_other_pawn(self, x: int, y: int) -> dict:
        for player in self.players.keys():
            if player != self.selected_color['color']:
                for pawn in self.players[player]['pawns']:
                    if pawn.curr == [x, y]:
                        return {'color': player,
                                'pawn': self.players[player]['pawns'].index(pawn)}

    def check_other_boats(self, x: int, y: int) -> bool:
        for player in self.players.keys():
            if player != self.selected_color['color']:
                if self.players[player]["boat"].curr == [x, y]:
                    return True
        return False

    def boat_step(self, x: int, y: int):
        boat = self.players[self.selected_color['color']]['boat']
        for pawn in self.players[self.selected_color['color']]['pawns']:
            if pawn.curr == boat.curr:
                pawn.last[0] = pawn.curr[0]
                pawn.last[1] = pawn.curr[1]
                pawn.curr[0] = x
                pawn.curr[1] = y
        boat.curr[0] = x
        boat.curr[1] = y

    def rescuing_pawn(self, x: int, y: int):
        for pawn in self.players[self.selected_color['color']]['pawns']:
            if pawn.curr == [x, y] and \
                    pawn is not self.get_pawn(self.selected_color):
                pawn.skip = 0
                self.get_pawn(self.selected_color).skip = 0
                break

    def drunk(self, area: Area):
        global game_mode, way_pawn
        if self.selected_color != {'color': "", 'pawn': -1}:
            if self.get_pawn(self.selected_color).skip != 0 and \
                    self.get_boat(self.selected_color).alco > 0:
                self.get_pawn(self.selected_color).skip = 0
                self.get_boat(self.selected_color).alco -= 1

                print(f"☺ Пешка нажралась:     "
                      f"{', '.join(map(str, self.get_pawn(self.selected_color).curr))}"
                      f"{' ' * (4 - (self.get_pawn(self.selected_color).curr[0] // 10 + self.get_pawn(self.selected_color).curr[1] // 10))}"
                      f"{area.get_square(self.get_pawn(self.selected_color).curr[0], self.get_pawn(self.selected_color).curr[1])}")

                print(f"𝕽 Запасы рома:         "
                      f"{self.selected_color['color']} {self.get_boat(self.selected_color).alco}")

    def reborn_pawn(self, area: Area):
        global way_pawn, game_mode

        if area.get_square(self.get_pawn(self.selected_color).curr[0],
                           self.get_pawn(self.selected_color).curr[1])[0] == "r":

            if len(self.players[self.selected_color['color']]['pawns']) < self.quantity_pawns:
                self.players[self.selected_color['color']]['pawns'].append(
                    Pawn(self.get_pawn(self.selected_color).last,
                         self.get_pawn(self.selected_color).curr,
                         self.get_pawn(self.selected_color).skip))

                print("\033[32m{}\033[0m".format(f"☮ Возрождена пешка: "
                                                 f"{', '.join(map(str, self.get_pawn(self.selected_color).curr))}"
                                                 f"{self.selected_color['color']}"))

                print("\033[32m{}\033[0m".format(f"  Пешек {len(self.players[self.selected_color['color']]['pawns'])}"
                                                 f" {'♟' * len(self.players[self.selected_color['color']]['pawns'])}"))
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
            self.get_pawn(self.selected_color).curr = [x, new_y]
        elif area.get_square(x, y)[1][0] == 4:
            while area.get_square(new_x, new_y)[0] != "S":
                new_x -= 1
            self.get_pawn(self.selected_color).curr = [new_x, y]
        elif area.get_square(x, y)[1][0] == 5:
            while area.get_square(new_x, new_y)[0] != "S":
                new_x += 1
            self.get_pawn(self.selected_color).curr = [new_x, y]
        elif area.get_square(x, y)[1][0] == 7:
            while area.get_square(new_x, new_y)[0] != "S":
                new_y += 1
            self.get_pawn(self.selected_color).curr = [x, new_y]

    def info(self) -> str:
        result_line = ""
        for player in self.players.keys():
            line = ""
            for pawn in self.players[player]["pawns"]:
                line += f"{pawn.info()}\n         "
            result_line += f'{player} Лодка: {self.players[player]["boat"].info()}\n' \
                           f'  Пешки: {line}\n'
        return result_line


class Screen:
    def __init__(self):
        global window_height, window_width
        pygame.display.init()
        self.__screen = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)
        pygame.display.set_caption("Thousand devils")
        pygame.display.set_icon(pygame.image.load("IMG/empty1.png"))

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
        self.empty = pygame.image.load("IMG/empty.png").convert()
        self.boat_img = pygame.image.load("IMG/boat.png").convert()
        self.frame = pygame.image.load("IMG/frame.png").convert_alpha()

        # Загрузка шрифтов
        self.RobotoBold = pygame.font.Font("font/RobotoMono-Bold.ttf", 12)
        self.RobotoRegular = pygame.font.Font("font/RobotoMono-Regular.ttf", 12)

        # Нормализация картинок
        gun = pygame.transform.rotate(gun, 270)
        arrow7 = pygame.transform.rotate(arrow7, 270)

        self.squares_img_name = {"e1": empty1, "e2": empty2, "e3": empty3, "e4": empty4,
                                 "a1": arrow1, "a2": arrow2, "a3": arrow3, "a4": arrow4, "a5": arrow5, "a6": arrow6,
                                 "a7": arrow7,
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

    def print_in_window(self, text: str, coord_xy: tuple):
        self.__screen.blit(self.RobotoRegular.render(text, True, text_color, bg_color), coord_xy)

    def update_window(self, area: Area, players: Players):
        global scope, way_pawn
        self.__screen.fill(bg_color)  # Очистить окно

        square_temp = pygame.transform.scale(self.frame, (scope * 13, scope * 13))
        self.__screen.blit(square_temp, (place_x, place_y))
        for y in range(0, area.get_len_area()[1]):
            for x in range(0, area.get_len_area()[0]):
                if area.get_open(x, y) and area.get_square(x, y)[0] != "S" and area.get_square(x, y)[0] != "n":
                    square_temp = pygame.transform.scale(self.squares_img_name[area.get_square(x, y)[0]],
                                                         (scope, scope))
                    if "a" in area.get_square(x, y)[0] or "g" in area.get_square(x, y)[0]:
                        square_temp = pygame.transform.rotate(square_temp,
                                                              int(digit2degrees[area.get_square(x, y)[1][0]]))
                    self.__screen.blit(square_temp, (x * scope + place_x, y * scope + place_y))
                else:
                    if area.get_square(x, y)[0] != "S" and area.get_square(x, y)[0] != "n":
                        square_temp = pygame.transform.scale(self.empty, (scope, scope))
                        self.__screen.blit(square_temp, (x * scope + place_x, y * scope + place_y))

        square_temp = pygame.transform.scale(self.boat_img, (scope, scope))

        def mark_stroke_squares(coords_xy: list, color: tuple):
            for coord_xy in coords_xy:
                pygame.draw.rect(self.__screen, color,
                                 (coord_xy[0] * scope + place_x,
                                  coord_xy[1] * scope + place_y,
                                  scope, scope), 4)

        def mark_fill_squares(coords_xy: list, color: tuple):
            square = pygame.Surface((scope, scope), pygame.SRCALPHA)
            square.fill(color)
            for coord_xy in coords_xy:
                self.__screen.blit(square,
                                   (coord_xy[0] * scope + place_x,
                                    coord_xy[1] * scope + place_y))

        def draw_pawn(item: Pawn, pawn_x, pawn_y, radius, select: bool, color: str):
            pygame.draw.circle(self.__screen, pawn2color[color],
                               (item.curr[0] * scope + place_x + pawn_x,
                                item.curr[1] * scope + place_y + pawn_y),
                               radius)
            if select:
                pygame.draw.circle(self.__screen, pawn_select_color,
                                   (item.curr[0] * scope + place_x + pawn_x,
                                    item.curr[1] * scope + place_y + pawn_y),
                                   radius, 4)

        for player in players.players.keys():
            boat = players.players[player]["boat"]
            square = pygame.Surface((scope, scope), pygame.SRCALPHA)
            square.fill(pawn2color[player])
            square.set_alpha(40)
            self.__screen.blit(square_temp,
                               (boat.curr[0] * scope + place_x,
                                boat.curr[1] * scope + place_y))
            self.__screen.blit(square,
                               (boat.curr[0] * scope + place_x,
                                boat.curr[1] * scope + place_y))

            self.__screen.blit(pygame.font.Font("font/RobotoMono-Bold.ttf",
                                                int(scope / 8)).render(f"Рома: {boat.alco}",
                                                                       True,
                                                                       bg_color),
                               (boat.curr[0] * scope + place_x,
                                boat.curr[1] * scope + place_y))

            for pawn in players.players[player]["pawns"]:
                if players.is_selected():
                    mark = pawn == players.get_select_pawn()
                else:
                    mark = False

                if pawn.skip <= 0:
                    if area.get_square(*pawn.curr)[0] == "t5":
                        draw_pawn(pawn, scope * 5 / 6, scope * 5 / 6, scope / 6, mark, player)
                    elif area.get_square(*pawn.curr)[0] == "t4":
                        draw_pawn(pawn, scope / 3, scope / 6, scope / 6, mark, player)
                    elif area.get_square(*pawn.curr)[0] == "t3":
                        draw_pawn(pawn, scope * 5 / 6, scope / 6, scope / 6, mark, player)
                    elif area.get_square(*pawn.curr)[0] == "t2":
                        draw_pawn(pawn, scope * 2 / 3, scope / 6, scope / 6, mark, player)

                    else:
                        draw_pawn(pawn, scope / 2, scope / 2, scope / 4, mark, player)

                        if pawn.skip == -1:
                            pygame.draw.line(self.__screen, mark_block_color,
                                             (pawn.curr[0] * scope + place_x + scope / 4,
                                              pawn.curr[1] * scope + place_y + scope / 4),
                                             (pawn.curr[0] * scope + place_x + 3 * scope / 4,
                                              pawn.curr[1] * scope + place_y + 3 * scope / 4), 4)

                            pygame.draw.line(self.__screen, mark_block_color,
                                             (pawn.curr[0] * scope + place_x + 3 * scope / 4,
                                              pawn.curr[1] * scope + place_y + scope / 4),
                                             (pawn.curr[0] * scope + place_x + scope / 4,
                                              pawn.curr[1] * scope + place_y + 3 * scope / 4), 4)

                elif pawn.skip == 1:
                    if area.get_square(*pawn.curr)[0] == "t5":
                        draw_pawn(pawn, scope / 3, scope * 5 / 6, scope / 6, mark, player)
                    elif area.get_square(*pawn.curr)[0] == "t4":
                        draw_pawn(pawn, scope * 2 / 3, scope / 3, scope / 6, mark, player)
                    elif area.get_square(*pawn.curr)[0] == "t3":
                        draw_pawn(pawn, scope / 3, scope / 2, scope / 6, mark, player)
                    elif area.get_square(*pawn.curr)[0] == "t2":
                        draw_pawn(pawn, scope / 6, scope * 5 / 6, scope / 6, mark, player)
                elif pawn.skip == 2:
                    if area.get_square(*pawn.curr)[0] == "t5":
                        draw_pawn(pawn, scope / 6, scope / 2, scope / 6, mark, player)
                    elif area.get_square(*pawn.curr)[0] == "t4":
                        draw_pawn(pawn, scope / 6, scope * 2 / 3, scope / 6, mark, player)
                    elif area.get_square(*pawn.curr)[0] == "t3":
                        draw_pawn(pawn, scope * 5 / 6, scope * 5 / 6, scope / 6, mark, player)
                elif pawn.skip == 3:
                    if area.get_square(*pawn.curr)[0] == "t5":
                        draw_pawn(pawn, scope / 2, scope / 6, scope / 6, mark, player)
                    elif area.get_square(*pawn.curr)[0] == "t4":
                        draw_pawn(pawn, scope * 5 / 6, scope * 5 / 6, scope / 6, mark, player)
                elif pawn.skip == 4:
                    draw_pawn(pawn, scope * 5 / 6, scope / 6, scope / 6, mark, player)
            mark_stroke_squares(way_pawn, pawn_select_color)


def loop_search(start_x: int, start_y: int) -> bool:
    def check_arrow(coord_xy: tuple):
        nonlocal used_steps

        x = coord_xy[0]
        y = coord_xy[1]

        # print(f"↗ Проверка стрелки:  "
        #       f"{x}, {y}{' ' * (4 - (x // 10 + y // 10))}{areaSquares[y][x][1]}")
        for digit in game_area.get_square(x, y)[1]:
            new_x = x + digit2delta[digit][0]
            new_y = y + digit2delta[digit][1]
            if game_area.inside_area(new_x, new_y) and \
                    (new_x, new_y) not in used_steps:
                if game_area.get_open(new_x, new_y):
                    if "a" in game_area.get_square(new_x, new_y)[0]:
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

        if game_area.inside_area(coord_xy[0], coord_xy[1]):
            if game_area.get_open(coord_xy[0], coord_xy[1]):
                if game_area.get_square(x, y)[0] == "2":
                    check_step((x + (x - old_x), y + (y - old_y)), (x, y))
                elif "a" in game_area.get_square(x, y)[0] and (x, y) not in used_steps:
                    used_steps.add((x, y))
                    check_arrow((x, y))
                elif game_area.get_square(x, y)[0] != "c" and \
                        (x, y) not in used_steps and \
                        ((game_area.get_square(x, y)[0] != "f" or
                          game_area.get_square(x, y)[0] != "r") and
                         game_players.check_other_pawns(x, y) == 0):
                    used_steps.add((x, y))
            else:
                if (x, y) not in used_steps:
                    used_steps.add((x, y))

        # print(f"☐ Проверка шага:     "
        #       f"{x}, {y}"
        #       f"{' ' * (4 - (x // 10 + y // 10))}{(x, y) in used_steps}")

    checked_digits = [1, 2, 3, 4, 5, 6, 7, 8]
    checked_steps = []
    used_steps = set()
    extra_quantity = 0

    if game_area.inside_area(start_x, start_y):
        if "a" in game_area.get_square(start_x, start_y)[0]:
            checked_digits = game_area.get_square(start_x, start_y)[1]
        for digit in checked_digits:  # Получаем из направлений координаты
            checked_steps.append((start_x + digit2delta[digit][0],
                                  start_y + digit2delta[digit][1]))
        for step in checked_steps:  # Проверяем координаты
            check_step(step, (start_x, start_y))
    for step in used_steps:
        if ("a" in game_area.get_square(step[0], step[1])[0] or
            game_area.get_square(step[0], step[1])[0] == "2") and \
                game_area.get_open(step[0], step[1]):
            extra_quantity += 1
    used_steps = list(used_steps)
    # print_area(used_steps, "Строка", ps="Координаты, куда можно сходить")
    # mark_fill_squares(list(used_steps), mark_select_color)
    # show_area(areaSquares, areaOpen)
    return len(used_steps) - extra_quantity == 0


def file2area(name_file: str, hide=False):  # Аргумент hide для проверки
    if not hide:
        print(f'⎙ Создание поля из файла "{name_file[:-4]}"')

    try:
        file = open(name_file, 'r')
    except:
        print("\033[31m{}\033[0m".format(f"Файла {name_file} не существует"))
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
        print("\033[31m{}\033[0m".format(f"Неполный файл\n"
                                         f"Нет блока $n$ (Название)"))
        return False
    if a_cleaned == "":
        print("\033[31m{}\033[0m".format(f"Неполный файл\n"
                                         f"Нет блока $a$ (Поле)"))
        return False
    if f_cleaned == "":
        print("\033[31m{}\033[0m".format(f"Неполный файл\n"
                                         f"Нет блока $f$ (Настройка)"))
        return False
    if s_cleaned == "":
        print("\033[31m{}\033[0m".format(f"Неполный файл\n"
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
            area_x.append("S")
        elif piece == "O":
            empty_row = False
            waste_row = False
            area_x.append(0)
            quantity_square_area += 1
        elif piece == "n":
            waste_row = False
            area_x.append("n")

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
            if flip_area[y][x] == 0 or \
                    flip_area[y][x] == "S":
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

    boats = 0
    pawns = 0
    start_boat = ""

    try:
        boats = int(facilities["b"])
        pawns = int(facilities["p"])
        start_boat = facilities["s"]
    except:
        print("\033[31m{}\033[0m".format(f"Количество лодок или пешек не число\n"
                                         f"Блок $f$"))
        return False

    pawn_color = {}
    start_coord_xy = {}
    color = 0

    for i in range(boats):
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
                    start_coord_xy[color] = temp
                if separator == 2:
                    pawn_color[color] = temp

    if len(pawn_color) != len(start_coord_xy):
        print("\033[31m{}\033[0m".format(f"Количество цветов и координат старта различны\n"
                                         f"Цвета: {pawn_color}\n"
                                         f"Координаты начала: {start_coord_xy}"))
        return False

    for key in pawn_color.keys():
        for i in range(len(pawn_color[key])):
            try:
                pawn_color[key][i] = int(pawn_color[key][i])
            except:
                print("\033[31m{}\033[0m".format(f"В вектор цвета не число\n"
                                                 f"Цвет {key}, Вектор: {pawn_color[key]}"))
                return False
        pawn_color[key] = tuple(pawn_color[key])

    for key in start_coord_xy.keys():
        for i in range(len(start_coord_xy[key])):
            try:
                start_coord_xy[key][i] = int(start_coord_xy[key][i])
            except:
                print("\033[31m{}\033[0m".format(f"В вектор цвета не числа\n"
                                                 f"Цвет {key}, Вектор: {start_coord_xy[key]}"))
                return False

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

    if not hide:
        print("\033[32m{}".format(f"  Название карты: {name_area}\n"))
        print(f"  Каркас поля:")
        for y in range(len(area)):
            line = ''
            for x in range(len(area[y])):
                line = line + str(area[y][x]) + ' '
            print(f"  {line}")
        print(f"\n  Кол-во      Кол-во   Старт")
        print(f"  кораблей:   пешек:   корабль:")
        print(f"  {boats}{' ' * (13 - int(str(boats)))}{pawns}{' ' * (10 - int(str(boats)))}{start_boat}")
        print(f"\n  Цвета кораблей:")
        for key in pawn_color.keys():
            print(f"  {key}: {pawn_color[key]}")
        print(f"\n  Координаты кораблей:")
        for key in start_coord_xy.keys():
            print(f"  {key}: {start_coord_xy[key]}")
        print(f"  Карточки:")
        line = "  "
        i = 0
        for key in squares.keys():
            i += 1
            line += f"{key}: {squares[key]} "
            if i == 4:
                line += "\n  "
                i = 0
        print("\033[32m{}\033[0m".format(f"{line}"))
    return {"area": area,
            "pawns": pawns,
            "start_boat": start_boat,
            "pawn2color": pawn_color,
            "start_coord_xy": start_coord_xy,
            "squares": squares}


def illuminate(x: int, y: int):
    global game_mode

    if game_area.get_square(*game_players.get_select_pawn().curr)[1] >= 1:
        if game_mode == "lighthouse":
            if game_area.inside_area(x, y) and \
                    not game_area.get_open(x, y):
                print(f"☄ Маяк открыл:         "
                      f"{x}, {y}{' ' * (4 - (x // 10 + y // 10))}"
                      f"{game_area.get_square(x, y)}")
                game_area.set_open(x, y, True)

                game_area.get_square(*game_players.get_select_pawn().curr)[1] -= 1
                if game_area.get_square(*game_players.get_select_pawn().curr)[1] == 0:
                    game_cycle.set_next()
                    game_mode = "select"
                    game_players.cancel_select()
        else:
            game_mode = "lighthouse"
    else:
        game_mode = "select"
        game_players.cancel_select()


def print_string(line: list, ps=""):
    print("\033[34m{}\033[0m".format(f"▧ Просмотр строки: {ps}\n  {line}"))


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


def mouse_click_cancel_select(coord_xy: tuple, delay: float):
    global way_pawn, game_mode
    x = (coord_xy[0] - place_x) // scope
    y = (coord_xy[1] - place_y) // scope

    if game_players.is_selected():
        if game_area.inside_area(x, y) and \
                game_players.get_select_pawn().curr == [x, y] and \
                "a" not in game_area.get_square(*game_players.get_select_pawn().curr)[0] and \
                game_area.get_square(*game_players.get_select_pawn().curr)[0] != "2" and \
                (game_area.get_square(*game_players.get_select_pawn().curr)[0] != "l" or
                 game_area.get_square(*game_players.get_select_pawn().curr)[1] == 0):
            game_players.cancel_select()
            game_mode = "select"
            way_pawn = []
            print("\033[35m{}\033[0m".format(f"  Отмена выбора пешки: "
                                             f"{x}, {y}{' ' * (4 - (x // 10 + y // 10))}{game_area.get_square(x, y)}"
                                             f"{' ' * (50 - len(str(game_area.get_square(x, y))))}"
                                             f"Δt {delay}"))


def mouse_click_select(x: int, y: int, delay: float) -> list:
    global game_mode

    if game_area.inside_area(x, y) and \
            game_players.is_selected():

        game_mode = "move"
        print("\033[35m{}\033[0m".format(f"\n  Выбрана пешка:       "
                                         f"{x}, {y}{' ' * (4 - (x // 10 + y // 10))}{game_area.get_square(x, y)}"
                                         f"{' ' * (50 - len(str(game_area.get_square(x, y))))}"
                                         f"Δt {delay}"))
        if loop_search(x, y):
            game_players.kill_pawn()
        else:
            return check_steps(x, y)
    return []


def check_steps(x: int, y: int) -> list:
    global game_mode
    checked_steps = [1, 2, 3, 4, 5, 6, 7, 8]
    allowed_steps = set()
    mode = "Field"
    if game_area.inside_area(x, y):
        if game_area.get_square(x, y)[0] == "S":
            checked_steps = []

            if [x, y] == game_players.get_boat(game_players.get_select()).curr:
                mode = "Boat"
                condition = "None"

                for step in [2, 4, 5, 7]:
                    new_x = x + digit2delta[step][0]
                    new_y = y + digit2delta[step][1]

                    if game_area.inside_area(new_x, new_y):
                        if game_area.get_square(new_x, new_y)[0] == "S":
                            if step == 2 or step == 7:
                                condition = "vertical"
                            elif step == 4 or step == 5:
                                condition = "horizontal"

                if game_area.inside_area(x - 1, y - 1) and game_area.get_square(x - 1, y - 1)[0] == "S":
                    if condition == "vertical":
                        checked_steps = [4, 7]
                    elif condition == "horizontal":
                        checked_steps = [2, 5]

                elif game_area.inside_area(x + 1, y + 1) and game_area.get_square(x + 1, y + 1)[0] == "S":
                    if condition == "vertical":
                        checked_steps = [2, 5]
                    elif condition == "horizontal":
                        checked_steps = [4, 7]

                elif game_area.inside_area(x + 1, y - 1) and game_area.get_square(x + 1, y - 1)[0] == "S":
                    if condition == "vertical":
                        checked_steps = [5, 7]
                    elif condition == "horizontal":
                        checked_steps = [2, 4]

                elif game_area.inside_area(x - 1, y + 1) and game_area.get_square(x - 1, y + 1)[0] == "S":
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

                    if game_area.inside_area(new_x, new_y) and game_area.get_square(new_x, new_y)[0] == "S":
                        checked_steps.append(step)

        elif game_area.get_square(x, y)[0] == "h":
            checked_steps = [9, 10, 11, 12, 13, 14, 15, 16]

        elif game_area.get_square(x, y)[0] == "p" and game_area.get_square(x, y)[1]:
            allowed_steps = game_area.flight()

        elif "t" in game_area.get_square(x, y)[0]:
            if game_area.get_square(x, y)[0] != "tk" and \
                    game_area.get_square(x, y)[0] != "tc" and \
                    game_area.get_square(x, y)[0] != "tv":

                if game_players.get_select_pawn().skip != 0:
                    return [(x, y)]
            if game_players.get_select_pawn().skip != 0 and \
                    game_area.get_square(x, y)[0] == "tc":
                return []

        elif "a" in game_area.get_square(x, y)[0]:
            checked_steps = game_area.get_square(x, y)[1]

        for step in checked_steps:
            new_x = x + digit2delta[step][0]
            new_y = y + digit2delta[step][1]
            if game_area.inside_area(new_x, new_y):
                if game_area.get_open(new_x, new_y):
                    if mode == "Field" and \
                            game_area.get_square(new_x, new_y)[0] != "c" and \
                            (game_area.get_square(new_x, new_y)[0] != "S" or
                             [new_x, new_y] == game_players.get_boat(game_players.get_select()).curr):
                        allowed_steps.add((new_x, new_y))
                    if mode == "Coast" or mode == "Boat":
                        allowed_steps.add((new_x, new_y))
                else:
                    allowed_steps.add((new_x, new_y))

                if (game_area.get_square(new_x, new_y)[0] == "f" or
                    game_area.get_square(new_x, new_y)[0] == "r") and \
                        game_players.check_other_pawns(x, y) != 0:
                    allowed_steps.remove((new_x, new_y))

        if game_area.get_square(x, y)[0] == "d":
            quantity_open = []
            for step in game_area.get_square(x, y)[1]:
                if game_area.get_open(step[0], step[1]):
                    quantity_open.append(step)
                    if step != (x, y):
                        allowed_steps.add(step)

            if len(quantity_open) < 2:
                return []

    print_string(list(allowed_steps), ps="Координаты, куда ходить")
    return list(allowed_steps)


def mouse_click_move(x: int, y: int, delay: float):
    global game_mode, way_pawn

    if game_area.inside_area(x, y) and \
            way_pawn and \
            game_players.is_selected():

        for step in way_pawn:
            if x == step[0] and y == step[1]:
                game_players.set_pawn_last(game_players.get_select_pawn().curr)
                game_players.set_pawn_curr([x, y])
                game_area.set_open(x, y, True)

                if game_players.get_select_pawn().last == \
                        game_players.get_boat(game_players.get_select()).curr:
                    if game_area.inside_area(x, y) and game_area.get_square(x, y)[0] == "S":
                        game_players.boat_step(x, y)

                way_pawn = check_second_steps(x, y)

                print("\033[35m{}\033[0m".format(f"  Ход пешки:           "
                                                 f"{x}, {y}{' ' * (4 - (x // 10 + y // 10))}{game_area.get_square(x, y)}"
                                                 f"{' ' * (50 - len(str(game_area.get_square(x, y))))}"
                                                 f"Δt {delay}"))
                break


def check_second_steps(x: int, y: int) -> list:
    global game_mode

    print("\033[33m{}\033[0m".format(f"  Проверка клетки:     "
                                     f"{x}, {y}{' ' * (4 - (x // 10 + y // 10))}{game_area.get_square(x, y)}"
                                     f"{' ' * (50 - len(str(game_area.get_square(x, y))))}"))
    steps = []

    if game_players.check_other_boats(*game_players.get_select_pawn().curr) or \
            loop_search(x, y):
        game_players.kill_pawn()
        game_players.cancel_select()
        game_mode = "select"
        game_cycle.set_next()
        return []

    if game_players.check_other_pawns(x, y) > 0 and \
            game_area.get_square(x, y)[0] != "j":
        if game_players.check_other_pawns(x, y) == 1:
            game_players.kick_pawn(game_players.take_other_pawn(x, y))
        else:
            game_players.kick_pawn(game_players.get_select())
            game_players.kick_pawn(game_players.take_other_pawn(x, y))

    if "a" in game_area.get_square(x, y)[0]:
        for digit in game_area.get_square(x, y)[1]:
            steps.append((x + digit2delta[digit][0],
                          y + digit2delta[digit][1]))
        return steps

    elif game_area.get_square(x, y)[0] == "2":
        if game_area.get_square(*game_players.get_select_pawn().last)[0] == "h":
            for digit in [9, 10, 11, 12, 13, 14, 15, 16]:
                steps.append((x + digit2delta[digit][0], y + digit2delta[digit][1]))
            return steps
        else:
            delta_x = game_players.get_select_pawn().curr[0] - \
                      game_players.get_select_pawn().last[0]
            delta_y = game_players.get_select_pawn().curr[1] - \
                      game_players.get_select_pawn().last[1]

            game_players.set_pawn_last(game_players.get_select_pawn().curr)
            game_players.set_pawn_curr([game_players.get_select_pawn().curr[0] + delta_x,
                                        game_players.get_select_pawn().curr[1] + delta_y])
            game_area.set_open(*game_players.get_select_pawn().curr, True)
            return check_second_steps(*game_players.get_select_pawn().curr)

    elif "t" in game_area.get_square(x, y)[0]:
        if game_area.get_square(x, y)[0] != "tk" and \
                game_area.get_square(x, y)[0] != "tc" and \
                game_area.get_square(x, y)[0] != "tv":

            if game_players.get_select_pawn().skip != 0:
                game_players.get_select_pawn().skip -= 1

            if game_players.get_select_pawn().last != [x, y]:
                game_players.get_select_pawn().skip = int(game_area.get_square(x, y)[0][1]) - 1
                # Волшебная единица

        elif game_area.get_square(x, y)[0] == "tc":
            game_players.get_select_pawn().skip = -1
            game_players.rescuing_pawn(x, y)

        print(f"◮ Пешка в ловушке:     "
              f"{x}, {y}{' ' * (4 - (x // 10 + y // 10))}"
              f"{game_area.get_square(x, y)}   "
              f"Нужно пройти: ∞" if game_players.get_select_pawn().skip == -1
              else f"◮ Пешка в ловушке:     "
                   f"{x}, {y}{' ' * (4 - (x // 10 + y // 10))}"
                   f"{game_area.get_square(x, y)}   "
                   f"Нужно пройти: {game_players.get_select_pawn().skip}")

    elif game_area.get_square(x, y)[0] == "q" and \
            game_area.get_square(x, y)[1]:
        game_area.earthquake()
        game_area.get_square(x, y)[1] = False

    elif game_area.get_square(x, y)[0] == "w":
        game_players.kill_pawn()

    elif game_area.get_square(x, y)[0] == "b":
        game_players.kick_pawn(game_players.get_select())

    elif game_area.get_square(x, y)[0][0] == "v" and \
            game_area.get_square(x, y)[1]:
        game_players.get_boat(game_players.get_select()).alco += int(game_area.get_square(x, y)[0][1])
        game_area.get_square(x, y)[1] = False
        print(f"𝕽 Запасы рома:        "
              f"{game_players.get_boat(game_players.get_select()).alco} {game_players.get_select()['color']}")

    elif game_area.get_square(x, y)[0] == "l":
        illuminate(-1, -1)
        return []

    elif game_area.get_square(x, y)[0] == "d":
        den_open_coords_xy = []
        for step in game_area.get_square(x, y)[1]:
            if game_area.get_open(*step):
                den_open_coords_xy.append(step)

        print(f"{den_open_coords_xy = }")
        print(f"{len(den_open_coords_xy) = }")

        if len(den_open_coords_xy) == 2 and \
                den_open_coords_xy != game_area.get_square(x, y)[1]:
            print(f"{game_area.get_square(x, y)[1] = }")
            print(f"{game_players.take_other_pawn(x, y) = }")
            print(f"{game_players.get_select() = }")

            for coord_xy in den_open_coords_xy:
                if coord_xy != (x, y):
                    if game_players.check_other_pawns(*coord_xy) != 0:
                        game_players.kick_pawn(game_players.get_select())
                    game_players.get_pawn(game_players.take_other_pawn(*coord_xy)).last = \
                        [*game_players.get_pawn(game_players.take_other_pawn(*coord_xy)).curr]
                    game_players.get_pawn(game_players.take_other_pawn(*coord_xy)).curr = [x, y]

        for step in den_open_coords_xy:
            game_area.set_square(step[0], step[1], ["d", den_open_coords_xy])

    elif game_area.get_square(x, y)[0] == "g":
        game_players.gunshot(x, y, game_area)

    elif game_area.get_square(x, y)[0] == "c":
        game_players.set_pawn_curr(game_players.get_select_pawn().last)
        return check_second_steps(game_players.get_pawn(game_players.get_select()).curr[0],
                                  game_players.get_pawn(game_players.get_select()).curr[1])

    if game_area.get_square(*game_players.get_select_pawn().last)[0] == "p":
        game_area.set_square(game_players.get_select_pawn().last[0],
                             game_players.get_select_pawn().last[1],
                             ["p", False])

    if "m" in game_area.get_square(x, y)[0] and \
            game_area.get_square(x, y)[0] != "m" and \
            game_area.get_square(x, y)[1]:
        game_area.get_square(x, y)[1] = False

        if game_area.get_square(x, y)[0][1] != "c":
            game_area.set_money(x, y, int(game_area.get_square(x, y)[0][1]))
            game_area.print_area("moneys", "Поле", ps="Монетки")
        else:
            pass

    game_players.cancel_select()
    game_mode = "select"
    game_cycle.set_next()
    return []


def mouse_click(coord_xy: tuple, color: str, delay: float):
    global way_pawn, game_mode
    x = (coord_xy[0] - place_x) // scope
    y = (coord_xy[1] - place_y) // scope
    if game_mode == "lighthouse":
        illuminate(x, y)
    else:
        if game_mode == "select":
            game_players.select(x, y, color)
            way_pawn = mouse_click_select(x, y, delay)
        elif game_mode == "move":
            mouse_click_move(x, y, delay)
    if game_area.inside_area(x, y):
        window.update_window(game_area, game_players)
        window.print_in_window(f"{game_area.get_square(x, y)}\n{x}, {y}", coord_xy)


window_height = 800
window_width = window_height * 16 / 9

fps = 60
scope = 95
place_x = 90
place_y = 10
time_tap = 0.17
way_pawn = []
clock = pygame.time.Clock()

flag_holdup = False
temp_time = 0.0
running = True

# Цвета
bg_color = (255, 255, 255)
text_color = (0, 0, 0)
mark_step_color = (50, 205, 50, 255 / 2)
mark_select_color = (0, 255, 0, 255 / 1.5)
mark_frame_color = (0, 128, 0)
mark_block_color = (255, 0, 0)
pawn_select_color = (50, 205, 50)
# mark_step_color = (139, 0, 139, 255 / 2)
# white = (255, 255, 255)
# dark_blue_a = (0, 0, 139, 255/2)
# dark_blue = (0, 0, 139, 255)
# deep_pink_a = (255, 20, 147, 255/2)

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

if not file2area("AreaN1.txt", hide=True):
    exit()
setup_dict = file2area("AreaN1.txt")

game_mode = "select"  # select — выбор пешки, move — ход пешкой
game_cycle = TheGameCycle(setup_dict["start_coord_xy"], setup_dict["start_boat"])
game_players = Players(setup_dict["start_coord_xy"], setup_dict["pawns"])
game_area = Area(setup_dict["area"], setup_dict["squares"])
game_area.mix_area()
window = Screen()
pawn2color = setup_dict["pawn2color"]


#
def set_1test_area():
    game_area.clear_area()
    game_area.fill_area(["e2"])

    game_area.set_square(2, 5, ["m5", True])

    game_area.set_square(3, 6, ["a2", [5]])
    game_area.set_square(3, 7, ["a2", [4]])
    game_area.set_square(6, 6, ["h"])
    game_area.set_square(7, 8, ["2"])

    game_area.set_square(2, 7, ["a2", [2]])
    game_area.set_square(2, 8, ["a2", [2]])
    game_area.set_square(2, 9, ["a2", [2]])
    game_area.set_square(1, 9, ["f"])
    game_area.set_square(3, 9, ["f"])

    game_area.set_square(7, 8, ["a7", [3, 4, 7]])
    game_area.set_square(2, 2, ["p", True])
    game_area.set_square(3, 3, ["f"])
    game_area.set_square(4, 5, ["c"])
    game_area.set_square(9, 7, ["r"])
    game_area.set_square(1, 4, ["j"])
    game_area.set_square(6, 10, ["g", [4]])
    game_area.set_square(10, 3, ["q", True])

    game_area.set_square(8, 5, ["d", [(8, 5), (8, 10), (2, 7), (6, 2)]])
    game_area.set_square(8, 10, ["d", [(8, 5), (8, 10), (2, 7), (6, 2)]])
    game_area.set_square(2, 7, ["d", [(8, 5), (8, 10), (2, 7), (6, 2)]])
    game_area.set_square(6, 2, ["d", [(8, 5), (8, 10), (2, 7), (6, 2)]])

    game_area.set_square(9, 10, ["a1", [3]])
    game_area.set_square(10, 9, ["c"])

    game_area.set_square(2, 11, ["a2", [5]])
    game_area.set_square(3, 11, ["2"])
    game_area.set_square(4, 11, ["a2", [4]])

    # areaSquares[11][4] = ["a3", [4, 5]]
    # areaSquares[11][6] = ["a3", [4, 5]]
    game_area.set_square(9, 6, ["2"])
    # areaSquares[3][4] = ["2"]
    game_area.set_square(4, 3, ["a2", [4]])
    game_area.set_square(10, 2, ["l", 3])
    game_area.set_square(4, 1, ["2"])

    game_area.set_square(11, 6, ["a2", [4]])

    game_area.set_square(5, 11, ["tc"])
    game_area.set_square(6, 11, ["t2"])
    game_area.set_square(7, 11, ["t3"])
    game_area.set_square(8, 11, ["t4"])
    game_area.set_square(9, 11, ["t5"])


def set_2test_area():
    game_area.clear_area()
    game_area.fill_area(["e2"])
    game_area.set_square(3, 5, ["2"])
    game_area.set_square(3, 6, ["2"])
    game_area.set_square(3, 7, ["2"])
    game_area.set_square(3, 8, ["2"])

    game_area.set_square(4, 6, ["2"])
    game_area.set_square(4, 7, ["2"])
    game_area.set_square(4, 8, ["2"])

    game_area.set_square(5, 7, ["2"])
    game_area.set_square(5, 8, ["2"])

    game_area.set_square(6, 8, ["2"])

    game_area.set_square(2, 5, ["a2", [5]])
    game_area.set_square(2, 6, ["a2", [5]])
    game_area.set_square(2, 7, ["a2", [5]])
    game_area.set_square(2, 8, ["a2", [5]])

    game_area.set_square(4, 5, ["a2", [4]])
    game_area.set_square(5, 6, ["a2", [4]])
    game_area.set_square(6, 7, ["a2", [4]])
    game_area.set_square(7, 8, ["a2", [4]])

    game_area.set_square(2, 3, ["a1", [3]])
    game_area.set_square(3, 2, ["a1", [6]])

    game_area.set_square(5, 2, ["a1", [8]])
    game_area.set_square(6, 3, ["a1", [1]])

    game_area.set_square(8, 2, ["a2", [5]])
    game_area.set_square(9, 2, ["a2", [4]])


def set_3test_area():
    game_area.clear_area()
    game_area.fill_area(["e2"])
    game_area.set_square(1, 3, ["a1", [3]])
    game_area.set_square(1, 4, ["a1", [3]])
    game_area.set_square(1, 5, ["a1", [3]])
    game_area.set_square(1, 6, ["a1", [3]])

    game_area.set_square(3, 1, ["a1", [6]])
    game_area.set_square(4, 1, ["a1", [6]])
    game_area.set_square(5, 1, ["a1", [6]])
    game_area.set_square(6, 1, ["a1", [6]])

    game_area.set_square(5, 6, ["a1", [8]])
    game_area.set_square(6, 6, ["a1", [8]])
    game_area.set_square(7, 6, ["a1", [8]])
    game_area.set_square(8, 6, ["a1", [8]])

    game_area.set_square(10, 8, ["a1", [1]])
    game_area.set_square(10, 9, ["a1", [1]])
    game_area.set_square(10, 10, ["a1", [1]])
    game_area.set_square(10, 11, ["a1", [1]])

    game_area.set_square(2, 2, ["2"])
    game_area.set_square(2, 3, ["2"])
    game_area.set_square(2, 4, ["2"])
    game_area.set_square(2, 5, ["2"])

    game_area.set_square(3, 2, ["2"])
    game_area.set_square(3, 3, ["2"])
    game_area.set_square(3, 4, ["2"])

    game_area.set_square(4, 2, ["2"])
    game_area.set_square(4, 3, ["2"])

    game_area.set_square(5, 2, ["2"])

    game_area.set_square(9, 7, ["2"])
    game_area.set_square(9, 8, ["2"])
    game_area.set_square(9, 9, ["2"])
    game_area.set_square(9, 10, ["2"])

    game_area.set_square(8, 7, ["2"])
    game_area.set_square(8, 8, ["2"])
    game_area.set_square(8, 9, ["2"])

    game_area.set_square(7, 7, ["2"])
    game_area.set_square(7, 8, ["2"])

    game_area.set_square(6, 7, ["2"])


def set_4test_area():
    game_area.clear_area()
    game_area.fill_area(["e2"])

    game_area.set_square(3, 2, ["a2", [5]])
    game_area.set_square(4, 2, ["a2", [4]])
    game_area.set_square(5, 2, ["a2", [4]])
    game_area.set_square(7, 2, ["a2", [5]])
    game_area.set_square(8, 2, ["a2", [5]])
    game_area.set_square(9, 2, ["a2", [4]])

    game_area.set_square(2, 3, ["a2", [5]])
    game_area.set_square(3, 3, ["a2", [4]])
    game_area.set_square(4, 3, ["a2", [4]])
    game_area.set_square(5, 3, ["a2", [4]])
    game_area.set_square(7, 3, ["a2", [5]])
    game_area.set_square(8, 3, ["a2", [5]])
    game_area.set_square(9, 3, ["a2", [5]])
    game_area.set_square(10, 3, ["a2", [4]])

    game_area.set_square(1, 4, ["a2", [5]])
    game_area.set_square(2, 4, ["a2", [4]])
    game_area.set_square(3, 4, ["a2", [4]])
    game_area.set_square(4, 4, ["a2", [4]])
    game_area.set_square(5, 4, ["a2", [4]])
    game_area.set_square(7, 4, ["a2", [5]])
    game_area.set_square(8, 4, ["a2", [5]])
    game_area.set_square(9, 4, ["a2", [5]])
    game_area.set_square(10, 4, ["a2", [5]])
    game_area.set_square(11, 4, ["a2", [4]])

    game_area.set_square(6, 7, ["a1", [6]])
    game_area.set_square(8, 7, ["a1", [6]])
    game_area.set_square(10, 7, ["a1", [6]])

    game_area.set_square(5, 8, ["a1", [6]])
    game_area.set_square(7, 8, ["a1", [6]])
    game_area.set_square(9, 8, ["a1", [6]])

    game_area.set_square(4, 9, ["a1", [6]])
    game_area.set_square(6, 9, ["a1", [6]])
    game_area.set_square(8, 9, ["a1", [3]])

    game_area.set_square(3, 10, ["a1", [6]])
    game_area.set_square(5, 10, ["a1", [3]])

    game_area.set_square(2, 11, ["a1", [3]])


def set_5test_area():
    game_area.clear_area()
    game_area.fill_area(["e2"])

    game_area.set_square(1, 2, ["a2", [7]])
    game_area.set_square(1, 3, ["a2", [5]])
    game_area.set_square(2, 3, ["a1", [1]])

    game_area.set_square(4, 2, ["a2", [7]])
    game_area.set_square(5, 2, ["a2", [4]])
    game_area.set_square(4, 3, ["a1", [3]])

    game_area.set_square(7, 2, ["a2", [5]])
    game_area.set_square(8, 2, ["a2", [7]])
    game_area.set_square(8, 3, ["a1", [1]])

    game_area.set_square(11, 2, ["a1", [6]])
    game_area.set_square(11, 3, ["a2", [2]])
    game_area.set_square(10, 3, ["a2", [5]])

    game_area.set_square(9, 9, ["a2", [5]])
    game_area.set_square(10, 10, ["a2", [4]])
    game_area.set_square(10, 9, ["a2", [7]])
    game_area.set_square(9, 10, ["a2", [2]])

    game_area.set_square(1, 5, ["a2", [7]])
    game_area.set_square(1, 6, ["2"])
    game_area.set_square(2, 6, ["2"])
    game_area.set_square(1, 7, ["a2", [5]])
    game_area.set_square(2, 7, ["2"])
    game_area.set_square(3, 7, ["a1", [1]])

    game_area.set_square(5, 5, ["a2", [7]])
    game_area.set_square(6, 5, ["2"])
    game_area.set_square(7, 5, ["a2", [4]])
    game_area.set_square(5, 6, ["2"])
    game_area.set_square(6, 6, ["2"])
    game_area.set_square(5, 7, ["a1", [3]])

    game_area.set_square(1, 9, ["a1", [8]])
    game_area.set_square(2, 9, ["2"])
    game_area.set_square(3, 9, ["a2", [4]])
    game_area.set_square(2, 10, ["2"])
    game_area.set_square(3, 10, ["2"])
    game_area.set_square(3, 11, ["a2", [2]])

    game_area.set_square(7, 9, ["a1", [6]])
    game_area.set_square(7, 10, ["2"])
    game_area.set_square(6, 10, ["2"])
    game_area.set_square(7, 11, ["a2", [2]])
    game_area.set_square(6, 11, ["2"])
    game_area.set_square(5, 11, ["a2", [5]])


def set_6test_area():
    game_area.clear_area()
    game_area.fill_area(["e2"])

    game_area.set_square(3, 1, ["a1", [6]])
    game_area.set_square(2, 2, ["a1", [8]])
    game_area.set_square(4, 2, ["a1", [1]])
    game_area.set_square(3, 3, ["a1", [3]])

    game_area.set_square(1, 5, ["a2", [5]])
    game_area.set_square(2, 5, ["2"])
    game_area.set_square(3, 5, ["a2", [7]])
    game_area.set_square(1, 6, ["2"])

    game_area.set_square(3, 6, ["2"])
    game_area.set_square(1, 7, ["a2", [2]])
    game_area.set_square(2, 7, ["2"])
    game_area.set_square(3, 7, ["a2", [4]])

    game_area.set_square(7, 5, ["a1", [8]])
    game_area.set_square(8, 6, ["2"])
    game_area.set_square(9, 7, ["a1", [6]])
    game_area.set_square(8, 8, ["2"])
    game_area.set_square(7, 9, ["a1", [1]])
    game_area.set_square(6, 8, ["2"])
    game_area.set_square(5, 7, ["a1", [3]])
    game_area.set_square(6, 6, ["2"])


def set_7test_area():
    game_area.clear_area()
    game_area.fill_area(["e2"])

    game_area.set_square(2, 2, ["a2", [5]])
    game_area.set_square(3, 2, ["a3", [4, 5]])
    game_area.set_square(4, 2, ["a2", [4]])

    game_area.set_square(6, 1, ["a2", [7]])
    game_area.set_square(6, 2, ["a3", [2, 7]])
    game_area.set_square(6, 3, ["a2", [2]])

    game_area.set_square(3, 4, ["a1", [6]])
    game_area.set_square(2, 5, ["a4", [3, 6]])
    game_area.set_square(1, 6, ["a1", [3]])

    game_area.set_square(1, 8, ["a1", [8]])
    game_area.set_square(2, 9, ["a4", [1, 8]])
    game_area.set_square(3, 10, ["a1", [1]])

    game_area.set_square(6, 5, ["a2", [7]])
    game_area.set_square(5, 6, ["a2", [5]])
    game_area.set_square(6, 6, ["a6", [2, 4, 5, 7]])
    game_area.set_square(7, 6, ["a2", [4]])
    game_area.set_square(6, 7, ["a2", [2]])

    game_area.set_square(5, 9, ["a1", [8]])
    game_area.set_square(7, 9, ["a1", [6]])
    game_area.set_square(6, 10, ["a5", [1, 3, 6, 8]])
    game_area.set_square(5, 11, ["a1", [3]])
    game_area.set_square(7, 11, ["a1", [1]])


def set_8test_area():
    game_area.clear_area()
    game_area.fill_area(["e2"])

    game_area.set_square(4, 2, ["a1", [6]])
    game_area.set_square(2, 3, ["a2", [5]])
    game_area.set_square(3, 3, ["a7", [3, 4, 7]])
    game_area.set_square(3, 4, ["a2", [2]])

    game_area.set_square(7, 2, ["a1", [8]])
    game_area.set_square(8, 3, ["a7", [1, 7, 5]])
    game_area.set_square(9, 3, ["a2", [4]])
    game_area.set_square(8, 4, ["a2", [2]])

    game_area.set_square(3, 7, ["a2", [7]])
    game_area.set_square(2, 8, ["a2", [5]])
    game_area.set_square(3, 8, ["a7", [8, 2, 4]])
    game_area.set_square(4, 9, ["a1", [1]])

    game_area.set_square(8, 7, ["a2", [7]])
    game_area.set_square(8, 8, ["a7", [6, 2, 5]])
    game_area.set_square(9, 8, ["a2", [4]])
    game_area.set_square(7, 9, ["a1", [3]])


def set_9test_area():
    game_area.clear_area()
    game_area.fill_area(["e2"])

    game_area.set_square(2, 2, ["a6", [2, 4, 5, 7]])
    game_area.set_square(3, 3, ["a6", [2, 4, 5, 7]])
    game_area.set_square(3, 2, ["a6", [2, 4, 5, 7]])
    game_area.set_square(2, 3, ["a6", [2, 4, 5, 7]])

    game_area.set_square(6, 2, ["a7", [6, 2, 5]])
    game_area.set_square(5, 3, ["a7", [3, 4, 7]])

    game_area.set_square(2, 5, ["a2", [5]])
    game_area.set_square(3, 5, ["a3", [4, 5]])

    game_area.set_square(5, 6, ["a4", [3, 6]])
    game_area.set_square(6, 5, ["a4", [3, 6]])

    game_area.set_square(3, 7, ["a3", [4, 5]])
    game_area.set_square(2, 7, ["a3", [2, 7]])
    game_area.set_square(2, 8, ["a3", [4, 5]])
    game_area.set_square(3, 8, ["a3", [2, 7]])

    game_area.set_square(5, 8, ["a3", [4, 5]])
    game_area.set_square(6, 8, ["a3", [4, 5]])

    game_area.set_square(2, 10, ["a7", [1, 5, 7]])
    game_area.set_square(3, 10, ["a7", [3, 4, 7]])
    game_area.set_square(2, 11, ["a7", [6, 2, 5]])
    game_area.set_square(3, 11, ["a7", [8, 2, 4]])

    game_area.set_square(9, 2, ["a5", [1, 3, 6, 8]])
    game_area.set_square(11, 2, ["a5", [1, 3, 6, 8]])
    game_area.set_square(10, 3, ["a5", [1, 3, 6, 8]])
    game_area.set_square(9, 4, ["a5", [1, 3, 6, 8]])
    game_area.set_square(11, 4, ["a5", [1, 3, 6, 8]])


def set_10test_area():
    game_area.clear_area()
    game_area.fill_area(["e2"])

    game_area.set_square(2, 2, ["a6", [2, 4, 5, 7]])
    game_area.set_square(3, 2, ["2"])
    game_area.set_square(4, 2, ["a6", [2, 4, 5, 7]])
    game_area.set_square(2, 3, ["2"])

    game_area.set_square(4, 3, ["2"])
    game_area.set_square(2, 4, ["a6", [2, 4, 5, 7]])
    game_area.set_square(3, 4, ["2"])
    game_area.set_square(4, 4, ["a6", [2, 4, 5, 7]])

    game_area.set_square(2, 6, ["a7", [1, 5, 7]])
    game_area.set_square(3, 6, ["2"])
    game_area.set_square(4, 6, ["a7", [3, 4, 7]])
    game_area.set_square(2, 7, ["2"])

    game_area.set_square(4, 7, ["2"])
    game_area.set_square(2, 8, ["a7", [6, 2, 5]])
    game_area.set_square(3, 8, ["2"])
    game_area.set_square(4, 8, ["a7", [8, 2, 4]])

    game_area.set_square(2, 10, ["a2", [5]])
    game_area.set_square(3, 10, ["2"])
    game_area.set_square(4, 10, ["a3", [4, 5]])

    game_area.set_square(8, 1, ["a7", [6, 2, 5]])
    game_area.set_square(7, 2, ["2"])
    game_area.set_square(6, 3, ["a7", [3, 4, 7]])

    game_area.set_square(8, 5, ["a4", [3, 6]])
    game_area.set_square(7, 6, ["2"])
    game_area.set_square(6, 7, ["a4", [3, 6]])

    game_area.set_square(6, 10, ["a3", [4, 5]])
    game_area.set_square(7, 10, ["2"])
    game_area.set_square(8, 10, ["a3", [4, 5]])


def set_11test_area():
    game_area.clear_area()
    game_area.fill_area(["e2"])

    game_area.set_square(4, 4, ["a5", [1, 3, 6, 8]])
    game_area.set_square(5, 5, ["2"])
    game_area.set_square(6, 6, ["a5", [1, 3, 6, 8]])
    game_area.set_square(7, 7, ["2"])
    game_area.set_square(8, 8, ["a5", [1, 3, 6, 8]])

    game_area.set_square(8, 4, ["a5", [1, 3, 6, 8]])
    game_area.set_square(7, 5, ["2"])
    game_area.set_square(5, 7, ["2"])
    game_area.set_square(4, 8, ["a5", [1, 3, 6, 8]])


#


set_1test_area()

game_area.print_area("squares", "Массив", ps="Поле")
game_area.print_area("squares", "Поле", ps="Поле")
window.update_window(game_area, game_players)

print("\033[36m{}\033[0m".format("\n☸ Игра началась ☸"))

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
                    mouse_click(event.pos, game_cycle.get_current(),
                                time.time() - temp_time)  # update_window() внутри print_in_window()
                if event.button == 3:
                    mouse_click_cancel_select(event.pos, time.time() - temp_time)
                    window.update_window(game_area, game_players)
            flag_holdup = False

        elif event.type == pygame.MOUSEWHEEL:
            change_scope(event.y)
            window.update_window(game_area, game_players)

        elif event.type == pygame.MOUSEMOTION and flag_holdup:
            change_place(event.rel)
            window.update_window(game_area, game_players)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                game_area.mix_area()
                game_area.print_area("squares", "Поле", ps="Поле")

            elif event.key == pygame.K_o:
                game_area.open_area()

            elif event.key == pygame.K_v:
                game_players.drunk(game_area)

            elif event.key == pygame.K_r:
                game_players.reborn_pawn(game_area)

            elif event.key == pygame.K_n:
                game_cycle.set_next()

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

            window.update_window(game_area, game_players)
    clock.tick(fps)
