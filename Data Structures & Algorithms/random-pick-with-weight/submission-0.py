class Solution:

    def __init__(self, w: List[int]):
        self.total_sum = sum(w) 
        self.w = w

    def pickIndex(self) -> int:
        random_sum = random.randrange(0,self.total_sum)
        running_sum, i = 0,0
        while running_sum <= random_sum:
            running_sum += self.w[i]
            i += 1
        return i-1

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()