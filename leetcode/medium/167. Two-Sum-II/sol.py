from turtle import st
from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r_idx = bisect_right(numbers, target)
        answer = []
        for i in range(r_idx):
            if target - numbers[i] in numbers:
                answer.append(i+1)
                answer.append(bisect_right(numbers, target-numbers[i]))
                if len(answer) == 2:
                    break
        if answer == []:
            l_idx = bisect_left(numbers, target)
            for j in numbers[l_idx:]:
                if target - numbers[j] in numbers:
                    answer.append(j+1+l_idx)
                    answer.append(numbers.index(target-numbers[j])+1+l_idx)
        
        return answer

numbers = [2,7,11,15]
target = 9

Solution().twoSum(numbers, target)