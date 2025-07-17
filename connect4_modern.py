import tkinter as tk
from tkinter import messagebox
import numpy as np
import math

class Connect4Game:
    def __init__(self, root):
        self.root = root
        self.root.title("Connect 4 - Modern Edition")
        self.root.configure(bg='#1a1a2e')
        
        # Game constants from original repository
        self.ROW_COUNT = 6
        self.COLUMN_COUNT = 7
        
        # Game state
        self.board = self.create_board()
        self.game_over = False
        self.turn = 0  # 0 for Player 1 (Red), 1 for Player 2 (Yellow)
        
        # Colors (using original repository colors)
        self.colors = {
            'blue': '#003f88',      # Board background
            'red': '#d00000',       # Player 1
            'yellow': '#ffd60a',    # Player 2
            'empty': '#2c3e50',     # Empty slots
            'hover': '#34495e',     # Hover effect
            'text': '#ecf0f1'       # Text color
        }
        
        self.setup_ui()
        
    def create_board(self):
        """Initialize the game board (from original repository)"""
        return np.zeros((self.ROW_COUNT, self.COLUMN_COUNT))
    
    def drop_piece(self, board, row, col, piece):
        """Drop a piece on the board (from original repository)"""
        board[row][col] = piece
    
    def is_valid_location(self, board, col):
        """Check if the top spot in a column is open (from original repository)"""
        return board[self.ROW_COUNT - 1][col] == 0
    
    def get_next_open_row(self, board, col):
        """Find the next open row available (from original repository)"""
        for r in range(self.ROW_COUNT):
            if board[r][col] == 0:
                return r
        return None
    
    def winning_move(self, board, piece):
        """Check for winning moves (from original repository)"""
        # Check horizontal locations for win
        for c in range(self.COLUMN_COUNT-3):
            for r in range(self.ROW_COUNT):
                if (board[r][c] == piece and board[r][c+1] == piece and 
                    board[r][c+2] == piece and board[r][c+3] == piece):
                    return True

        # Check vertical locations for win
        for r in range(self.ROW_COUNT-3):
            for c in range(self.COLUMN_COUNT):
                if (board[r][c] == piece and board[r+1][c] == piece and 
                    board[r+2][c] == piece and board[r+3][c] == piece):
                    return True

        # Check positive sloped diagonals
        for r in range(self.ROW_COUNT-3):
            for c in range(self.COLUMN_COUNT-3):
                if (board[r][c] == piece and board[r+1][c+1] == piece and 
                    board[r+2][c+2] == piece and board[r+3][c+3] == piece):
                    return True

        # Check negative sloped diagonals
        for r in range(3, self.ROW_COUNT):
            for c in range(self.COLUMN_COUNT-3):
                if (board[r][c] == piece and board[r-1][c+1] == piece and 
                    board[r-2][c+2] == piece and board[r-3][c+3] == piece):
                    return True
        
        return False
    
    def is_board_full(self):
        """Check if the board is full (draw condition)"""
        return all(self.board[self.ROW_COUNT-1][col] != 0 for col in range(self.COLUMN_COUNT))
    
    def setup_ui(self):
        """Create the modern UI"""
        # Main container
        main_frame = tk.Frame(self.root, bg='#1a1a2e', padx=15, pady=15)
        main_frame.pack(expand=True, fill='both')
        
        # Header
        header_frame = tk.Frame(main_frame, bg='#1a1a2e')
        header_frame.pack(fill='x', pady=(0, 15))
        
        # Title
        title_label = tk.Label(
            header_frame,
            text="CONNECT 4",
            font=('Arial', 24, 'bold'),
            fg='#ecf0f1',
            bg='#1a1a2e'
        )
        title_label.pack()
        
        # Subtitle
        subtitle_label = tk.Label(
            header_frame,
            text="Modern Edition",
            font=('Arial', 10),
            fg='#bdc3c7',
            bg='#1a1a2e'
        )
        subtitle_label.pack()
        
        # Game info frame
        info_frame = tk.Frame(main_frame, bg='#1a1a2e')
        info_frame.pack(pady=(15, 20))
        
        # Current player indicator
        self.player_label = tk.Label(
            info_frame,
            text="🎮 Player 1's Turn (Red)",
            font=('Arial', 14, 'bold'),
            fg='#e74c3c',
            bg='#1a1a2e'
        )
        self.player_label.pack()
        
        # Game board frame
        board_frame = tk.Frame(main_frame, bg='#16213e', relief='raised', bd=3)
        board_frame.pack()
        
        # Create the game board - FIXED: Much smaller buttons to fit properly
        self.buttons = []
        for row in range(self.ROW_COUNT):
            button_row = []
            for col in range(self.COLUMN_COUNT):
                button = tk.Button(
                    board_frame,
                    width=4,  # Much smaller
                    height=2,  # Much smaller
                    bg=self.colors['empty'],
                    relief='raised',
                    bd=1,     # Thinner border
                    command=lambda c=col: self.make_move(c)
                )
                button.grid(row=row, column=col, padx=1, pady=1)  # Minimal padding
                
                # Add hover effects
                button.bind('<Enter>', lambda e, b=button: self.on_hover(b, True))
                button.bind('<Leave>', lambda e, b=button: self.on_hover(b, False))
                
                button_row.append(button)
            self.buttons.append(button_row)
        
        # Control buttons frame
        control_frame = tk.Frame(main_frame, bg='#1a1a2e')
        control_frame.pack(pady=(20, 0))
        
        # Reset button
        reset_button = tk.Button(
            control_frame,
            text="🔄 New Game",
            font=('Arial', 12, 'bold'),
            bg='#3498db',
            fg='white',
            relief='raised',
            bd=2,
            padx=15,
            pady=5,
            command=self.reset_game
        )
        reset_button.pack(side='left', padx=(0, 15))
        
        # Instructions
        instructions = tk.Label(
            control_frame,
            text="Click any column to drop your piece",
            font=('Arial', 10),
            fg='#bdc3c7',
            bg='#1a1a2e'
        )
        instructions.pack(side='left')
        
    def on_hover(self, button, entering):
        """Handle hover effects"""
        if entering and not self.game_over:
            button.configure(bg=self.colors['hover'])
        else:
            button.configure(bg=self.colors['empty'])
    
    def make_move(self, col):
        """Make a move (using original repository logic)"""
        if self.game_over:
            return
            
        # Check if the move is valid
        if not self.is_valid_location(self.board, col):
            return  # Column is full
            
        # Get the row where the piece will be placed
        row = self.get_next_open_row(self.board, col)
        if row is None:
            return
            
        # Determine which player's piece to place
        piece = 1 if self.turn == 0 else 2
        
        # Place the piece (using original repository function)
        self.drop_piece(self.board, row, col, piece)
        
        # Update the UI - FIXED: Use correct row indexing
        color = self.colors['red'] if piece == 1 else self.colors['yellow']
        # Note: We need to flip the row index because UI shows bottom row as 0
        ui_row = self.ROW_COUNT - 1 - row
        self.buttons[ui_row][col].configure(bg=color)
        
        # Check for win (using original repository function)
        if self.winning_move(self.board, piece):
            self.game_over = True
            winner = "Player 1 (Red)" if piece == 1 else "Player 2 (Yellow)"
            messagebox.showinfo("🎉 Game Over!", f"{winner} wins!")
            return
            
        # Check for draw
        if self.is_board_full():
            self.game_over = True
            messagebox.showinfo("🤝 Game Over!", "It's a draw!")
            return
            
        # Switch turns
        self.turn = (self.turn + 1) % 2
        
        # Update player indicator
        if self.turn == 0:
            self.player_label.configure(text="🎮 Player 1's Turn (Red)", fg='#e74c3c')
        else:
            self.player_label.configure(text="🎮 Player 2's Turn (Yellow)", fg='#f1c40f')
    
    def reset_game(self):
        """Reset the game to initial state"""
        # Reset board
        self.board = self.create_board()
        
        # Reset buttons
        for row in range(self.ROW_COUNT):
            for col in range(self.COLUMN_COUNT):
                self.buttons[row][col].configure(bg=self.colors['empty'])
        
        # Reset game state
        self.game_over = False
        self.turn = 0
        self.player_label.configure(text="🎮 Player 1's Turn (Red)", fg='#e74c3c')

def main():
    root = tk.Tk()
    root.geometry("500x600")  # Much smaller window
    root.resizable(False, False)
    
    # Center the window
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (500 // 2)
    y = (root.winfo_screenheight() // 2) - (600 // 2)
    root.geometry(f"500x600+{x}+{y}")
    
    game = Connect4Game(root)
    root.mainloop()

if __name__ == "__main__":
    main() 