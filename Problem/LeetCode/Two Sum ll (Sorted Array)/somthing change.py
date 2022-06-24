class Sou:
    def sum(self, number, target):
        l = 0
        r = len(number) - 1

        while l < r:
            do_sum = number[l] + number[r]

            if do_sum == target:
                return [l + 1, r + 1]
            elif do_sum < target:
                l += 1
            elif do_sum > target:
                r -= 1
        return []


Twosum = Sou()
number = [1, 3, 4, 5, 6, 7, 8, 9]
print(Twosum.sum(number, 11))

'''
class Solution:
    def twoSum(self, numbers,target):
        l, r = 0, len(numbers) - 1

        while l < r:
            currentSum = numbers[1] + numbers[1] # aitai vul amr 

            if currentSum == target:
                return [l + 1, r + 1]
            elif currentSum < target:
                l += 1
            elif currentSum > target:
                r -= 1

        return []
sum = Solution()
numbers = [2,7,11,15]
print(sum.twoSum(numbers, 9))
# [2,7,11,15], target = 9 

'''