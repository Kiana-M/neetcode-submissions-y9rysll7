class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1=0
        while p1<len(numbers):
            p2 = p1+1
            while p2<len(numbers):
                if numbers[p1] + numbers[p2] == target:
                    return [p1+1,p2+1]
                p2 += 1
            p1+= 1

        