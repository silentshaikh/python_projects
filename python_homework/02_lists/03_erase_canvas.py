# Implement an 'eraser' on a canvas.

# The canvas consists of a grid of blue 'cells' which are drawn as rectangles on the screen. We then create an eraser rectangle which, when dragged around the canvas, sets all of the rectangles it is in contact with to white.

import tkinter as tk

# Grid configuration
ROWS, COLS = 10, 10
CELL_SIZE = 50
ERASER_SIZE = 60

class EraserCanvasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Canvas Eraser")

        self.canvas = tk.Canvas(root, width=COLS*CELL_SIZE, height=ROWS*CELL_SIZE, bg="white")
        self.canvas.pack()

        self.cells = {}  # {(row, col): cell_id}
        self.draw_grid()

        # Create eraser rectangle
        self.eraser = self.canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, fill="gray", outline="black")
        self.dragging = False

        # Bind mouse events
        self.canvas.tag_bind(self.eraser, "<ButtonPress-1>", self.start_drag)
        self.canvas.tag_bind(self.eraser, "<B1-Motion>", self.do_drag)
        self.canvas.tag_bind(self.eraser, "<ButtonRelease-1>", self.stop_drag)

    def draw_grid(self):
        for row in range(ROWS):
            for col in range(COLS):
                x1 = col * CELL_SIZE
                y1 = row * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE
                cell_id = self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue", outline="black")
                self.cells[(row, col)] = cell_id

    def start_drag(self, event):
        self.dragging = True

    def stop_drag(self, event):
        self.dragging = False

    def do_drag(self, event):
        if self.dragging:
            # Center eraser around the mouse
            x = event.x - ERASER_SIZE // 2
            y = event.y - ERASER_SIZE // 2
            self.canvas.coords(self.eraser, x, y, x + ERASER_SIZE, y + ERASER_SIZE)

            # Get eraser position
            ex1, ey1, ex2, ey2 = self.canvas.coords(self.eraser)

            # Check overlapping cells
            for (row, col), cell_id in self.cells.items():
                cx1 = col * CELL_SIZE
                cy1 = row * CELL_SIZE
                cx2 = cx1 + CELL_SIZE
                cy2 = cy1 + CELL_SIZE

                # Check if eraser overlaps cell
                if not (ex2 < cx1 or ex1 > cx2 or ey2 < cy1 or ey1 > cy2):
                    self.canvas.itemconfig(cell_id, fill="white")

# Run the application
root = tk.Tk()
app = EraserCanvasApp(root)
root.mainloop()
