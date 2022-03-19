def search(self, nums: List[int], target: int) -> int:
    for i in range(len(nums)):
        if nums[i] == target:
            return i
        if nums[i] > target:
            return -1
    return -1