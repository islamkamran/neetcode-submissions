class Solution:
    def isHappy(self, n: int) -> bool:
        check = set()

        while n not in check:
            check.add(n)
            n = self.sum_square(n)
            if n == 1:
                return True
        return False
        

    def sum_square(self, n: int):
        sum_square = 0
        while n:
            value = n % 10
            value = value ** 2
            sum_square += value
            n = n // 10
        return sum_square