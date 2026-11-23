from fish import Fish

CELL_SIZE = 64

class Grid():
    def __init__(self, size_x, size_y):
        self.num_x = size_x // CELL_SIZE + 1
        self.num_y = size_y // CELL_SIZE + 1
        self.cells = [[[] for _ in range (self.num_y)]  for _ in range (self.num_x)]

    def add_fish(self, fish):
        #print("adding fish")
        updated_cells = set() 
        x_first_cell = int(fish.x // CELL_SIZE)
        y_first_cell = int(fish.y // CELL_SIZE)
        cells_x = max(1, int(fish.width) // CELL_SIZE)
        cells_y = max(1, int(fish.height) // CELL_SIZE)
        for i in range (x_first_cell, x_first_cell + cells_x):
            for j in range (y_first_cell, y_first_cell + cells_y):
                if fish not in self.cells[i][j]:
                    self.cells[i][j].append(fish)
                updated_cells.add((i, j))
        return updated_cells

    def update_fish(self, fish):
        #print("updating fish")
        fish_cells = fish.cells.copy()
        new_cells = self.add_fish(fish)
        to_remove = fish_cells - new_cells
        fish.cells = new_cells
        for x, y in to_remove:
            self.cells[x][y].remove(fish)


    def possible_collisions(self, fish):
        #print("running possible collisions")
        possible_collisions = set()
        checked_cells = set()
        for x,y in fish.cells:
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    nx = x + dx
                    ny = y + dy
                    if (nx, ny) in checked_cells:
                        continue
                    checked_cells.add((nx, ny))
                    for other_fish in self.cells[nx][ny]:
                        if other_fish != fish:
                            possible_collisions.add(other_fish)
        #print (f"possible collisions are: {possible_collisions}")
        return possible_collisions

    