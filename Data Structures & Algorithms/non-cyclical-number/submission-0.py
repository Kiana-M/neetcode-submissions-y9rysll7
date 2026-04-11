class Solution:
    def isHappy(self, n: int) -> bool:
        sum_set = set()
        #break into digits:
        def digits(num):
            res = []
            while num//10 != 0:
                res.append(num%10)
                num = num//10
            res.append(num%10)
            return res
        print(digits(n))
        sumSq = sum([digit**2 for digit in digits(n)])
        if sumSq == 1:
            return True
        while sumSq not in sum_set:
            print(sumSq)
            sum_set.add(sumSq)
            sumSq = sum([digit**2 for digit in digits(sumSq)])
            if sumSq ==1:
                return True
        return False

            