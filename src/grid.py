from fish import Fish

CELL_SIZE = 64

class Grid():
    def __init__(self, size_x, size_y):
        self.num_x = size_x / CELL_SIZE
        self.num_y = size_y / CELL_SIZE
        self.cells = [[set() for _ in range num_y]  for _ in range num_x]

    def add_fish(self, fish):
        x_first_cell = fish.x / CELL_SIZE
        y_first_cell = fish.y / CELL_SIZE
        cells_x = fish.width/CELL_SIZE
        cells_y = fish.height/CELL_SIZE
        for i in range (x_first_cell, cells_x):
            for j in range (y_first_cell, cells_y):
                if fish not in cells[i][j]:
                    self.cells[i][j].append(fish)

    