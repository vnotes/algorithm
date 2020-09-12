from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        k = len(nums)
        if k < 3:
            return []
        nums.sort()
        result = []
        for i in range(k):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            p = k - 1
            for j in range(i + 1, k - 1):
                if j >= p:
                    break
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                while p > j and (nums[i] + nums[j] + nums[p]) > 0:
                    p -= 1
                if p == j:
                    break
                if (nums[i] + nums[j] + nums[p]) == 0:
                    result.append([nums[i], nums[j], nums[p]])
        return result


if __name__ == '__main__':
    s = Solution()
    r = s.threeSum([-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4])
    print(r)
