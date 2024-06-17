from typing import List


def max_avg_cum(nums: List[int], k: int) -> float:
    sums_cum = [0] * len(nums)
    sums_cum[0] = nums[0]
    for i in range(1, len(nums)):
        sums_cum[i] = sums_cum[i - 1] + nums[i]

    max_sum = sums_cum[k - 1]
    for idx_r in range(k, len(nums)):
        max_sum = max(max_sum, sums_cum[idx_r] - sums_cum[idx_r - k])

    return max_sum / k


def max_avg_slide(nums: List[int], k: int) -> float:
    sum_current = sum(nums[0:k])
    max_sum = sum_current
    for idx_r in range(k, len(nums)):
        sum_current += nums[idx_r] - nums[idx_r - k]
        max_sum = max(max_sum, sum_current)

    return max_sum / k


def max_ones(nums: List[int], k: int) -> int:
    max_ones = 0
    count_zeros = 0

    idx_l = 0
    for idx_r in range(len(nums)):
        if nums[idx_r] == 0:
            count_zeros += 1

        while count_zeros > k:
            if nums[idx_l] == 0:
                count_zeros -= 1
            idx_l += 1

        max_ones = max(max_ones, idx_r - idx_l + 1)

    return max_ones


def min_start(nums: List[int]) -> int:
    min_current = 0

    sum_current = 0
    for n in nums:
        sum_current += n
        min_current = min(sum_current, min_current)

    return 1 - min_current


def sort_squares(nums: List[int]) -> List[int]:
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


def sums_cum(nums: List[int]) -> List[int]:
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]

    return nums
