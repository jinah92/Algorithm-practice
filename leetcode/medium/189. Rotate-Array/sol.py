from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if len(nums) < k:
            k %= len(nums)
        sliced_list = nums[len(nums)-k:]
        del nums[len(nums)-k:]
        for num in reversed(sliced_list):
            nums.insert(0, num)

nums = [1,2,3,4,5,6,7]
k = 3
Solution().rotate(nums, k)
