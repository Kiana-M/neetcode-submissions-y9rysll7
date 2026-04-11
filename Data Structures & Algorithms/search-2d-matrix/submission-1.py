class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #finding the row:
        u,d = 0, len(matrix)-1
        while u<=d:
            m = (u+d)//2
            if matrix[m][0] > target:
                print(matrix[m][0])
                d = m-1
            elif matrix[m][len(matrix[0])-1] < target:
                print(matrix[m][len(matrix[0])-1])
                u = m+1
            else: #we found the row
                return self.binarySearch(matrix[m], target)
        return False
      

    def binarySearch(self, nums: list, target):
        l,r = 0, len(nums)-1
        while l<=r:
            m = (l+r)//2
            if nums[m] > target:
                r = m-1
            elif nums[m] < target:
                l = m+1
            else:
                return True
        return False       