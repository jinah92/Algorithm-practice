from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
       return sorted(list(map(lambda x: x ** 2, nums)))