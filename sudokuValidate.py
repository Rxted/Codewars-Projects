'''
Given a Sudoku data structure with size NxN, N > 0 and √N == integer, write a method to validate if it has been filled out correctly.

The data structure is a multi-dimensional Array(in Rust: Vec<Vec<u32>>) , ie:

[
  [7,8,4,  1,5,9,  3,2,6],
  [5,3,9,  6,7,2,  8,4,1],
  [6,1,2,  4,3,8,  7,5,9],

  [9,2,8,  7,1,5,  4,6,3],
  [3,5,7,  8,4,6,  1,9,2],
  [4,6,1,  9,2,3,  5,8,7],

  [8,7,6,  3,9,4,  2,1,5],
  [2,4,3,  5,6,1,  9,7,8],
  [1,9,5,  2,8,7,  6,3,4]
]
'''
from math import sqrt
from math import floor
class Sudoku(object):
    def __init__(self, data):
      self.no = True
      for a in data:
        for b in a:
          if isinstance(b, bool) or not isinstance(b, int):
             self.no = False
             break
        if self.no == False:
          break
      self.data = data     
    def row_check(self, grid, n, bad):
      if self.no == False:
        return False
      for i in range(0,len(grid)):
        bucket = []
        for f in range(1, n+1):
          bucket.append(f)
        for j in range(0, len(grid[i])):
          if grid[i][j] in bucket:
            bucket.remove(grid[i][j])
          else:
            bad = True
            break
        if bad==True:
          return False
    def is_valid(self):
        grid = self.data
        bad = False
        n = int(len(grid))
        if self.row_check(grid, n, bad) == False:
          return False
        zip(*grid[::-1])
        if self.row_check(grid, n, bad) == False:
          return False
        num = 0
        for i in range(1, n+1):
          num+=i
        emlist = []
        for i in range(0, int(sqrt(len(grid)))):
          emlist.append([])
          for j in range(0, int(sqrt(len(grid)))):
            emlist[i].append(0)
        x = int(sqrt(n))
        for i in range(0, len(grid)):
          for j in range(0, len(grid[i])):
              #I thought this was clever
            emlist[floor(i/x)][floor(j/x)]+=grid[i][j]
        for i in emlist:
          for j in i:
            if j != num:
              return False
        return True