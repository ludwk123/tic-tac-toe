#!/usr/bin/env python3
"""
Tic Tac Toe Game
A simple command-line tic-tac-toe game for two players.
"""

import sys
from typing import List, Optional, Tuple


class TicTacToe:
    """A tic-tac-toe game implementation."""
    
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.game_over = False
        self.winner = None
    
    def display_board(self) -> None:
        """Display the current game board."""
        print("\n   1   2   3")
        for i, row in enumerate(self.board):
            print(f"{i + 1}  {row[0]} | {row[1]} | {row[2]}")
            if i < 2:
                print("  -----------")
        print()
    
    def is_valid_move(self, row: int, col: int) -> bool:
        """Check if a move is valid."""
        return (0 <= row < 3 and 
                0 <= col < 3 and 
                self.board[row][col] == ' ')
    
    def make_move(self, row: int, col: int) -> bool:
        """Make a move on the board."""
        if self.is_valid_move(row, col):
            self.board[row][col] = self.current_player
            return True
        return False
    
    def check_winner(self) -> Optional[str]:
        """Check if there's a winner."""
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return row[0]
        
        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return self.board[0][col]
        
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]
        
        return None
    
    def is_board_full(self) -> bool:
        """Check if the board is full."""
        return all(cell != ' ' for row in self.board for cell in row)
    
    def switch_player(self) -> None:
        """Switch to the other player."""
        self.current_player = 'O' if self.current_player == 'X' else 'X'
    
    def get_player_input(self) -> Tuple[int, int]:
        """Get valid input from the current player."""
        while True:
            try:
                move = input(f"Player {self.current_player}, enter your move (row col): ").strip()
                
                if move.lower() in ['quit', 'exit', 'q']:
                    print("Thanks for playing!")
                    sys.exit(0)
                
                parts = move.split()
                if len(parts) != 2:
                    print("Please enter two numbers separated by a space (row col)")
                    continue
                
                row, col = int(parts[0]) - 1, int(parts[1]) - 1
                
                if not (0 <= row < 3 and 0 <= col < 3):
                    print("Please enter numbers between 1 and 3")
                    continue
                
                if not self.is_valid_move(row, col):
                    print("That position is already taken! Choose another.")
                    continue
                
                return row, col
                
            except ValueError:
                print("Please enter valid numbers")
            except KeyboardInterrupt:
                print("\nThanks for playing!")
                sys.exit(0)
    
    def play_game(self) -> None:
        """Main game loop."""
        print("🎮 Welcome to Tic Tac Toe! 🎮")
        print("Enter moves as 'row col' (e.g., '1 2' for row 1, column 2)")
        print("Type 'quit' to exit the game")
        
        while not self.game_over:
            self.display_board()
            
            # Get player move
            row, col = self.get_player_input()
            
            # Make the move
            if self.make_move(row, col):
                # Check for winner
                winner = self.check_winner()
                if winner:
                    self.display_board()
                    print(f"🎉 Player {winner} wins! 🎉")
                    self.game_over = True
                    self.winner = winner
                elif self.is_board_full():
                    self.display_board()
                    print("🤝 It's a tie! 🤝")
                    self.game_over = True
                else:
                    self.switch_player()
            else:
                print("Invalid move! Try again.")


def main():
    """Main function to run the game."""
    while True:
        game = TicTacToe()
        game.play_game()
        
        # Ask if players want to play again
        while True:
            try:
                play_again = input("\nWould you like to play again? (y/n): ").strip().lower()
                if play_again in ['y', 'yes']:
                    break
                elif play_again in ['n', 'no']:
                    print("Thanks for playing! Goodbye! 👋")
                    return
                else:
                    print("Please enter 'y' for yes or 'n' for no")
            except KeyboardInterrupt:
                print("\nThanks for playing! Goodbye! 👋")
                return


if __name__ == "__main__":
    main()
