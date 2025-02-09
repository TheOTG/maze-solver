from window import Window
from maze import Maze

def main():
    win = Window(800, 600)

    x = 10
    y = 10
    rows = 10
    cols = 10
    x_size = 20
    y_size = 20

    maze = Maze(x, y, rows, cols, x_size, y_size, win)
    maze.create_cells()
    maze.break_entrance_and_exit()
    maze.break_walls_r(0, 0)
    maze.reset_cells_visited()
    maze.solve()

    win.wait_for_close()

main()