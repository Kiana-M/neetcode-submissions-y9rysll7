class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_len = 0
        
        for num in num_set:
            if (num-1) in num_set:
                continue
            else:
                cur_len = 0
                while num+ cur_len in num_set:
                    cur_len += 1
                max_len = max(max_len, cur_len)
        return max_len
                
                
        