from typing import List
from pymeaux.leet import leet_num, leet_str, leet_win


class Solution:
    # 643
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        return leet_win.max_avg_slide(nums, k)

    # 1004
    def longestOnes(self, nums: List[int], k: int) -> int:
        return leet_win.max_ones(nums, k)

    def reverseString(self, s: List[str]) -> None:
        leet_str.str_rev(s)

    def sortedSquares(self, nums: List[int]) -> List[int]:
        return leet_num.num_sort_squares(nums)
