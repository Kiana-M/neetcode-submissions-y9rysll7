class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #two pointer approach. one pointer finds first elelmnt, the other find target-elemnt
        p1, p2 = 0, 1
        while p1 < len(numbers):
            while p2 < len(numbers):
                if target - numbers[p1] == numbers[p2]:
                    return [p1+1, p2+1]
                p2 += 1
            p1 += 1
            p2 = p1+1

        


        