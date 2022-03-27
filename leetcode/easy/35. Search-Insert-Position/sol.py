from typing import List

def searchInsert(self, nums: List[int], target: int) -> int:
    start = 0
    end = len(nums)-1
    
    while start <= end:
        mid = start + int((end-start)/2)            
        if nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    
    return start