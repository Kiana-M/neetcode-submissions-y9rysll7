class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #max (l-r)*min(heights[l],heights[r])
        max_a = 0
        l,r = 0, len(heights)-1
        while l<r:
            a = (r-l)*min(heights[r],heights[l])
            max_a = max(a, max_a)
            if heights[r]<heights[l]:
                r-=1
            else:
                l+=1
        return max_a

        