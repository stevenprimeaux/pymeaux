from typing import List
from pymeaux.leet import leet_list, leet_str


class Solution:
    # 643
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        return leet_list.max_avg_slide(nums, k)

    # 1004
    def longestOnes(self, nums: List[int], k: int) -> int:
        return leet_list.max_ones(nums, k)

    # 1413
    def minStartValue(self, nums: List[int]) -> int:
        return leet_list.min_start(nums)

    # 1480
    def runningSum(self, nums: List[int]) -> List[int]:
        return leet_list.sums_cum(nums)

    def reverseString(self, s: List[str]) -> None:
        leet_str.rev(s)

    def sortedSquares(self, nums: List[int]) -> List[int]:
        return leet_list.sort_squares(nums)
