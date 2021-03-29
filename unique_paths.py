# Given an nxm grid, return the number of possible paths a robot located at the 
# top left corner can take to reach the bottom right corner. The robot can only move right or down
# at any time. 
# Example: n = 3, m = 7 -> returns 28
def uniquePaths(n, m):
  if m == 1 or n == 1:
    return 1
  else:
    return uniquePaths(n-1, m) + uniquePaths(n, m-1)
