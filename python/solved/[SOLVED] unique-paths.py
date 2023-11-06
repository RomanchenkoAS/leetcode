'''There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]).
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down 
or right at any point in time.
Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the 
bottom-right corner.
The test cases are generated so that the answer will be less than or equal to 2 * 109.'''



class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        if m == 1 and n == 1:
            return 1
        
        # Already calculated cells
        seen = dict()
        
        def calculate_paths(i, j):
            
            if (i,j) == (0,1) or (i,j) == (1,0):
                return 1

            prev = seen.get((i,j))
            
            if prev:
                return seen[(i,j)]

            subtotal = 0
            
            if i > 0:
                subtotal += calculate_paths(i - 1, j)
            
            if j > 0:
                subtotal += calculate_paths(i, j - 1)
                
            seen[(i,j)] = subtotal
                
            return subtotal
        
        return calculate_paths(m - 1, n - 1)
                
                
s = Solution()
m = 2
n = 2
print(s.uniquePaths(m,n))

seen = dict()

print(seen.get(1))