from typing import List


def num_sort_squares(nums: List[int]) -> List[int]:
    len_nums = len(nums)
    sorted = [0] * len_nums

    idx_l = 0
    idx_r = len_nums - 1
    for i in range(len_nums - 1, -1, -1):
        if abs(nums[idx_l]) > abs(nums[idx_r]):
            root = nums[idx_l]
            idx_l += 1
        else:
            root = nums[idx_r]
            idx_r -= 1
        sorted[i] = root * root

    return sorted
