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

# Test Cases

# Example 1
grid1 = [
    ["L", "L", "L", "L", "W"],
    ["L", "L", "W", "L", "W"],
    ["L", "L", "W", "W", "W"],
    ["W", "W", "W", "W", "W"]
]

# Example 2
grid2 = [
    ["L", "L", "W", "W", "W"],
    ["L", "L", "W", "W", "W"],
    ["W", "W", "L", "W", "W"],
    ["W", "W", "W", "L", "L"]
]

# Create an instance of the clas
solution = Solution()

# Testing
print(solution.getTotalIsles(grid1))  
print(solution.getTotalIsles(grid2)) 
