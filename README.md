# MINESWEEPER-LLM

A smart Minesweeper game that uses OpenAI's GPT model to play the game based on visual understanding.

-----------

## FEATURES
- Interactive Minesweeper game with GUI
- Takes screenshot of the game grid
- Extracts text using OCR (Tesseract)
- Uses GPT (LLM) to analyze the board and decide next move
- Automatically clicks the cell

## HOW TO RUN

1. Clone the repository:
git clone https://github.com/sampath-009/Minesweeper-LLM.git
cd Minesweeper-LLM

2. Install requirements:
pip install -r requirements.txt

3. Add your OpenAI API key:
Create a file named .env
Add this line inside it:
OPENAI_API_KEY=your-api-key-here

4. Run the game GUI:
python gui.py

5. Run the LLM agent:
python main.py


## PROJECT STRUCTURE

Minesweeper-LLM/
├── gui.py            # GUI of the game
├── main.py           # LLM-based gameplay
├── vision/           # OCR + screen capture
├── llm/              # Prompt + GPT logic
├── utils/            # Text parsing
├── requirements.txt
└── README.md

## LICENSE

- OpenAI for ChatGPT API
- Pytesseract for OCR
- Tkinter for GUI

