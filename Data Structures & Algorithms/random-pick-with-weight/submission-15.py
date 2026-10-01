class Solution:
# A strong interview-style explanation would be:
# “I transform the weights into prefix sums. Each weight then corresponds to an interval whose length equals that weight. I uniformly sample a random value across the total weight. Since the probability of landing in an interval is its length divided by the total length, index i is selected with probability w[i] / sum(w). Finally, I use binary search on the prefix sums to find which interval contains the sampled value.”
    def __init__(self, w: List[int]):
        self.prefix = [0]
        for i in range(len(w)):
            self.prefix.append(w[i]+self.prefix[i])

    def pickIndex(self) -> int:
        draw = random.randrange(0, self.prefix[-1])
        l, r = 0, len(self.prefix)-1
        while r-l>1:
            m = (l+r)//2
            if draw >= self.prefix[m]:
                l = m
            else:
                r = m
        return l
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()