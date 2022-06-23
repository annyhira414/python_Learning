class Solution:
    def twoSum(self, nums: [int], target: int):
        ans = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in ans:
                return [ans[diff], i]
            ans[n] = i
        return


take = Solution()
nums = [1, 3, 5, 2]
print(take.twoSum(nums, 4))
