class Solution:
    def isHappy(self, n: int) -> bool:
        check_number = set()

        while n not in check_number:
            check_number.add(n)

            n = self.calc_square(n)
            if n == 1:
                return True
        return False

        
    def calc_square(self, n: int)->int:
        output = 0

        while n:
            digit = n % 10
            digit = digit ** 2
            output +=digit

            n = n // 10
            
        return output
        