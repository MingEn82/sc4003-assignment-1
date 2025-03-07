import matplotlib.pyplot as plt
import tkinter as tk
from classes.Tile import Wall, Square

class RewardPlotter:
    def __init__(self):
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def clear_scores(self):
        self.scores.clear()
    
    def show_plot(self, smoothen=False):
        x = [i+1 for i in range(len(self.scores))]
        if smoothen:
            y = self._smoothen_rewards(self.scores)
        else:
            y = self.scores
        plt.plot(x, y)
        plt.xlabel("Iterations")
        plt.ylabel("Cumulative Rewards")
        plt.show()
    
    def _smoothen_rewards(self, rewards, smoothing_factor=0.9):
        smoothed_rewards = [rewards[0]]
        for reward in rewards[1:]:
            smoothed_rewards += [
                smoothed_rewards[-1] * smoothing_factor
                + reward * (1 - smoothing_factor)
            ]
        return smoothed_rewards
    
class MazePlotter(tk.Frame):
    def __init__(self, master=None, cell_size=70, cols=3):
        super().__init__(master)
        self.master = master
        self.cell_size = cell_size
        self.cols = cols

        self.n_cols = self.n_rows = 0
        self.canvas_count = 0

    def _load_canvas(self, layout, title=""):
        self.n_rows = len(layout)
        self.n_cols = len(layout[0])
        row_pos = self.canvas_count // self.cols
        col_pos = self.canvas_count % self.cols

        container = tk.Frame(self)
        container.grid(row=row_pos, column=col_pos, padx=5, pady=5)
        if title:
            title_label = tk.Label(container, text=title)
            title_label.pack(side=tk.TOP, pady=(0, 5))

        canvas = tk.Canvas(container, width=self.n_cols * self.cell_size,
                           height=self.n_rows * self.cell_size)
        canvas.pack()
        self.canvas_count += 1
        return canvas
    
    def _draw_wall(self, canvas:tk.Canvas, x1, y1, x2, y2):
        canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill='#808080')
        center_x = x1 + self.cell_size / 2
        center_y = y1 + self.cell_size / 2
        canvas.create_text(center_x, center_y, text="Wall", fill='#E2E2E2')

    def _draw_square(self, canvas:tk.Canvas, x1, y1, x2, y2, text, fill='#FFFFFF', text_color='#000000'):
        canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill=fill)
        center_x = x1 + self.cell_size / 2
        center_y = y1 + self.cell_size / 2
        canvas.create_text(center_x, center_y, text=text, fill=text_color)

    def draw_estimated_utilities(self, layout, title="Estimated Utilities"):
        canvas = self._load_canvas(layout, title)
        for row in range(self.n_rows):
            for col in range(self.n_cols):
                # Calculate the coordinates for each cell
                x1 = col * self.cell_size
                y1 = row * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size

                tile = layout[row][col]
                if isinstance(tile, Wall):
                    self._draw_wall(canvas, x1, y1, x2, y2)
                elif isinstance(tile, Square):
                    self._draw_square(canvas, x1, y1, x2, y2, text=f"{tile.value:^7.7}")
        
    def draw_action(self, layout, title="Action"):
        canvas = self._load_canvas(layout, title)
        for row in range(self.n_rows):
            for col in range(self.n_cols):
                # Calculate the coordinates for each cell
                x1 = col * self.cell_size
                y1 = row * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size

                tile = layout[row][col]
                if isinstance(tile, Wall):
                    self._draw_wall(canvas, x1, y1, x2, y2)
                elif isinstance(tile, Square):
                    self._draw_square(canvas, x1, y1, x2, y2, text=f"{tile.action.icon}")
    
    def draw_maze(self, layout, title="Maze"):
        canvas = self._load_canvas(layout, title)
        for row in range(self.n_rows):
            for col in range(self.n_cols):
                # Calculate the coordinates for each cell
                x1 = col * self.cell_size
                y1 = row * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size

                tile = layout[row][col]
                if isinstance(tile, Wall):
                    self._draw_wall(canvas, x1, y1, x2, y2)
                elif isinstance(tile, Square):
                    reward = tile.reward
                    if reward > 0:
                        text = f"+{tile.reward}"
                        fill = "#46E950"
                    elif reward > -1:
                        text = ""
                        fill = "#FFFFFF"
                    else:
                        text = f"{tile.reward}"
                        fill = "#FE922B"
                    self._draw_square(canvas, x1, y1, x2, y2, text=text, fill=fill)
        