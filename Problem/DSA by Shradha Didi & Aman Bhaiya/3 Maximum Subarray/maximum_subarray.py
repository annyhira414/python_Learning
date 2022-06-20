'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        currentSum = 0

        for n in nums:
            if currentSum < 0:
                currentSum = 0
            currentSum += n
            maxSub = max(maxSub, currentSum)

        return maxSub

'''


def max_SubArray(nums):
    mainArray = nums[0]
    subArray = nums[0]

    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            mainArray += nums[i]
        else:
            mainArray = nums[i]

        if mainArray > subArray:
            subArray = mainArray
    return subArray


nums = [2, 3, 4, 5, 77, -9]
print(max_SubArray(nums))
