# utils/response_parser.py

import re

def extract_coordinates(response_text):
    """
    Extracts (row, col) from LLM response like:
    "(3, 4) — Reason text"
    """
    match = re.search(r"\((\d+),\s*(\d+)\)", response_text)
    if match:
        row, col = int(match.group(1)), int(match.group(2))
        return row, col
    return None
