from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero_cnt = 0
        while 0 in nums:
            zero_cnt += 1
            nums.remove(0)
        nums.extend([0 for i in range(zero_cnt)])

Solution().moveZeroes([0,1,0,3,12])