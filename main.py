print('Hello')



class Solution:
    def countOdds(self, low: int, high: int) -> int:
        odd = (high - low) // 2
        

        if low % 2 == 1 or high % 2 == 1:
            odd += 1
        

        return odd
    
    

def average(salary):
    min_salary = min(salary)
    max_salary = max(salary)
    sum_salary = sum(salary) - min_salary - max_salary
    return sum_salary / (len(salary) - 2)



return nums == sorted(nums) or nums == sorted(nums, reverse=True)



def hamming_weight(n):
    binary = bin(n)[2:]  
    count = 0
    for bit in binary:
        if bit == '1':
            count += 1
    return count


def digit_difference(n):
    str_n = str(n)
    product = 1
    sum = 0
    for digit in str_n:
        digit = int(digit)
        product *= digit
        sum += digit
    return product - sum
