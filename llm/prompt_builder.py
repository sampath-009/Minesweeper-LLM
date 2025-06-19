# llm/prompt_builder.py

def clean_ocr_output(raw_text):
    """
    Cleans up OCR noise and converts it into a grid of tokens (2D list).
    Treats unknown characters as 'X'.
    """
    lines = raw_text.strip().splitlines()
    grid = []

    for line in lines:
        row = []
        for ch in line.strip().split():
            if ch.isdigit():
                row.append(ch)
            elif ch in ["M", "*", "-", ".", "–"]:
                row.append("X")  # Treat as unrevealed tile or noise
        if row:
            grid.append(row)

    return grid


def grid_to_prompt(grid):
    """
    Converts a 2D list grid into a prompt string for the LLM.
    """
    formatted = "\n".join(" ".join(row) for row in grid)
    prompt = f"""
You are an expert Minesweeper player. Here's the current game board:

{formatted}

Each cell is either a number (0-8), or 'X' for unrevealed tiles.
Based on standard Minesweeper logic, what cell should be clicked next and why?

Reply in this format:
(row, col) — Reason
"""
    return prompt.strip()
