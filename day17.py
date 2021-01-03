# Data

def load_data(puzzle):
    f = open('/Users/macuser/Desktop/AdventOfCode/day17_input.txt', 'r')
    l = f.readlines()
    f.close()
    d = {}
    if puzzle == 1:
        for i in range(len(l)):
            line = list(l[i])
            for j in range(len(line)):
                if line[j] == '#':
                    d[(i, j, 0)] = 1
        return d
    elif puzzle == 2:
        for i in range(len(l)):
            line = list(l[i])
            for j in range(len(line)):
                if line[j] == '#':
                    d[(i, j, 0, 0)] = 1
        return d


# puzzle 1
def number_neighbor(xyz, grid):
    num_neighbors = 0
    x, y, z = xyz
    for n_x in [x+1, x, x-1]:
        for n_y in [y+1, y, y-1]:
            for n_z in [z+1, z, z-1]:
                if (n_x, n_y, n_z) in grid:
                    num_neighbors += 1
    return num_neighbors - 1 if xyz in grid else num_neighbors

def compute_minmax(grid):
    x, y, z = [], [], []
    for k in grid:
        x.append(k[0])
        y.append(k[1])
        z.append(k[2])
    max_x, max_y, max_z = max(x) + 2, max(y) + 2, max(z) + 2
    min_x, min_y, min_z = min(x) - 1, min(y) - 1, min(z) - 1

    return [min_x, max_x, min_y, max_y, min_z, max_z]

def solution1(grid, steps):
    new_grid = {}
    for _ in range(steps):
        minmax = compute_minmax(grid)
        for x in range(minmax[0], minmax[1]):
            for y in range(minmax[2], minmax[3]):
                for z in range(minmax[4], minmax[5]):
                    xyz = (x, y, z)
                    n = number_neighbor(xyz, grid)
                    if xyz in grid and n in [3, 2]:
                        new_grid[xyz] = 1
                    elif xyz not in grid and n == 3:
                        new_grid[xyz] = 1
        grid.clear()
        grid, new_grid = new_grid, grid
    return len(grid)

# Puzzle 2

def number_neighbor2(xyzw, grid):
    num_neighbors = 0
    x, y, z, w = xyzw
    for n_x in [x+1, x, x-1]:
        for n_y in [y+1, y, y-1]:
            for n_z in [z+1, z, z-1]:
                for n_w in [w+1, w, w-1]:
                    if (n_x, n_y, n_z, n_w) in grid:
                        num_neighbors += 1
    return num_neighbors - 1 if xyzw in grid else num_neighbors

def compute_minmax2(grid):
    x, y, z, w = [], [], [], []
    for k in grid:
        x.append(k[0])
        y.append(k[1])
        z.append(k[2])
        w.append(k[3])
    max_x, max_y, max_z, max_w = max(x) + 2, max(y) + 2, max(z) + 2, max(w) + 2
    min_x, min_y, min_z, min_w = min(x) - 1, min(y) - 1, min(z) - 1, min(w) - 1

    return [min_x, max_x, min_y, max_y, min_z, max_z, min_w, max_w]

def solution2(grid, steps):
    new_grid = {}
    for _ in range(steps):
        minmax = compute_minmax2(grid)
        for x in range(minmax[0], minmax[1]):
            for y in range(minmax[2], minmax[3]):
                for z in range(minmax[4], minmax[5]):
                    for w in range(minmax[6], minmax[7]):
                        xyzw = (x, y, z, w)
                        n = number_neighbor2(xyzw, grid)
                        if xyzw in grid and n in [3, 2]:
                            new_grid[xyzw] = 1
                        elif xyzw not in grid and n == 3:
                            new_grid[xyzw] = 1
        grid.clear()
        grid, new_grid = new_grid, grid
    return len(grid)

if __name__ == "__main__":
    grid1 = load_data(1)
    grid2 = load_data(2)
    print('----------------------')
    print('Puzzle 1:', solution1(grid1, 6))
    print('----------------------')
    print('Puzzle 2:', solution2(grid2, 6))
    print('----------------------')