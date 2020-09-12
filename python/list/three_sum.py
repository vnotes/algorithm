from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    if len(nums) < 3:
        return []
    result = []
    nums.sort()
    i, j, k = 0, 1, len(nums) - 1
    while i <= k - 2:
        if i == 1:
            pass
        if i > 0 and nums[i - 1] == nums[i]:
            i += 1
            j = i + 1
            continue
        while j < k:
            rs = nums[i] + nums[j] + nums[k]
            if rs == 0:
                t = [nums[i], nums[j], nums[k]]
                if result and result[-1] == t:
                    j += 1
                    continue
                result.append(t)
                j += 1
            elif rs < 0:
                j += 1
            else:
                k -= 1
        i += 1
        j = i + 1
        k = len(nums) - 1
    return result


if __name__ == '__main__':
    print(three_sum([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]))
    s = [[-4, -2, 6], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2], [-2, -2, 4], [-2, 0, 2]]
