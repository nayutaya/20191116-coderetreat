import unittest

def next_state(alive_count):
  if alive_count == 2: return True
  if alive_count == 3: return True
  return False

def get_number_of_alive_neighbours(grid):
  # FIXME: assert
  count = 0
  if grid[0][0]: count += 1
  if grid[0][1]: count += 1
  if grid[0][2]: count += 1
  if grid[1][0]: count += 1
  if grid[1][2]: count += 1
  if grid[2][0]: count += 1
  if grid[2][1]: count += 1
  if grid[2][2]: count += 1

  return count

A = True
D = False

class Lifegame(unittest.TestCase):
  def test_next_state(self):
    self.assertEqual(False, next_state(0))
    self.assertEqual(False, next_state(1))
    self.assertEqual(True,  next_state(2))
    self.assertEqual(True,  next_state(3))
    self.assertEqual(False, next_state(4))
    self.assertEqual(False, next_state(5))
    self.assertEqual(False, next_state(6))
    self.assertEqual(False, next_state(7))
    self.assertEqual(False, next_state(8))
  
  def test_get_number_of_neighbours(self):
    g1 = [[D, D, D], [D, D, D], [D, D, D]]
    self.assertEqual(0, get_number_of_alive_neighbours(g1))
    g2 = [[A, A, A], [A, A, A], [A, A, A]]
    self.assertEqual(8, get_number_of_alive_neighbours(g2))
    
    g3 = [[A, D, D], [D, D, D], [D, D, D]]
    self.assertEqual(1, get_number_of_alive_neighbours(g3))
    g4 = [[D, A, D], [D, D, D], [D, D, D]]
    self.assertEqual(1, get_number_of_alive_neighbours(g4))
    g5 = [[D, D, A], [D, D, D], [D, D, D]]
    self.assertEqual(1, get_number_of_alive_neighbours(g5))
    g6 = [[D, D, D], [A, D, D], [D, D, D]]
    self.assertEqual(1, get_number_of_alive_neighbours(g6))
    g7 = [[D, D, D], [D, A, D], [D, D, D]]
    self.assertEqual(0, get_number_of_alive_neighbours(g7))
    g8 = [[D, D, D], [D, D, A], [D, D, D]]
    self.assertEqual(1, get_number_of_alive_neighbours(g8))
    g9 = [[D, D, D], [D, D, D], [A, D, D]]
    self.assertEqual(1, get_number_of_alive_neighbours(g9))
    g10 = [[D, D, D], [D, D, D], [D, A, D]]
    self.assertEqual(1, get_number_of_alive_neighbours(g10))
    g11 = [[D, D, D], [D, D, D], [D, D, A]]
    self.assertEqual(1, get_number_of_alive_neighbours(g11))
  
  # def test_get_number_of_neighbours_2(self):
  #   g = [[D, D, D], [D, D, D], [D, D, D]]
  #   self.assertEqual(0, get_number_of_alive_neighbours(g, , 1))


if __name__ == "__main__":
    unittest.main()
