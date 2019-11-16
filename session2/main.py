import unittest


def is_alive(alive, alive_cells_count):
    if alive_cells_count == 3:
        return True
    if alive_cells_count == 2 and alive:
        return True
    return False


def count_of_alive_neighbours(grid):
  count=0
  if grid[0][0]:
      count +=1
  if grid[0][1]:
      count +=1
  if grid[0][2]:
      count +=1
  if grid[1][0]:
      count +=1
  if grid[1][2]:
      count +=1
  if grid[2][0]:
      count +=1
  if grid[2][1]:
      count +=1
  if grid[2][2]:
      count +=1
  return count

def clip_grid(grid, x, y):
  # len(grid)
  # len(grid[0])


  # grid00=False
  # gird01=False
  # grid02=False
  # if x-1 < 0 :
  #   grid00=False
  #   gird01=False
  #   grid02=False

  g = [[False, False, False], [False, False, False], [False, False, False]]

  print("--")
  for yy in range(3):
    for xx in range(3):
      xxx = xx + x - 1
      yyy = yy + y - 1
      print(str(xxx) + "," + str(yyy))
      if xxx >= 0 and yyy >= 0:
        grid[xxx, yyy] = grid[xx, yy]

  # gird[x-1][y-1]
  return g

class TestFoo(unittest.TestCase):
    def test_is_alive(self):
        self.assertEqual(True, is_alive(True, 3))
        self.assertEqual(True, is_alive(True, 2))
        self.assertEqual(False, is_alive(False, 2))
        self.assertEqual(False, is_alive(True, 1))
        self.assertEqual(False, is_alive(True, 4))
        self.assertEqual(False, is_alive(False, 1))
        self.assertEqual(False, is_alive(False, 4))

    def test_count_of_alive_neighbours(self):
        g = [[False, False, False], [False, False, False], [False, False, False]]
        self.assertEqual(0, count_of_alive_neighbours(g))

        g = [[True, False, False], [False, False, False], [False, False, False]]
        self.assertEqual(1, count_of_alive_neighbours(g))
        g = [[False, True, False], [False, False, False], [False, False, False]]
        self.assertEqual(1, count_of_alive_neighbours(g))
        g = [[False, False, True], [False, False, False], [False, False, False]]
        self.assertEqual(1, count_of_alive_neighbours(g))

        g = [[False, False, False], [True, False, False], [False, False, False]]
        self.assertEqual(1, count_of_alive_neighbours(g))
        g = [[False, False, False], [False, True, False], [False, False, False]]
        self.assertEqual(0, count_of_alive_neighbours(g))
        g = [[False, False, False], [False, False, True], [False, False, False]]
        self.assertEqual(1, count_of_alive_neighbours(g))

        g = [[False, False, False], [False, False, False], [True, False, False]]
        self.assertEqual(1, count_of_alive_neighbours(g))
        g = [[False, False, False], [False, False, False], [False, True, False]]
        self.assertEqual(1, count_of_alive_neighbours(g))
        g = [[False, False, False], [False, False, False], [False, False, True]]
        self.assertEqual(1, count_of_alive_neighbours(g))

        g = [[True, True, True], [True, False, True], [True, True, True]]
        self.assertEqual(8, count_of_alive_neighbours(g))

    def test_clip_gird(self):
      self.assertEqual(
        [[False, False, False], [False, False, False], [False, False, False]],
        clip_grid([[False, False, False], [False, False, False], [False, False, False]], 1, 1)
      )

      g = [[True, False, True], [False, True, False], [True, False, True]]
      self.assertEqual(
        [[True, False, True], [False, True, False], [True, False, True]],
        clip_grid(g, 1, 1)
      )
      self.assertEqual(
        [[False, False, False], [False, True, False], [False, False, True]],
        clip_grid(g, 0, 0)
      )


if __name__ == "__main__":
    unittest.main()
