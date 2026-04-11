class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k_min, k_max = 1, max(piles)
        res = max(piles)
        while k_min <= k_max:
            k = (k_min + k_max)//2
            hours = 0
            for i in range(len(piles)):
                if piles[i]%k == 0:
                    hours += piles[i]/k
                else:
                    hours += piles[i]//k + 1
                #hours += math.ceil(piles[i]/k)
            if hours > h:
                k_min = k+1
            else:
                res = min(k, res)
                k_max = k-1
        return res


        