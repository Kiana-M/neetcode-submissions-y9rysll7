class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.cum_sum = [0]
        for i in range(len(w)):
            self.cum_sum.append(self.cum_sum[-1]+w[i])
            print(self.cum_sum)

    def pickIndex(self) -> int:
        total = self.cum_sum[-1]
        random_sample = random.randrange(0,total)
        l, r = 0, len(self.cum_sum)
        while r-l>1:
            m = (l+r)//2
            if random_sample < self.cum_sum[m]:
                r = m
            else: 
                l = m
        return l
         
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()