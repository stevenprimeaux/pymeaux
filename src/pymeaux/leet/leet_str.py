from typing import List


def rev(s: List[str]) -> None:
    idx_l = 0
    idx_r = len(s) - 1
    while idx_l < idx_r:
        temp = s[idx_l]
        s[idx_l] = s[idx_r]
        s[idx_r] = temp

        idx_l += 1
        idx_r -= 1
