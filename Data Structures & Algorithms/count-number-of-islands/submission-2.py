class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nums = 0
        def dfs(r,c):
            if r < 0 or r >= len(grid[0]) or c < 0 or c >= len(grid):
                return
            if grid[c][r] == '0':
                return
            if grid[c][r] == '1':
                grid[c][r] = '#'
            
                dfs(r+1, c)
                dfs(r,c+1)
                dfs(r-1,c)
                dfs(r, c-1)

        for i in range(len(grid[0])):
            for j in range(len(grid)):
                if grid[j][i] == "1":
                    nums += 1
                    dfs(i, j)

        return nums



        