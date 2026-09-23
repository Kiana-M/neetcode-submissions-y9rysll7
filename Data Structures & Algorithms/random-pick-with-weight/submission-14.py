class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.suum = sum(w)
        self.cum_sum = [w[0]]
        for i in range(1,len(w)):
            self.cum_sum.append(w[i]+self.cum_sum[i-1])

    def pickIndex(self) -> int:
        rand_sum = random.randrange(0, self.suum)
        l, r = 0, len(self.w)-1
        while l<r:
            m = (l+r)//2
            if self.cum_sum[m]<=rand_sum:
                l = m + 1
            else:
                r = m
        return l


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()