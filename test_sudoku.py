import unittest
from sudoku_solver import Sudoku, InvalidSudokuException

class TestSudoku(unittest.TestCase):
	
	@classmethod
	def setUpClass(self):
		self.easy_grid = [
			[   8, None,    2, None,    5, None,    7, None,    1],
			[None, None,    7, None,    8,    2,    4,    6, None],
			[None,    1, None,    9, None, None, None, None, None],
			[   6, None, None, None, None,    1,    8,    3,    2],
			[   5, None, None, None, None, None, None, None,    9], 
			[   1,    8,    4,    3, None, None, None, None,    6],
			[None, None, None, None, None,    4, None,    2, None], 
			[None,    9,    5,    6,    1, None,    3, None, None], 
			[   3, None,    8, None,    9, None,    6, None,    7] 
			]
		self.easy_grid_puzzle = Sudoku(self.easy_grid)
		
		self.solved_grid = [
			  [1, 2, 3, 4, 5, 6, 7, 8, 9],
			  [4, 5, 6, 7, 8, 9, 1, 2, 3],
			  [7, 8, 9, 1, 2, 3, 4, 5, 6],
			  [2, 3, 4, 5, 6, 7, 8, 9, 1],
			  [5, 6, 7, 8, 9, 1, 2, 3, 4],
			  [8, 9, 1, 2, 3, 4, 5, 6, 7],
			  [3, 4, 5, 6, 7, 8, 9, 1, 2],
			  [6, 7, 8, 9, 1, 2, 3, 4, 5],
			  [9, 1, 2, 3, 4, 5, 6, 7, 8]
			  ]
		self.solved_puzzle = Sudoku(self.solved_grid)

		self.unsolved_grid = [
			  [1, 2, 3, 4, 5, 6, 7, 8, 9],
			  [4, None, 6, 7, 8, 9, 1, 2, 3],
			  [7, 8, 9, 1, None, 3, 4, 5, 6],
			  [2, 3, 4, 5, 6, 7, 8, 9, 1],
			  [5, 6, 7, 8, 9, 1, 2, 3, 4],
			  [8, 9, 1, 2, 3, 4, 5, 6, 7],
			  [3, 4, 5, 6, 7, 8, 9, 1, 2],
			  [6, 7, 8, 9, 1, 2, 3, 4, 5],
			  [9, 1, 2, 3, 4, 5, 6, 7, 8]
			]
		self.unsolved_puzzle = Sudoku(self.unsolved_grid)
		
	def test_initialize_solved_grid(self):
		puzzle = Sudoku(self.solved_grid)
		self.assertIsInstance(puzzle, Sudoku)
		
	def test_get_empty_cell_indices(self):
		received_empty_cell_indices = self.unsolved_puzzle.find_empty_cell_indices()
		expected_empty_cell_indices = [(1, 1), (2, 4)]
		self.assertEqual(received_empty_cell_indices, expected_empty_cell_indices)
		
	def test_invalid_grid_raises_exception(self):
		bad_grid = [
			[1, 2, 3, 4, 5, 6, 7, 8, 9],
			[4, 5, 6, 7, 8, 9, 1, 2, 3],
			[7, 8, 9, 1, 2, 3, 4, 5, 6],
			[2, 3, 4, 5, 6, 7, 8, 9, 1],
			[5, 6, 7, 8, 9, 1, 2, 3, 4],
			[8, 9, 1, 2, 3, 4, 5, 6, 7],
			[3, 4, 5, 6, 7, 8, 9, 1, 2],
			[6, 7, 8, 9, 1, 2, 3, 4, 5],
			[9, 1, 2, 3, 4, 5, 6, 2, 8]
			]
		self.assertRaises(InvalidSudokuException, Sudoku, bad_grid)
		
	def test_invalid_grid_with_nones(self):
		grid_with_nones = [
	 		[1, 2, 3, 4, 5, 6, 7, 8, 9],
			[4, 5, 6, 7, 8, 9, 1, 2, 3],
			[7, 8, 9, 1, 2, 3, 4, 5, 6],
			[2, 3, 4, 5, 6, 7, 8, 9, 1],
			[5, 6, 7, 8, 9, 1, 2, 3, 4],
			[8, 9, 1, 2, 3, 4, 5, 6, 7],
			[3, 4, 5, 6, 7, 8, 9, 1, 2],
			[6, 7, 8, 9, 1, 2, 3, 4, 5],
			[9, 1, 2, 3, 4, 5, 2, None, 8],
			]
		self.assertRaises(InvalidSudokuException, Sudoku, grid_with_nones)
		
	def test_solve_very_easy(self):
		very_easy_grid = [
			  [1, 2,    3, 4,    5, 6, 7, 8, 9],
			  [4, None, 6, 7,    8, 9, 1, 2, 3],
			  [7, 8,    9, 1, None, 3, 4, 5, 6],
			  [2, 3,    4, 5,    6, 7, 8, 9, 1],
			  [5, 6,    7, 8,    9, 1, 2, 3, 4],
			  [8, 9,    1, 2,    3, 4, 5, 6, 7],
			  [3, 4,    5, 6,    7, 8, 9, 1, 2],
			  [6, 7,    8, 9,    1, 2, 3, 4, 5],
			  [9, 1,    2, 3,    4, 5, 6, 7, 8]
			]
		puzzle = Sudoku(very_easy_grid)
		returned_solution = puzzle.solve()
		expected_solution = [
			  [1, 2, 3, 4, 5, 6, 7, 8, 9],
			  [4, 5, 6, 7, 8, 9, 1, 2, 3],
			  [7, 8, 9, 1, 2, 3, 4, 5, 6],
			  [2, 3, 4, 5, 6, 7, 8, 9, 1],
			  [5, 6, 7, 8, 9, 1, 2, 3, 4],
			  [8, 9, 1, 2, 3, 4, 5, 6, 7],
			  [3, 4, 5, 6, 7, 8, 9, 1, 2],
			  [6, 7, 8, 9, 1, 2, 3, 4, 5],
			  [9, 1, 2, 3, 4, 5, 6, 7, 8]
			]
		self.assertEqual(returned_solution, expected_solution)
		
	def test_solve_easy(self):
		easy_grid = [
			[   8, None,    2, None,    5, None,    7, None,    1],
			[None, None,    7, None,    8,    2,    4,    6, None],
			[None,    1, None,    9, None, None, None, None, None],
			[   6, None, None, None, None,    1,    8,    3,    2],
			[   5, None, None, None, None, None, None, None,    9], 
			[   1,    8,    4,    3, None, None, None, None,    6],
			[None, None, None, None, None,    4, None,    2, None], 
			[None,    9,    5,    6,    1, None,    3, None, None], 
			[   3, None,    8, None,    9, None,    6, None,    7] 
			]
		puzzle = Sudoku(easy_grid)
		returned_solution = puzzle.solve()
		expected_solution = [
			[8, 3, 2, 4, 5, 6, 7, 9, 1],
			[9, 5, 7, 1, 8, 2, 4, 6, 3],
			[4, 1, 6, 9, 7, 3, 2, 5, 8],
			[6, 7, 9, 5, 4, 1, 8, 3, 2],
			[5, 2, 3, 7, 6, 8, 1, 4, 9],
			[1, 8, 4, 3, 2, 9, 5, 7, 6],
			[7, 6, 1, 8, 3, 4, 9, 2, 5],
			[2, 9, 5, 6, 1, 7, 3, 8, 4],
			[3, 4, 8, 2, 9, 5, 6, 1, 7]
			]
		self.assertEqual(returned_solution, expected_solution)
		
	def test_get_row(self):
		received_row = self.solved_puzzle.get_row(0)
		expected_row = [1, 2, 3, 4, 5, 6, 7, 8, 9]
		self.assertEqual(received_row, expected_row)
		
	def test_get_column(self):
		received_column = self.solved_puzzle.get_column(0)
		expected_column = [1, 4, 7, 2, 5, 8, 3, 6, 9]
		self.assertEqual(received_column, expected_column)
		
	def test_get_box(self):
		received_box = self.solved_puzzle.get_box(0, 1)
		expected_box = [1, 2, 3, 4, 5, 6, 7, 8, 9]
		self.assertEqual(received_box, expected_box)
		
		received_box = self.solved_puzzle.get_box(8, 8)
		expected_box = [9, 1, 2, 3, 4, 5, 6, 7, 8]
		self.assertEqual(received_box, expected_box)
		
	def test_get_candidates(self):
		received_candidates = self.easy_grid_puzzle.get_candidates(0, 1)
		expected_candidates = {3, 4, 6}
		self.assertEqual(received_candidates, expected_candidates)
