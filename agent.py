import tkinter as tk
from utils.response_parser import extract_coordinates
from vision.capture import capture_window
from vision.preprocess import preprocess
from vision.ocr import extract_grid_text
from llm.chatgpt import query_chatgpt
from llm.prompt_builder import clean_ocr_output, grid_to_prompt

def run_ai_agent_once():
    print(" Capturing screen...")
    img = capture_window(save=True)

    print(" Preprocessing image...")
    processed = preprocess(img)

    print(" Running OCR...")
    result = extract_grid_text(processed)
    print(" OCR Result:\n", result)

    grid = clean_ocr_output(result)
    print("\n Structured Grid:")
    for row in grid:
        print(" ".join(row))

    prompt = grid_to_prompt(grid)
    print("\n LLM Prompt:\n", prompt)

    print("\n Querying LLM...")
    response = query_chatgpt(prompt)
    print("\n LLM Response:\n", response)

    coords = extract_coordinates(response)
    root = tk._default_root
    app = getattr(root, "app_instance", None)

    if app and coords:
        row, col = coords
        print(f"\n NPC will click on cell ({row}, {col})")
        app.click_cell(row, col)
    else:
        print("\n Could not extract coordinates or access app.")
