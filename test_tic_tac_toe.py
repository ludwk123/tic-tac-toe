#!/usr/bin/env python3
"""
Unit tests for Tic Tac Toe Game
Tests all methods and edge cases of the TicTacToe class.
"""

import unittest
from unittest.mock import patch, call
from io import StringIO
import sys
from tic_tac_toe import TicTacToe


class TestTicTacToe(unittest.TestCase):
    """Test cases for the TicTacToe class."""
    
    def setUp(self):
        """Set up a fresh game instance before each test."""
        self.game = TicTacToe()
    
    def test_initialization(self):
        """Test that the game initializes correctly."""
        self.assertEqual(self.game.board, [[' ' for _ in range(3)] for _ in range(3)])
        self.assertEqual(self.game.current_player, 'X')
        self.assertFalse(self.game.game_over)
        self.assertIsNone(self.game.winner)
    
    def test_is_valid_move(self):
        """Test valid and invalid moves."""
        # Test valid moves
        self.assertTrue(self.game.is_valid_move(0, 0))
        self.assertTrue(self.game.is_valid_move(1, 1))
        self.assertTrue(self.game.is_valid_move(2, 2))
        
        # Test invalid moves (out of bounds)
        self.assertFalse(self.game.is_valid_move(-1, 0))
        self.assertFalse(self.game.is_valid_move(0, -1))
        self.assertFalse(self.game.is_valid_move(3, 0))
        self.assertFalse(self.game.is_valid_move(0, 3))
        
        # Test invalid moves (occupied positions)
        self.game.board[0][0] = 'X'
        self.assertFalse(self.game.is_valid_move(0, 0))
        
        self.game.board[1][1] = 'O'
        self.assertFalse(self.game.is_valid_move(1, 1))
    
    def test_make_move(self):
        """Test making moves on the board."""
        # Test successful moves
        self.assertTrue(self.game.make_move(0, 0))
        self.assertEqual(self.game.board[0][0], 'X')
        
        # Switch player and make another move
        self.game.switch_player()
        self.assertTrue(self.game.make_move(1, 1))
        self.assertEqual(self.game.board[1][1], 'O')
        
        # Test invalid moves
        self.assertFalse(self.game.make_move(0, 0))  # Already occupied
        self.assertFalse(self.game.make_move(-1, 0))  # Out of bounds
        self.assertFalse(self.game.make_move(0, 3))   # Out of bounds
    
    def test_switch_player(self):
        """Test player switching."""
        self.assertEqual(self.game.current_player, 'X')
        
        self.game.switch_player()
        self.assertEqual(self.game.current_player, 'O')
        
        self.game.switch_player()
        self.assertEqual(self.game.current_player, 'X')
    
    def test_check_winner_rows(self):
        """Test winning conditions in rows."""
        # Test first row win
        self.game.board = [
            ['X', 'X', 'X'],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        self.assertEqual(self.game.check_winner(), 'X')
        
        # Test second row win
        self.game.board = [
            [' ', ' ', ' '],
            ['O', 'O', 'O'],
            [' ', ' ', ' ']
        ]
        self.assertEqual(self.game.check_winner(), 'O')
        
        # Test third row win
        self.game.board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            ['X', 'X', 'X']
        ]
        self.assertEqual(self.game.check_winner(), 'X')
    
    def test_check_winner_columns(self):
        """Test winning conditions in columns."""
        # Test first column win
        self.game.board = [
            ['X', ' ', ' '],
            ['X', ' ', ' '],
            ['X', ' ', ' ']
        ]
        self.assertEqual(self.game.check_winner(), 'X')
        
        # Test second column win
        self.game.board = [
            [' ', 'O', ' '],
            [' ', 'O', ' '],
            [' ', 'O', ' ']
        ]
        self.assertEqual(self.game.check_winner(), 'O')
        
        # Test third column win
        self.game.board = [
            [' ', ' ', 'X'],
            [' ', ' ', 'X'],
            [' ', ' ', 'X']
        ]
        self.assertEqual(self.game.check_winner(), 'X')
    
    def test_check_winner_diagonals(self):
        """Test winning conditions in diagonals."""
        # Test main diagonal win
        self.game.board = [
            ['X', ' ', ' '],
            [' ', 'X', ' '],
            [' ', ' ', 'X']
        ]
        self.assertEqual(self.game.check_winner(), 'X')
        
        # Test anti-diagonal win
        self.game.board = [
            [' ', ' ', 'O'],
            [' ', 'O', ' '],
            ['O', ' ', ' ']
        ]
        self.assertEqual(self.game.check_winner(), 'O')
    
    def test_check_winner_no_winner(self):
        """Test when there's no winner."""
        # Empty board
        self.assertIsNone(self.game.check_winner())
        
        # Partially filled board
        self.game.board = [
            ['X', 'O', ' '],
            ['O', 'X', ' '],
            [' ', ' ', ' ']
        ]
        self.assertIsNone(self.game.check_winner())
        
        # Full board with no winner
        self.game.board = [
            ['X', 'O', 'X'],
            ['O', 'X', 'O'],
            ['O', 'X', 'O']
        ]
        self.assertIsNone(self.game.check_winner())
    
    def test_is_board_full(self):
        """Test board full detection."""
        # Empty board
        self.assertFalse(self.game.is_board_full())
        
        # Partially filled board
        self.game.board = [
            ['X', 'O', 'X'],
            ['O', 'X', ' '],
            [' ', ' ', ' ']
        ]
        self.assertFalse(self.game.is_board_full())
        
        # Full board
        self.game.board = [
            ['X', 'O', 'X'],
            ['O', 'X', 'O'],
            ['O', 'X', 'O']
        ]
        self.assertTrue(self.game.is_board_full())
    
    def test_display_board(self):
        """Test board display output."""
        # Set up a specific board state
        self.game.board = [
            ['X', 'O', 'X'],
            ['O', 'X', ' '],
            [' ', ' ', 'O']
        ]
        
        # Capture the output
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.game.display_board()
            output = fake_out.getvalue()
            
            # Check that the output contains expected elements
            self.assertIn('1   2   3', output)
            self.assertIn('1  X | O | X', output)
            self.assertIn('2  O | X |', output)
            self.assertIn('3    |   | O', output)
            self.assertIn('-----------', output)
    
    @patch('builtins.input')
    def test_get_player_input_valid(self, mock_input):
        """Test getting valid player input."""
        mock_input.return_value = "2 3"
        
        row, col = self.game.get_player_input()
        
        self.assertEqual(row, 1)  # 2-1 = 1
        self.assertEqual(col, 2)  # 3-1 = 2
        mock_input.assert_called_once()
    
    @patch('builtins.input')
    def test_get_player_input_invalid_format(self, mock_input):
        """Test handling of invalid input format."""
        mock_input.side_effect = ["1", "1 2 3", "2 3"]
        
        row, col = self.game.get_player_input()
        
        self.assertEqual(row, 1)
        self.assertEqual(col, 2)
        self.assertEqual(mock_input.call_count, 3)
    
    @patch('builtins.input')
    def test_get_player_input_out_of_bounds(self, mock_input):
        """Test handling of out-of-bounds input."""
        mock_input.side_effect = ["0 1", "4 2", "2 3"]
        
        row, col = self.game.get_player_input()
        
        self.assertEqual(row, 1)
        self.assertEqual(col, 2)
        self.assertEqual(mock_input.call_count, 3)
    
    @patch('builtins.input')
    def test_get_player_input_occupied_position(self, mock_input):
        """Test handling of occupied position input."""
        self.game.board[1][1] = 'X'  # Occupy position (2,2)
        mock_input.side_effect = ["2 2", "1 1"]
        
        row, col = self.game.get_player_input()
        
        self.assertEqual(row, 0)
        self.assertEqual(col, 0)
        self.assertEqual(mock_input.call_count, 2)
    
    @patch('builtins.input')
    def test_get_player_input_quit(self, mock_input):
        """Test quitting the game."""
        mock_input.return_value = "quit"
        
        with self.assertRaises(SystemExit):
            self.game.get_player_input()
    
    @patch('builtins.input')
    def test_get_player_input_exit(self, mock_input):
        """Test exiting the game."""
        mock_input.return_value = "exit"
        
        with self.assertRaises(SystemExit):
            self.game.get_player_input()
    
    @patch('builtins.input')
    def test_get_player_input_keyboard_interrupt(self, mock_input):
        """Test handling keyboard interrupt."""
        mock_input.side_effect = KeyboardInterrupt()
        
        with self.assertRaises(SystemExit):
            self.game.get_player_input()
    
    def test_complete_game_flow(self):
        """Test a complete game flow."""
        # Simulate a game where X wins in the first row
        moves = [(0, 0), (1, 0), (0, 1), (1, 1), (0, 2)]  # X wins
        
        for i, (row, col) in enumerate(moves):
            # Make the move
            self.assertTrue(self.game.make_move(row, col))
            
            # Check for winner
            winner = self.game.check_winner()
            if winner:
                self.assertEqual(winner, 'X')
                self.game.game_over = True
                self.game.winner = winner
                break
            
            # Check for tie
            if self.game.is_board_full():
                self.game.game_over = True
                break
            
            # Switch player if game continues
            if not self.game.game_over:
                self.game.switch_player()
        
        # Verify final state
        self.assertTrue(self.game.game_over)
        self.assertEqual(self.game.winner, 'X')
        self.assertEqual(self.game.board[0], ['X', 'X', 'X'])
    
    def test_tie_game(self):
        """Test a tie game scenario."""
        # Set up a tie game
        self.game.board = [
            ['X', 'O', 'X'],
            ['O', 'X', 'O'],
            ['O', 'X', 'O']
        ]
        
        # Check that there's no winner
        self.assertIsNone(self.game.check_winner())
        
        # Check that board is full
        self.assertTrue(self.game.is_board_full())
        
        # Verify it's a tie
        self.assertFalse(self.game.game_over)  # Game should continue until checked


if __name__ == '__main__':
    unittest.main() 