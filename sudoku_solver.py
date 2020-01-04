import numpy as np

class InvalidSudokuException(Exception):
	pass

class Sudoku(object):
	
	_grid = None
	_empty_cell_indices = None
	
	def __init__(self, grid):
		if self.is_valid(grid):
			self._grid = grid
			self._empty_cell_indices = self.find_empty_cell_indices()
		else:
			raise InvalidSudokuException
			
	def find_empty_cell_indices(self):
		empty_cell_indices = []
		for row in range(9):
			for column in range(9):
				if self._grid[row][column] is None:
					empty_cell_indices.append((row,column))
		return empty_cell_indices
		
	def is_valid(self, grid):
		# check each row and column contains no repeated numbers
		def exist_repeats_in_list(list_to_check):
			while None in list_to_check:
				list_to_check.remove(None)
			if not len(set(list_to_check))==len(list_to_check):
				return True
			
		for row in range(9):
			list_to_check = grid[row][0:]
			if exist_repeats_in_list(list_to_check):
				return False
			
		for column in range(9):
			list_to_check = [grid[row][column] for row in range(9)]
			if exist_repeats_in_list(list_to_check):
				return False	

		return True
				
	def solve(self):
		index = 0
		while index < len(self._empty_cell_indices):
			row, column = self._empty_cell_indices[index]
			
			candidates = self.get_candidates(row, column)
			
			old_value = self._grid[row][column]
			if old_value is None:
				new_value = 1
			else:
				new_value = old_value + 1
			
			while new_value not in candidates and new_value < 10:
				new_value += 1
				
			if new_value > 9:
				self._grid[row][column] = None
				index -= 1
			else:
				self._grid[row][column] = new_value
				index += 1
				
		return self._grid
	
	def get_row(self, row):
		return [self._grid[row][column] for column in range(9)]
	
	def get_column(self, column):
		return [self._grid[row][column] for row in range(9)]
	
	def get_box(self, row, column):
		row_offset    = 3 * int(np.floor(row/3))
		column_offset = 3 * int(np.floor(column/3))
		box = []
		for row_index in range(3):
			for column_index in range(3):
				box.append(self._grid[row_offset + row_index][column_offset + column_index])
		return box
		
	def get_candidates(self, row, column):
		candidates = set(range(1,10))
		taken_numbers = set(self.get_box(row, column) + self.get_row(row) + self.get_column(column))
		candidates = candidates.difference(taken_numbers)
		return candidates
