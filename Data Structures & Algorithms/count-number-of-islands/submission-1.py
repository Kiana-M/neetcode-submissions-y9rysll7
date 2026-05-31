class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #Walk every cell. When we see a '1' we haven't visited, that's a new island — start a DFS/BFS from it, marking everything reachable as visited. Increment our island counter.
        def dfs(r,c):
            if grid[r][c] == '0' or grid[r][c] == '#':
                return
            if grid[r][c] == '1':
                grid[r][c] = '#'
            #move through the grid
            if r-1>=0:
                dfs(r-1, c)
            if c-1>=0:
                dfs(r,c-1)
            if r+1<len(grid):
                dfs(r+1, c)
            if c+1<len(grid[0]):
                dfs(r, c+1)
        nums = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    nums+=1
                    dfs(i,j)
        return nums


                
        