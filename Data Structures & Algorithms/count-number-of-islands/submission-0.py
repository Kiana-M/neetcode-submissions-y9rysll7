class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #Walk every cell. When we see a '1' we haven't visited, that's a new island — start a DFS/BFS from it, marking everything reachable as visited. Increment our island counter.
        def dfs(a, b, visited):
            if (a,b) in visited:
                return
            if grid[a][b] == '0':
                return
            visited.add((a,b))

            for (i,j) in [(0,1), (1,0), (-1,0), (0,-1)]:
                if 0 <= a+i < len(grid) and 0 <= b+j < len(grid[0]):
                    dfs(a+i, b+j, visited)

        num = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited and grid[i][j] == '1':
                    num += 1
                dfs(i,j, visited)
        return num

        