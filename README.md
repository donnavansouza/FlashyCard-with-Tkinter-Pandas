# FlashyCard with Tkinter & Pandas

## Overview
This project is a simple flashcard application to help users learn French vocabulary. The application displays a French word on a card and flips to reveal the English translation after a set time interval. Users can mark words they have learned, which will be saved for future sessions.

## Features
- **Flashcards**: Randomly displays French words and their English translations.
- **Auto-Flip**: Cards automatically flip after 3 seconds to show the translation.
- **Progress Tracking**: Users can mark words as known, and the app will save their progress.
- **Persistent Data**: Progress is saved between sessions using CSV files.

## Requirements
- Python 3.x
- **pandas**
- **tkinter**

## Installation
1. **Clone the repository**:
   ```sh
   git clone https://github.com/your-username/flash-card-app.git
   cd flash-card-app
   ```

2. **Install the required packages**:
   ```sh
   pip install pandas
   ```

3. **Ensure the directory structure is as follows**:
   ```
   flash-card-app/
   ├── data/
   │   ├── 5000_wordlist_french.csv
   │   └── words_to_learn.csv (optional, will be created if not present)
   ├── images/
   │   ├── card_front.png
   │   ├── card_back.png
   │   ├── right.png
   │   └── wrong.png
   └── main.py
   ```

## Usage
1. **Run the application**:
   ```sh
   python main.py
   ```

2. **Interacting with the application**:
   - The app will display a French word on a card.
   - After 3 seconds, the card will flip to show the English translation.
   - Click the right button if you know the word (it will be removed from the learning list).
   - Click the wrong button to see the next card.

## Contributions
Contributions are welcome! Please open an issue or submit a pull request for any features, enhancements, or bugs.

## Acknowledgments
- This application was made following the 100 Days of Code: The Complete Python Pro Bootcamp with instructor Dr. Angela Yu.
- The csv with 5000 French words and it's translations to English can be found in https://www.reddit.com/r/learnfrench/comments/grnome/i_generated_a_csv_xlsx_version_for_anki/


## License
This project is licensed under the MIT License. See the LICENSE file for details.