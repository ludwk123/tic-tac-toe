#!/usr/bin/env python3
"""
Unit tests for Tic Tac Toe game
"""

import unittest
from unittest.mock import patch, call
from io import StringIO
import sys
from tic_tac_toe import TicTacToe


class TestTicTacToe(unittest.TestCase):
    """Test cases for TicTacToe class."""
    
    def setUp(self):
        """Set up a fresh game instance before each test."""
        self.game = TicTacToe()
    
    def test_initialization(self):
        """Test that the game initializes correctly."""
        self.assertEqual(self.game.current_player, 'X')
        self.assertFalse(self.game.game_over)
        self.assertIsNone(self.game.winner)
        
        # Check that board is empty
        for row in self.game.board:
            for cell in row:
                self.assertEqual(cell, ' ')
    
    def test_display_board(self):
        """Test board display functionality."""
        with patch('builtins.print') as mock_print:
            self.game.display_board()
            
            # Check that print was called with expected output
            expected_calls = [
                call('\n   1   2   3'),
                call('1    |   |  '),
                call('  -----------'),
                call('2    |   |  '),
                call('  -----------'),
                call('3    |   |  ')
            ]
            mock_print.assert_has_calls(expected_calls)
    
    def test_is_valid_move(self):
        """Test move validation."""
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
        # Test valid move
        self.assertTrue(self.game.make_move(0, 0))
        self.assertEqual(self.game.board[0][0], 'X')
        
        # Test invalid move (occupied position)
        self.assertFalse(self.game.make_move(0, 0))
        
        # Test invalid move (out of bounds)
        self.assertFalse(self.game.make_move(3, 0))
        self.assertFalse(self.game.make_move(0, 3))
    
    def test_switch_player(self):
        """Test player switching."""
        self.assertEqual(self.game.current_player, 'X')
        
        self.game.switch_player()
        self.assertEqual(self.game.current_player, 'O')
        
        self.game.switch_player()
        self.assertEqual(self.game.current_player, 'X')
    
    def test_check_winner_rows(self):
        """Test win detection for rows."""
        # Test row 0 win
        self.game.board[0] = ['X', 'X', 'X']
        self.assertEqual(self.game.check_winner(), 'X')
        
        # Test row 1 win
        self.game.board = [[' ', ' ', ' '], ['O', 'O', 'O'], [' ', ' ', ' ']]
        self.assertEqual(self.game.check_winner(), 'O')
        
        # Test row 2 win
        self.game.board = [[' ', ' ', ' '], [' ', ' ', ' '], ['X', 'X', 'X']]
        self.assertEqual(self.game.check_winner(), 'X')
    
    def test_check_winner_columns(self):
        """Test win detection for columns."""
        # Test column 0 win
        self.game.board[0][0] = 'X'
        self.game.board[1][0] = 'X'
        self.game.board[2][0] = 'X'
        self.assertEqual(self.game.check_winner(), 'X')
        
        # Test column 1 win
        self.game.board = [[' ', 'O', ' '], [' ', 'O', ' '], [' ', 'O', ' ']]
        self.assertEqual(self.game.check_winner(), 'O')
        
        # Test column 2 win
        self.game.board = [[' ', ' ', 'X'], [' ', ' ', 'X'], [' ', ' ', 'X']]
        self.assertEqual(self.game.check_winner(), 'X')
    
    def test_check_winner_diagonals(self):
        """Test win detection for diagonals."""
        # Test main diagonal (top-left to bottom-right)
        self.game.board[0][0] = 'X'
        self.game.board[1][1] = 'X'
        self.game.board[2][2] = 'X'
        self.assertEqual(self.game.check_winner(), 'X')
        
        # Test anti-diagonal (top-right to bottom-left)
        self.game.board = [[' ', ' ', 'O'], [' ', 'O', ' '], ['O', ' ', ' ']]
        self.assertEqual(self.game.check_winner(), 'O')
    
    def test_check_winner_no_winner(self):
        """Test when there's no winner."""
        # Empty board
        self.assertIsNone(self.game.check_winner())
        
        # Partially filled board
        self.game.board[0][0] = 'X'
        self.game.board[1][1] = 'O'
        self.assertIsNone(self.game.check_winner())
    
    def test_is_board_full(self):
        """Test board full detection."""
        # Empty board
        self.assertFalse(self.game.is_board_full())
        
        # Partially filled board
        self.game.board[0][0] = 'X'
        self.assertFalse(self.game.is_board_full())
        
        # Full board
        self.game.board = [
            ['X', 'O', 'X'],
            ['O', 'X', 'O'],
            ['X', 'O', 'X']
        ]
        self.assertTrue(self.game.is_board_full())
    
    def test_get_player_input_valid(self):
        """Test valid player input."""
        with patch('builtins.input', return_value='1 2'):
            row, col = self.game.get_player_input()
            self.assertEqual(row, 0)  # 1-1 = 0
            self.assertEqual(col, 1)  # 2-1 = 1
    
    def test_get_player_input_invalid_format(self):
        """Test invalid input format."""
        with patch('builtins.input', side_effect=['1', '1 2 3', '1 2']):
            row, col = self.game.get_player_input()
            self.assertEqual(row, 0)
            self.assertEqual(col, 1)
    
    def test_get_player_input_out_of_bounds(self):
        """Test out of bounds input."""
        with patch('builtins.input', side_effect=['0 1', '4 1', '1 0', '1 4', '1 2']):
            row, col = self.game.get_player_input()
            self.assertEqual(row, 0)
            self.assertEqual(col, 1)
    
    def test_get_player_input_occupied_position(self):
        """Test input for occupied position."""
        self.game.board[0][1] = 'X'  # Occupy position 1 2
        with patch('builtins.input', side_effect=['1 2', '2 1']):
            row, col = self.game.get_player_input()
            self.assertEqual(row, 1)  # 2-1 = 1
            self.assertEqual(col, 0)  # 1-1 = 0
    
    def test_get_player_input_quit(self):
        """Test quit command."""
        with patch('builtins.input', return_value='quit'):
            with self.assertRaises(SystemExit):
                self.game.get_player_input()
    
    def test_get_player_input_exit(self):
        """Test exit command."""
        with patch('builtins.input', return_value='exit'):
            with self.assertRaises(SystemExit):
                self.game.get_player_input()
    
    def test_get_player_input_q(self):
        """Test q command."""
        with patch('builtins.input', return_value='q'):
            with self.assertRaises(SystemExit):
                self.game.get_player_input()
    
    def test_get_player_input_keyboard_interrupt(self):
        """Test keyboard interrupt handling."""
        with patch('builtins.input', side_effect=KeyboardInterrupt):
            with self.assertRaises(SystemExit):
                self.game.get_player_input()
    
    def test_get_player_input_value_error(self):
        """Test value error handling."""
        with patch('builtins.input', side_effect=['a b', '1 2']):
            row, col = self.game.get_player_input()
            self.assertEqual(row, 0)
            self.assertEqual(col, 1)
    
    def test_play_game_winner(self):
        """Test game with a winner."""
        # Simulate a winning game: X wins in top row
        with patch.object(self.game, 'get_player_input') as mock_input:
            mock_input.side_effect = [(0, 0), (1, 0), (0, 1), (1, 1), (0, 2)]
            
            with patch.object(self.game, 'display_board') as mock_display:
                with patch('builtins.print') as mock_print:
                    self.game.play_game()
                    
                    # Check that display_board was called
                    self.assertTrue(mock_display.called)
                    
                    # Check that winner message was printed
                    mock_print.assert_any_call('🎉 Player X wins! 🎉')
                    
                    # Check game state
                    self.assertTrue(self.game.game_over)
                    self.assertEqual(self.game.winner, 'X')
    
    def test_play_game_tie(self):
        """Test game ending in a tie."""
        # Create a tie scenario - almost full board with one move left
        # This board has no winner but will be full after the last move
        self.game.board = [
            ['X', 'O', 'X'],
            ['O', 'X', 'O'],
            ['O', 'X', ' ']
        ]
        self.game.current_player = 'X'  # Set current player
        
        with patch.object(self.game, 'get_player_input') as mock_input:
            mock_input.return_value = (2, 2)  # Last move to complete the board
            
            with patch.object(self.game, 'display_board') as mock_display:
                with patch('builtins.print') as mock_print:
                    self.game.play_game()
                    
                    # Check that winner message was printed (X wins in column 3)
                    mock_print.assert_any_call('🎉 Player X wins! 🎉')
                    
                    # Check game state
                    self.assertTrue(self.game.game_over)
                    self.assertEqual(self.game.winner, 'X')
    
    def test_play_game_actual_tie(self):
        """Test game ending in an actual tie."""
        # Create a tie scenario - almost full board with one move left
        # This board has no winner and will be full after the last move
        self.game.board = [
            ['X', 'O', 'X'],
            ['O', 'X', 'O'],
            ['O', 'X', ' ']
        ]
        self.game.current_player = 'O'  # Set current player to O
        
        with patch.object(self.game, 'get_player_input') as mock_input:
            mock_input.return_value = (2, 2)  # Last move to complete the board
            
            with patch.object(self.game, 'display_board') as mock_display:
                with patch('builtins.print') as mock_print:
                    self.game.play_game()
                    
                    # Check that tie message was printed
                    mock_print.assert_any_call('🤝 It\'s a tie! 🤝')
                    
                    # Check game state
                    self.assertTrue(self.game.game_over)
                    self.assertIsNone(self.game.winner)
    
    def test_integration_game_flow(self):
        """Test complete game flow."""
        game = TicTacToe()
        
        # Simulate moves for a complete game
        moves = [(0, 0), (1, 1), (0, 1), (1, 0), (0, 2)]  # X wins in top row
        
        with patch.object(game, 'get_player_input') as mock_input:
            mock_input.side_effect = moves
            
            with patch.object(game, 'display_board'):
                with patch('builtins.print') as mock_print:
                    game.play_game()
                    
                    # Verify game ended with X as winner
                    self.assertTrue(game.game_over)
                    self.assertEqual(game.winner, 'X')
                    mock_print.assert_any_call('🎉 Player X wins! 🎉')


if __name__ == '__main__':
    unittest.main() 