from tkinter import *
import math
import time
import typing
import random

one = [-1, 1]

squares_quantity = [5, 4, 5, 4,
                    3, 3, 3, 3, 3, 3, 3,
                    2,
                    1, 2, 4, 5,
                    6, 3, 4, 1,
                    2, 1,
                    1, 2, 3, 5, 5, 1,
                    1, 1,
                    2, 2, 1,
                    1, 1, 1,
                    1, 2, 3,
                    4, 4,
                    1, 3, 2+4 # убрать 4 !!!
                    ]
squares = [["e1"], ["e2"], ["e3"], ["e4"],
           ["a1"], ["a2"], ["a3"], ["a4"], ["a5"], ["a6"], ["a7"],
           ["h"],
           ["t5"], ["t4"], ["t3"], ["t2"],
           ["2"], ["tc"], ["c"], ["w"],
           ["f"], ["r"],
           ["m5"], ["m4"], ["m3"], ["m2"], ["m1"], ["mc"],
           ["p"], ["tk"],
           ["b"], ["g"], ["l"],
           ["F"], ["B"], ["M"],
           ["v3"], ["v2"], ["v1"],
           ["d"], ["tv"],
           ["q"], ["j"], ["m"]
           ]

area_squareOpen = [[[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13]],
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


area_square = [[[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13]],
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

area_pawns = [[[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13]],
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


def own_rand(start, end):
    return random.randrange(start, end)


def own_copy(copied: list):
    inserted = []
    for i in range(0, len(copied)):
        inserted.append(copied[i])
    return inserted


def own_vector(vector_number: int):
    if vector_number == 1:
        return [-1, -1]
    elif vector_number == 2:
        return [0, -1]
    elif vector_number == 3:
        return [1, -1]
    elif vector_number == 4:
        return [-1, 0]
    elif vector_number == 5:
        return [1, 0]
    elif vector_number == 6:
        return [-1, 1]
    elif vector_number == 7:
        return [0, 1]
    elif vector_number == 8:
        return [1, 1]


def get_area_square(area: list, x: int, y: int, value=-1) -> list:
    area[y][x][0] = value
    return area


def clear_area(area: list):
    for y in range(0, len(area)):
        for x in range(0, len(area[y])):
            get_area_square(area, x, y, 0)
    return area


def mix_area(area: list) -> list:
    squares_ = squares[:]
    squares_quantity_ = squares_quantity[:]
    for y in range(1, len(area) - 1):
        for x in range(1, len(area[y]) - 1):
            if not ((x == 1 or x == 11) and (y == 1 or y == 11)):
                while True:
                    choose = own_rand(0, len(squares_))
                    if squares_quantity_[choose] != 0:
                        squares_quantity_[choose] -= 1
                        if squares_[choose][0] == "g":
                            area[y][x] = ["g", *random.sample([2, 4, 5, 7], 1)]
                            break
                        elif squares_[choose][0] == "a1":
                            area[y][x] = ["a1", *random.sample([1, 3, 6, 8], 1)]
                            break
                        elif squares_[choose][0] == "a2":
                            area[y][x] = ["a2", *random.sample([2, 4, 5, 7], 1)]
                            break
                        elif squares_[choose][0] == "a3":
                            area[y][x] = ["a3", *random.sample([[4, 5], [2, 7]], 1)]
                            break
                        elif squares_[choose][0] == "a4":
                            area[y][x] = ["a4", *random.sample([[1, 8], [3, 6]], 1)]
                            break
                        elif squares_[choose][0] == "a5":
                            area[y][x] = ["a5", [1, 3, 6, 8]]
                            break
                        elif squares_[choose][0] == "a6":
                            area[y][x] = ["a6", [2, 4, 5, 7]]
                            break
                        elif squares_[choose][0] == "a7":
                            area[y][x] = ["a7", *random.sample([[1, 5, 7], [3, 4, 7], [6, 5, 2], [8, 4, 2]], 1)]
                            break
                        else:
                            area[y][x][0] = squares_[choose][0]
                            break
    return area








def OLDmix_area(area: list):
    squares_ = own_copy(squares)
    squares_quantity_ = own_copy(squares_quantity)
    for y in range(1, len(area)-1):
        # print("----111")
        for x in range(1, len(area[y]) - 1):
            # print("---34-111")
            choose = own_rand(0, len(squares_))
            # choose = 43
            # print(choose)
            # print(squares_)
            # print(squares_quantity_)
            # print(len(squares_))
            # print(len(squares_quantity_))
            while True:
                # print(1)
                if squares_quantity_[choose] != 0:
                    squares_quantity_[choose] -= 1
                    # print("Первый")
                    if squares_[choose][0] == "g":
                        # print("Втлоро")
                        area[y][x] = ["g", *random.sample([2, 4, 5, 7], 1)]
                        break
                    elif squares_[choose][0] == "a1":
                        # print("четве")
                        area[y][x] = ["a1", *random.sample([1, 3, 6, 8], 1)]
                        break
                    elif squares_[choose][0] == "a2":
                        # print("пятый")
                        area[y][x] = ["a2", *random.sample([2, 4, 5, 7], 1)]
                        break
                    elif squares_[choose][0] == "a3":
                        # print("шестой")
                        area[y][x] = ["a3", *random.sample([[4, 5], [2, 7]], 1)]
                        break
                    elif squares_[choose][0] == "a4":
                        # print("седьмой")
                        area[y][x] = ["a4", *random.sample([[1, 8], [3, 6]], 1)]
                        break
                    elif squares_[choose][0] == "a5":
                        # print("восьной")
                        area[y][x] = ["a5", *[1, 3, 6, 8]]
                        break
                    elif squares_[choose][0] == "a6":
                        # print("девярый")
                        area[y][x] = ["a6", *[2, 4, 5, 7]]
                        break
                    elif squares_[choose][0] == "a7":
                        # print("10ТЫй")
                        area[y][x] = ["a7", *random.sample([[1, 5, 7], [3, 4, 7], [6, 5, 2], [8, 4, 2]], 1)]
                        break
                    else:
                        # print("11цапый")
                        area[y][x][0] = squares_[choose][0]
                        break

                else:
                    if choose != len(squares_) - 1:
                        choose += 1
                    else:
                        choose = 0
            # print("----------------------", squares_quantity_)
    return area


def random_area_xy(area: typing.List, element: typing.List, quantity = 1):
    counter = 0
    while counter <= quantity:
        x = random.randrange(0, 12)
        y = random.randrange(0, 12)
        if area[x][y][0] == 0:
            area[x][y] = element
            counter += 1
    return area


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













def quantity_step_arrow(x: int, y: int, used_steps: set, directions: list):
    print(f"↗ Проверка стрелки:  "
          f"{x}, {y}{' ' * (4 - (x // 10 + y // 10))}{used_steps}")

    for digit in directions:
        new_x = x + digit2delta[digit][0]
        new_y = y + digit2delta[digit][1]
        if 0 <= new_x < len(areaSquares) and \
                0 <= new_y < len(areaSquares):
            if areaOpen[new_y][new_x][0] == 1:
                if areaSquares[new_y][new_x][0] == "a1" and (new_x, new_y) not in used_steps:
                    used_steps.add((new_x, new_y))
                    quantity_step_arrow(new_x, new_y, used_steps, areaSquares[new_y][new_x][1])
                elif areaSquares[new_y][new_x][0] == "a2" and (new_x, new_y) not in used_steps:
                    used_steps.add((new_x, new_y))
                    quantity_step_arrow(new_x, new_y, used_steps, areaSquares[new_y][new_x][1])
                elif areaSquares[new_y][new_x][0] == "a3" and (new_x, new_y) not in used_steps:
                    used_steps.add((new_x, new_y))
                    quantity_step_arrow(new_x, new_y, used_steps, areaSquares[new_y][new_x][1])
                elif areaSquares[new_y][new_x][0] == "a4" and (new_x, new_y) not in used_steps:
                    used_steps.add((new_x, new_y))
                    quantity_step_arrow(new_x, new_y, used_steps, areaSquares[new_y][new_x][1])
                elif areaSquares[new_y][new_x][0] == "a5" and (new_x, new_y) not in used_steps:
                    used_steps.add((new_x, new_y))
                    quantity_step_arrow(new_x, new_y, used_steps, areaSquares[new_y][new_x][1])
                elif areaSquares[new_y][new_x][0] == "a6" and (new_x, new_y) not in used_steps:
                    used_steps.add((new_x, new_y))
                    quantity_step_arrow(new_x, new_y, used_steps, areaSquares[new_y][new_x][1])
                elif areaSquares[new_y][new_x][0] == "a7" and (new_x, new_y) not in used_steps:
                    used_steps.add((new_x, new_y))
                    quantity_step_arrow(new_x, new_y, used_steps, areaSquares[new_y][new_x][1])
                elif areaSquares[new_y][new_x][0] == "S" and (new_x, new_y) not in used_steps:
                    used_steps.add((new_x, new_y))
                elif (new_x, new_y) not in used_steps:
                    quantity_step(new_x, new_y, digit, used_steps)
            else:
                used_steps.add((new_x, new_y))


# Field — Поле, Coast — берег
def quantity_step(x: int, y: int, digit: int, used_steps: set, mode="Field"):
    print(f"☐ Проверка шага:     "
          f"{x}, {y}{' ' * (4 - (x // 10 + y // 10))}{used_steps}")

    if 0 <= x < len(areaSquares) and \
            0 <= y < len(areaSquares):
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
            mode = "Coast"
        elif areaSquares[y][x][0] == "p":
            if areaSquares[y][x][1]:  # True, если не использовали
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
        print(step, areaSquares[step[1]][step[0]])
        if "a" in areaSquares[step[1]][step[0]][0] and \
                areaOpen[step[1]][step[0]][0] == 1:
            extra_steps.add(step)
    allowed_steps -= extra_steps
    allowed_steps = list(allowed_steps)
    print_area(allowed_steps, "Строка", ps="Координаты, куда ходить")
    return allowed_steps


def mouse_click_select(x_y: tuple, color: str, delay: float) -> list:
    global scope, game_mode
    x = (x_y[0] - place_x) // scope
    y = (x_y[1] - place_y) // scope
    if 0 <= x < len(areaSquares) and 0 <= y < len(areaSquares):
        for pawn in pawns:
            if pawn["color"] == color and \
                    x == pawn["current"][0] and \
                    y == pawn["current"][1]:
                pawn["select"] = True
                game_mode = "move"
                print("\033[35m{}\033[0m".format(f"Выбор пешки:         "
                                                 f"{x}, {y}{' ' * (4 - (x // 10 + y // 10))}{areaSquares[y][x]}"
                                                 f"{' ' * (30 - len(str(areaSquares[y][x])))}"
                                                 f"Δt {delay}"))
                print_area_window(f"{areaSquares[y][x]}\n{x}, {y}", x_y)
                quantity_steps(x, y)
                return check_steps(x, y)


def mouse_click_move(x_y: tuple, move: list, delay: float):
    global scope, game_mode, way_pawn
    x = (x_y[0] - place_x) // scope
    y = (x_y[1] - place_y) // scope
    for pawn in pawns:
        if x == pawn["current"][0] and y == pawn["current"][1] and pawn["select"]:
            pawn["select"] = False
            game_mode = "select"
            way_pawn = []
    if move:
        for step in move:
            if x == step[0] and y == step[1]:
                for pawn in pawns:
                    if pawn["select"]:
                        pawn["select"] = False
                        pawn["last"] = [pawn["current"][0], pawn["current"][1]]
                        pawn["current"] = [x, y]
                        open_square(x, y)
                        game_mode = "select"
                        way_pawn = []
                        print("\033[35m{}\033[0m".format(f"Ход пешки:           "
                                                         f"{x}, {y}{' ' * (4 - (x // 10 + y // 10))}{areaSquares[y][x]}"
                                                         f"{' ' * (30 - len(str(areaSquares[y][x])))}"
                                                         f"Δt {delay}"))
                        print_area_window(f"{areaSquares[y][x]}\n{x}, {y}", x_y)



















# area_square = Get_area_square(area_square, 5, 10, value=39)

area_square = clear_area(area_square)

area_square = mix_area(area_square)

# area_square = random_area_xy(area_square, ["a"], quantity=4)

for t in range(0, 11):
    print(area_square[t])
    # for y in range(0, 11):

    # print("\n")

# print('\n'.join(area_square[t]))
# print(area_square[x][y][1])
# print(area_square[t])
