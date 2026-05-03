class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def helper(l: int, r: int) -> int:
            if l > r:
                return -1

            m = l + ((r - l) // 2)

            if nums[m] == target:
                return m
            elif nums[m] < target:
                return helper(m + 1, r)
            else:
                return helper(l, m - 1)
        return helper(0, len(nums) - 1)