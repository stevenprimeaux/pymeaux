from typing import List


def win_avg_max_cum(nums: List[int], k: int) -> float:
    sums_cum = [0] * len(nums)
    sums_cum[0] = nums[0]
    for i in range(1, len(nums)):
        sums_cum[i] = sums_cum[i - 1] + nums[i]

    max_sum_current = sums_cum[k - 1]
    for idx_r in range(k, len(nums)):
        max_sum_current = max(max_sum_current, sums_cum[idx_r] - sums_cum[idx_r - k])

    return max_sum_current / k


def win_avg_max_slide(nums: List[int], k: int) -> float:
    sum_current = sum(nums[0:k])
    max_sum_current = sum_current
    for idx_r in range(k, len(nums)):
        sum_current += nums[idx_r] - nums[idx_r - k]
        max_sum_current = max(max_sum_current, sum_current)

    return max_sum_current / k
