# Connect 4 - Modern Edition

A beautiful, modern, and fully functional Connect 4 game built with Python and Tkinter.

## 🎮 Features
- **Modern UI**: Clean, dark theme with professional colors
- **Responsive Board**: Properly sized, no overlapping, fits all screens
- **Two Players**: Red and Yellow pieces
- **Win Detection**: Horizontal, vertical, and diagonal
- **Draw Detection**: Handles tie games
- **Turn Indicator**: Shows whose turn it is
- **Hover Effects**: Visual feedback on columns
- **Reset Button**: Instantly start a new game
- **No External Dependencies**: Only requires Python 3 and NumPy

## 🖥️ Screenshot

![Connect 4 Modern UI Screenshot](screenshot.png) <!-- Add a screenshot if you wish -->

## 🚀 How to Run

1. **Install Python 3** (if not already installed)
2. **Install NumPy** (if not already installed):
   ```bash
   pip3 install numpy
   ```
3. **Run the game:**
   ```bash
   python3 connect4_modern.py
   ```

## 🕹️ How to Play
- Players take turns clicking a column to drop their piece
- The piece will fall to the lowest available slot in that column
- The first player to connect four pieces in a row (horizontally, vertically, or diagonally) wins
- If the board fills up with no winner, it's a draw
- Click **New Game** to reset the board at any time

## 📋 Requirements
- Python 3.x
- NumPy
- Tkinter (comes with most Python installations)

## 🏗️ Technical Details
- **Frontend**: Tkinter
- **Backend**: NumPy for board logic
- **Design**: Object-oriented, clean, and maintainable

## ✨ Credits
- UI and logic by [your name or organization]

Enjoy playing Connect 4! 