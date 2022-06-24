# we don't iterate through the entire array more than once
# the left and right pointers are never going to cross each other
# we don't need extra memory either
# our time complexity is the worst case is big o n  0(n)
# we found a linear algorithm using two pointers to solve this problem

class Do_It:
    def twoSum(self, numbers, target):
        l, r = 0, len(numbers) - 1

        while l < r:
            sum = numbers[l] + numbers[r]

            if sum > target:
                r -= 1
            elif sum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []


do = Do_It()
numbers = [1, 2, 4, 5, 7, 8, 9]
print(do.twoSum(numbers, 6))
