import tkinter as tk
import random
from agent import run_ai_agent_once  # 👈 import AI logic

GRID_SIZE = 9
NUM_MINES = 10

class Cell:
    def __init__(self, button, row, col):
        self.button = button
        self.row = row
        self.col = col
        self.is_mine = False
        self.is_revealed = False
        self.adjacent_mines = 0

class MinesweeperGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Minesweeper LLM")
        self.cells = {}
        self.setup_grid()
        self.place_mines()
        self.calculate_adjacent_mines()

        # 👇 Add a button for the AI to make its move
        ai_button = tk.Button(self.root, text="🤖 NPC Move", command=run_ai_agent_once)
        ai_button.grid(row=GRID_SIZE, column=0, columnspan=GRID_SIZE)

    def setup_grid(self):
        for r in range(GRID_SIZE):
            for c in range(GRID_SIZE):
                btn = tk.Button(self.root, width=4, height=2,
                                command=lambda r=r, c=c: self.reveal(r, c))
                btn.grid(row=r, column=c)
                self.cells[(r, c)] = Cell(btn, r, c)

    def place_mines(self):
        mines = random.sample(list(self.cells.keys()), NUM_MINES)
        for coord in mines:
            self.cells[coord].is_mine = True

    def calculate_adjacent_mines(self):
        for (r, c), cell in self.cells.items():
            if cell.is_mine:
                continue
            neighbors = [(r+i, c+j) for i in (-1,0,1) for j in (-1,0,1) if (i,j)!=(0,0)]
            for nr, nc in neighbors:
                if (nr, nc) in self.cells and self.cells[(nr, nc)].is_mine:
                    cell.adjacent_mines += 1

    def reveal(self, r, c):
        cell = self.cells[(r, c)]
        if cell.is_revealed:
            return
        cell.is_revealed = True
        if cell.is_mine:
            cell.button.config(text="M", bg="red")
            self.game_over()
        else:
            text = str(cell.adjacent_mines) if cell.adjacent_mines > 0 else ""
            cell.button.config(text=text, bg="yellow")

    def click_cell(self, row, col):
        """Allows external call to reveal a cell."""
        if (row, col) in self.cells:
            print(f"[🖱️] NPC clicked cell ({row}, {col})")
            self.reveal(row, col)
        else:
            print(f"[⚠️] Invalid cell ({row}, {col})")

    def game_over(self):
        for cell in self.cells.values():
            if cell.is_mine:
                cell.button.config(text="M", bg="red")
        print("💥 Game Over: You clicked on a mine!")

# 👇 Ensure the GUI launches properly and app instance is available
def launch_gui():
    root = tk.Tk()
    app = MinesweeperGUI(root)
    root.app_instance = app
    root.mainloop()

if __name__ == "__main__":
    launch_gui()
