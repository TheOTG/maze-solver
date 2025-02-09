from cell import Cell
import time
import random

class Maze():
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
            seed=None
        ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self.seed = random.seed(seed)

        self.create_cells()

    def create_cells(self):
        self._cells = []
        for col in range(self.num_cols):
            cell_row = []
            for row in range(self.num_rows):
                cell_row.append(self.draw_cell(row, col))
            self._cells.append(cell_row)

    def draw_cell(self, i, j):
        x1 = self.x1 + (self.cell_size_x * i)
        x2 = x1 + self.cell_size_x
        y1 = self.y1 + (self.cell_size_y * j)
        y2 = y1 + self.cell_size_y

        cell = Cell(x1, y1, x2, y2, self._win)
        cell.draw()
        self.animate()

        return cell

    def animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def break_entrance_and_exit(self):
        if not self._cells:
            return
        entrance = self._cells[0][0]
        exit = self._cells[-1][-1]
        entrance.has_top_wall = False
        exit.has_bottom_wall = False
        entrance.draw()
        exit.draw()

    def break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            left = (i, j - 1)
            right = (i, j + 1)
            top = (i - 1, j)
            bottom = (i + 1, j)

            if left[1] >= 0:
                left_cell = self._cells[left[0]][left[1]]
                if not left_cell.visited:
                    to_visit.append(left)
            if right[1] < self.num_cols:
                right_cell = self._cells[right[0]][right[1]]
                if not right_cell.visited:
                    to_visit.append(right)
            if top[0] >= 0:
                top_cell = self._cells[top[0]][top[1]]
                if not top_cell.visited:
                    to_visit.append(top)
            if bottom[0] < self.num_rows:
                bottom_cell = self._cells[bottom[0]][bottom[1]]
                if not bottom_cell.visited:
                    to_visit.append(bottom)
            
            if len(to_visit) == 0:
                self._cells[i][j].draw()
                return

            direction = random.randrange(0, len(to_visit))
            if to_visit[direction] == left:
                self._cells[i][j].has_left_wall = False
                self._cells[left[0]][left[1]].has_right_wall = False
            if to_visit[direction] == right:
                self._cells[i][j].has_right_wall = False
                self._cells[right[0]][right[1]].has_left_wall = False
            if to_visit[direction] == top:
                self._cells[i][j].has_top_wall = False
                self._cells[top[0]][top[1]].has_bottom_wall = False
            if to_visit[direction] == bottom:
                self._cells[i][j].has_bottom_wall = False
                self._cells[bottom[0]][bottom[1]].has_top_wall = False

            self.break_walls_r(to_visit[direction][0], to_visit[direction][1])

    def reset_cells_visited(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False

    def solve(self):
        return self.solve_r(0, 0)
    
    def solve_r(self, i, j):
        self.animate()
        cell = self._cells[i][j]
        cell.visited = True

        if i == (self.num_rows - 1) and j == (self.num_cols - 1):
            return True

        to_visit = []
        left = (i, j - 1)
        right = (i, j + 1)
        top = (i - 1, j)
        bottom = (i + 1, j)

        if left[1] >= 0:
            left_cell = self._cells[left[0]][left[1]]
            if not left_cell.visited and not cell.has_left_wall and not left_cell.has_right_wall:
                to_visit.append(left)
        if right[1] < self.num_cols:
            right_cell = self._cells[right[0]][right[1]]
            if not right_cell.visited and not cell.has_right_wall and not right_cell.has_left_wall:
                to_visit.append(right)
        if top[0] >= 0:
            top_cell = self._cells[top[0]][top[1]]
            if not top_cell.visited and not cell.has_top_wall and not top_cell.has_bottom_wall:
                to_visit.append(top)
        if bottom[0] < self.num_rows:
            bottom_cell = self._cells[bottom[0]][bottom[1]]
            if not bottom_cell.visited and not cell.has_bottom_wall and not bottom_cell.has_top_wall:
                to_visit.append(bottom)
        
        for direction in to_visit:
            next_cell = self._cells[direction[0]][direction[1]]
            cell.draw_move(next_cell)
            is_solved = self.solve_r(direction[0], direction[1])
            if is_solved:
                return True
            cell.draw_move(next_cell, True)
        
        return False
