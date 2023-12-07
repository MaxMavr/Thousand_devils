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


file2area("AreaN1.txt")


pawn2color = {
    "W": pawn_white,
    "B": pawn_black,
    "Y": pawn_yellow,
    "R": pawn_red
}
boat_start_coord_xy = {"R": (0, 6),
                       "W": (6, 0),
                       "B": (12, 6),
                       "Y": (6, 12)}


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