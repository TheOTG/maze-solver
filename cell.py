from point import Point
from line import Line

class Cell():
    def __init__(self, x1, y1, x2, y2, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._win = win
        self.visited = False

    def draw(self):
        if self._win is None:
            return
        
        left_line = Line(
            Point(self._x1, self._y1),
            Point(self._x1, self._y2)
        )
        right_line = Line(
            Point(self._x2, self._y1),
            Point(self._x2, self._y2)
        )
        top_line = Line(
            Point(self._x1, self._y1),
            Point(self._x2, self._y1)
        )
        bottom_line = Line(
            Point(self._x1, self._y2),
            Point(self._x2, self._y2)
        )
        self._win.draw_line(left_line, "black" if self.has_left_wall else "#d9d9d9")
        self._win.draw_line(right_line, "black" if self.has_right_wall else "#d9d9d9")
        self._win.draw_line(top_line, "black" if self.has_top_wall else "#d9d9d9")
        self._win.draw_line(bottom_line, "black" if self.has_bottom_wall else "#d9d9d9")
        
    def draw_move(self, to_cell, undo=False):
        if self._win is None:
            return
        fill_color = "gray" if undo else "red"
        mid_x1 = (self._x1 + self._x2) / 2
        mid_y1 = (self._y1 + self._y2) / 2
        mid_x2 = (to_cell._x1 + to_cell._x2) / 2
        mid_y2 = (to_cell._y1 + to_cell._y2) / 2
        point1 = Point(mid_x1, mid_y1)
        point2 = Point(mid_x2, mid_y2)
        line = Line(point1, point2)
        self._win.draw_line(line , fill_color)