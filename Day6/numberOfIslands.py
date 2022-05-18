class Solution:
    def bfs(self, grid: List[List[str]], j: int, i: int):
        
        if grid[i][j] == "0":
            return 
    
        grid[i][j] = "0"
        
        if j - 1 >= 0:
            self.bfs(grid, j - 1, i)
        if i - 1 >= 0:
            self.bfs(grid, j, i -1)
        if j + 1 < len(grid[0]):
            self.bfs(grid, j + 1, i)
        if i + 1 < len(grid):
            self.bfs(grid, j, i + 1)
    
    def numIslands(self, grid: List[List[str]]) -> int:
        
        count = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    count += 1
                    self.bfs(grid, j, i)
        
        return count