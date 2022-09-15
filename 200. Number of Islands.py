# Medium
'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
'''

# DFS

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m ,n = len(grid), len(grid[0])
        island = 0
        def dfs(i,j):
            if i >=m or j >=n or i<0 or j<0:return 
            if grid[i][j] == '0': return #If it is water/reached point then just return
            
            grid[i][j] = "0"
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' :
                    dfs(i,j)
                    island +=1
        return island
