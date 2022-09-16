# Hard
'''
You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.

 

Example 1:

Input: grid = [[1,0],[0,1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
Example 2:

Input: grid = [[1,1],[1,0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
Example 3:

Input: grid = [[1,1],[1,1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.

'''
#DFS

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        def dfs(i,j,island):
            
            if i<0 or i>=n or j<0 or j >=n or grid[i][j] ==0: return 0
            if grid[i][j] !=1: return 0
            grid[i][j]= island
            return 1+ dfs(i,j+1,island) + dfs(i, j-1,island) + dfs(i+1,j,island) + dfs(i-1, j,island)

        island = 2
        area = {}
        for i in range(n):
            for j in range(n):
                if grid[i][j] ==1:
                    area[island] = dfs(i,j,island) # area is a dict including idx(>1) as key and island area as value
                    island+=1
        
     
        ans = max(area.values() or [0]) # fix problems if no island in the matrix
       
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    seen = {grid[ni][nj] for ni, nj in zip((i,i,i+1,i-1),(j+1,j-1, j,j)) if 0<=ni<n and 0<=nj<n and  grid[ni][nj] > 1}
                    ans = max(ans, 1 + sum(area[i] for i in seen))
        return ans
