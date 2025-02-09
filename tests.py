import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells2(self):
        num_cols = 5
        num_rows = 5
        m1 = Maze(10, 10, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_break_entrance_exit(self):
        num_cols = 5
        num_rows = 5
        m1 = Maze(10, 10, num_rows, num_cols, 10, 10)
        m1.break_entrance_and_exit()
        entrance = m1._cells[0][0]
        exit = m1._cells[-1][-1]
        self.assertEqual(entrance.has_top_wall, False)
        self.assertEqual(exit.has_bottom_wall, False)

    def test_reset_cells_visited(self):
        num_cols = 5
        num_rows = 5
        m1 = Maze(10, 10, num_rows, num_cols, 10, 10)
        m1.break_walls_r(0, 0)
        m1.reset_cells_visited()
        for row in m1._cells:
            for cell in row:
                self.assertEqual(cell.visited, False)
        
if __name__ == "__main__":
    unittest.main()