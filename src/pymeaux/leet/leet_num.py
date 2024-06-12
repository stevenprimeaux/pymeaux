from typing import List


def num_sort_squares(nums: List[int]) -> List[int]:
    squares = [0] * len(nums)

    idx_l = 0
    idx_r = len(nums) - 1
    for i in range(len(nums) - 1, -1, -1):
        if abs(nums[idx_l]) > abs(nums[idx_r]):
            root = nums[idx_l]
            idx_l += 1
        else:
            root = nums[idx_r]
            idx_r -= 1
        squares[i] = root * root

    return squares
