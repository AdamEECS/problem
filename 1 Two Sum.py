class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            second = target - nums[i]

            if second in nums:
                l = [i for i, x in enumerate(nums) if x == second]
                if nums[i] != second:
                    return [i, nums.index(second)]
                elif len(l) > 1:
                    return [i, l[1]]


s = Solution()
print(s.twoSum([3, 3, 4], 6))
