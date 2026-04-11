class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #two pointer approach. one pointer finds first elelmnt, the other find target-elemnt
        p1, p2 = 0, len(numbers)-1

        while p1 < p2:
            if numbers[p1] + numbers[p2] == target:
                return [p1+1, p2+1]
            elif numbers[p1] + numbers[p2] < target:
                p1 += 1
                continue
            elif numbers[p1] + numbers[p2] > target:
                p2 -= 1
                continue
        
        
        

        


        