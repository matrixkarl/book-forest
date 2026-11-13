# Book Forest 🌲

Book Forest is a simple Python application designed to help readers collect and organize unfamiliar words they encounter while reading.

## Inspiration

The idea for Book Forest came from a problem I frequently encountered while reading: discovering unfamiliar words and opening multiple browser tabs on my phone to look up their definitions.

Over time, I found myself hoarding tabs, so I wanted to create a simple way to store words and their definitions in one place.

I envisioned the application as a forest filled with words, which inspired the name **Book Forest**.

## Features

- Organize vocabulary words by book title.
- Add unfamiliar words and their definitions.
- Store personal definitions or definitions found online.
- Save vocabulary using a JSON file.
- Load previously saved words when the program runs again.
- Display the collected vocabulary as a Python dictionary.

## Technologies Used

- Python
- JSON for data storage
- `pathlib` for working with file paths

## How to Run

1. Download `book_forest.py`.
2. Open a terminal in the folder containing the file.
3. Run the following command:

   `python book_forest.py`

4. Follow the prompts to enter a book title, vocabulary words, and definitions.

The application allows users to continue adding words to the same book or create entries for additional books. When the user chooses to exit, the program displays the collected vocabulary.
