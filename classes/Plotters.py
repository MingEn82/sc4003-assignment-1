from typing import List
import time
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from classes.States import State
from classes.Direction import Direction

class UtilityPlotter:
    def __init__(self):
        self.data = {}
    
    def add_data(self, utilities:List[List[float]], layout:List[List[State]]):
        for i, row in enumerate(utilities):
            for j, utility in enumerate(row):
                if layout[i][j].is_wall:
                    continue
                key = f"State({i},{j})"
                self.data[key] = self.data.get(key, []) + [utility]
    
    def plot(self):
        fig, ax = plt.subplots()
        fig.set_size_inches(18.5, 9.5)
        for label, data in self.data.items():
            ax.plot(data, label=label)
        plt.xlabel('Iterations')
        plt.ylabel('Utility Estimates')
        ax.legend(bbox_to_anchor=(1.05, 1), ncol=2, loc='upper left')
        plt.tight_layout()
        plt.show()

class GridWorldPlotter(tk.Frame):
    def __init__(self, master=None, cell_size=70, cols=1):
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
        canvas.create_text(center_x, center_y, text="", fill='#E2E2E2')
    
    def _draw_state(self, canvas:tk.Canvas, x1, y1, x2, y2, text, fill='#FFFFFF', text_color='#000000', font_size=10):
        canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill=fill)
        center_x = x1 + self.cell_size / 2
        center_y = y1 + self.cell_size / 2
        canvas.create_text(center_x, center_y, text=text, fill=text_color, font=("Purisa", font_size))
    
    def draw_estimated_utilities(self, layout:List[List[State]] , utilities:List[List[float]], title="Estimated Utilities", font_size=9):
        canvas = self._load_canvas(layout, title)
        for row in range(self.n_rows):
            for col in range(self.n_cols):
                # Calculate the coordinates for each cell
                x1 = col * self.cell_size
                y1 = row * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size

                if layout[row][col].is_wall:
                    self._draw_wall(canvas, x1, y1, x2, y2)
                else:
                    utility = utilities[row][col]
                    self._draw_state(canvas, x1, y1, x2, y2, text=f"{str(utility):^7.7}", font_size=font_size)
        
    def draw_action(self, layout:List[List[State]] , policy:List[List[Direction]], title="Action", font_size=20):
        canvas = self._load_canvas(layout, title)
        for row in range(self.n_rows):
            for col in range(self.n_cols):
                # Calculate the coordinates for each cell
                x1 = col * self.cell_size
                y1 = row * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size

                if layout[row][col].is_wall:
                    self._draw_wall(canvas, x1, y1, x2, y2)
                else:
                    action = policy[row][col]
                    self._draw_state(canvas, x1, y1, x2, y2, text=f"{action.icon}", font_size=font_size)
    
    def draw_maze(self, layout:List[List[State]], title="Maze", font_size:int=15, cell_size:int=None):
        if cell_size:
            self.cell_size = cell_size

        canvas = self._load_canvas(layout, title)
        for row in range(self.n_rows):
            for col in range(self.n_cols):
                # Calculate the coordinates for each cell
                x1 = col * self.cell_size
                y1 = row * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size

                state = layout[row][col]
                if state.is_wall:
                    self._draw_wall(canvas, x1, y1, x2, y2)
                else:
                    reward = state.reward
                    if reward > 0:
                        text = f"+{reward}"
                        fill = "#46E950"
                    elif reward > -1:
                        text = ""
                        fill = "#FFFFFF"
                    else:
                        text = str(reward)
                        fill = "#FE922B"
                    self._draw_state(canvas, x1, y1, x2, y2, text=text, fill=fill, font_size=font_size)

class ComplexityPlotter:
    def __init__(self):
        self.times = {}
        self.sizes = {}
        self.num_iterations = {}

    def add_data(self, key, size, func, *args, **kwargs):
        self.sizes[key] = self.sizes.get(key, []) + [size]
        start_time = time.perf_counter()
        iterations = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        self.times[key] = self.times.get(key, []) + [total_time]
        self.num_iterations[key] = self.num_iterations.get(key, []) + [np.log(iterations)]

    def plot_times(self):
        fig, ax = plt.subplots()
        fig.set_size_inches(18.5, 9.5)
        for label, data in self.times.items():
            ax.plot(self.sizes[label], data, label=label)
        plt.xlabel('Size of maze')
        plt.ylabel('Time taken for convergence (s)')
        ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        plt.show()
    
    def plot_iterations(self):
        fig, ax = plt.subplots()
        fig.set_size_inches(18.5, 9.5)
        for label, data in self.num_iterations.items():
            ax.plot(self.sizes[label], data, label=label)
        plt.xlabel('Size of maze')
        plt.ylabel('Log number of iterations for convergence')
        ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        plt.show()