class Solution:
    def isHappy(self, n) -> bool:
        def get_sum_of_digits(num: int):
            digit_list = []
            while num > 0:
                digit_list.append(num%10)
                num = int(num / 10)
            sum = 0
            for digit in digit_list:
                sum += digit ** 2
            return sum
        
        seen_set = set()
        curr = n
        while True:
            sum = get_sum_of_digits(curr)
            print(sum)
            if sum == 1:
                return True
            if sum in seen_set:
                return False
            seen_set.add(sum)
            curr = sum