class TwoSum:
    def twoSum(self, nums: int, target: int):

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


put = TwoSum()
nums = [1, 3, 4, 6]  # [0, 1, 2, 3] so 3 + 6 = 9
print(put.twoSum(nums, 9))
