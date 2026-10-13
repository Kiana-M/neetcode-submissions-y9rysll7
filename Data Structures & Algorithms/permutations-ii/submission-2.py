class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.count = {num:0 for num in nums}
        for num in nums:
            self.count[num] += 1
        res = []

        def backtrack(path):
            if len(path) == len(nums) and path not in res:
                res.append(path.copy())
                return
            
            for number in self.count:
                if self.count[number]>0:
                    path.append(number)
                    self.count[number] -= 1
                    backtrack(path)
                    self.count[number] += 1
                    path.pop()
        
        backtrack([])
        return res

        