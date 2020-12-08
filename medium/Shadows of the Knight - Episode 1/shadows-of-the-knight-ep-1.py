# https://www.codingame.com/training/medium/shadows-of-the-knight-episode-1

dirs = {  # y, x
    'U': (-1, +0),
    'UR': (-1, +1),
    'R': (+0, +1),
    'DR': (+1, +1),
    'D': (+1, +0),
    'DL': (+1, -1),
    'L': (+0, -1),
    'UL': (-1, -1)
}

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]

# building bounds
min_x, max_x = 0, w - 1
min_y, max_y = 0, h - 1

while True:
    # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    bomb_dir = input()
    dy, dx = dirs[bomb_dir]

    def update_coords(dir, coord, min_bound, max_bound):
        if dir > 0:  # not far enough
            min_bound = coord + 1
            tgt = (max_bound - coord + 1) // 2
            coord += tgt
        elif dir < 0:  # too far
            max_bound = coord - 1
            tgt = (coord - min_bound + 1) // 2
            coord -= tgt
        return coord, min_bound, max_bound

    x0, min_x, max_x = update_coords(dx, x0, min_x, max_x)
    y0, min_y, max_y = update_coords(dy, y0, min_y, max_y)

    # the location of the next window Batman should jump to.
    print(f"{x0} {y0}")
