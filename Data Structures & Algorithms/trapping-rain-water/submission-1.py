class Solution:
    def trap(self, height: List[int]) -> int:
        # water gets trapped between 2 maxs that have min between them
        # the amount of trapped water for each point is min(max-right, max-left-height) - height[point]
        # so we calc these amounts for each point and put it in 3 arrays
        # o(n) memory, o(n) time
        max_left = [0 for i in range(len(height))] #max value on the left of each point
        max_right = [0 for i in range(len(height))] # min value on the left of each point
        min_maxes = [0 for i in range(len(height))] # min of the above lists
    
        max_keeper = 0
        for i in range(len(height)):
            max_keeper = max(height[i], max_keeper)
            max_left[i] = max_keeper
        
        max_keeper = 0
        for i in range(len(height)-1, -1, -1):
            max_keeper = max(height[i], max_keeper)
            max_right[i] = max_keeper
            
        min_maxes = [min(max_left[i], max_right[i]) - height[i] for i in range(len(height))]
        
        return sum(min_maxes)
            
