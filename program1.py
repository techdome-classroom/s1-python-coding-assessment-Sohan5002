class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        # Check if the grid is empty
        if not grid:
            return 0
        
        # Dimensions of the grid
        rows, cols = len(grid), len(grid[0])
        island_count = 0
    
        def dfs(r, c):
            # Boundary and water check
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 'W':
                return
            # Mark the current land ('L') as visited by turning it into water ('W')
            grid[r][c] = 'W'
            dfs(r-1, c)  # Up
            dfs(r+1, c)  # Down
            dfs(r, c-1)  # Left
            dfs(r, c+1)  # Right
        
        # Traverse through the entire grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'L':  # Unvisited land
                    island_count += 1  # Found a new island
                    dfs(r, c)  # Perform DFS to mark the entire island
        
        return island_count
