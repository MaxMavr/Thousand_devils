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
