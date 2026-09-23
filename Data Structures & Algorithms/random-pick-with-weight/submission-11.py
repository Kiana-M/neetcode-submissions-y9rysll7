class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.suum = sum(w)

    def pickIndex(self) -> int:
        rand_sum = random.randrange(0, self.suum)
        print(rand_sum)
        run_sum = 0
        for i in range(len(self.w)):
            run_sum += self.w[i]
            if run_sum>rand_sum:
                return i
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()