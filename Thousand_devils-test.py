point = [(6, 0), (0, 6), (12, 6), (6, 12)]
result = []

for i in point:
    for j in point:
        s = (j[0] - i[0]) * (j[1] - i[1])
        print(f"({j[0]} - {i[0]}) * ({j[1]} - {i[1]}) = {j[0] - i[0]} * {j[1] - i[1]} = {s}")
        if s < 0:
            print("Заебись!")
            result.append(j)
            break
print(result)




# pawn2color = {
#     "W": pawn_white,
#     "B": pawn_black,
#     "Y": pawn_yellow,
#     "R": pawn_red
# }
# boat_start_coord_xy = {"R": (0, 6),
#                        "W": (6, 0),
#                        "B": (12, 6),
#                        "Y": (6, 12)}
#
#
# squares = {"e1": 5, "e2": 4, "e3": 5, "e4": 4,
#            "a1": 3, "a2": 3, "a3": 3, "a4": 3, "a5": 3, "a6": 3, "a7": 3,
#            "h": 2,
#            "t5": 1, "t4": 2, "t3": 4, "t2": 5,
#            "2": 6, "tc": 3, "c": 4, "w": 1,
#            "f": 2, "r": 1,
#            "m5": 1, "m4": 2, "m3": 3, "m2": 5, "m1": 5, "mc": 1,
#            "p": 1, "tk": 1,
#            "b": 2, "g": 2, "l": 1,
#            "F": 1, "B": 1, "M": 1,
#            "v3": 1, "v2": 2, "v1": 3,
#            "d": 4, "tv": 4,
#            "q": 1, "j": 3, "m": 2
#            }