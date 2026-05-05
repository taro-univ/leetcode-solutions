class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if not nums:
            return [-1, -1]

        l = 0
        r = len(nums) - 1
        ans = [-1] * 2

        while l < r:
            m = l + ((r - l) // 2)

            if nums[m] < target:
                l = m + 1

            else:
                r = m

        if nums[l] != target:
            return [-1, -1]

        ans[0] = l

        j = 0
        k = len(nums) 

        while j < k:
            n = j + ((k - j) // 2)

            if nums[n] < target + 1:
                j = n + 1

            else:
                k = n

        ans[1] = j - 1

        return ans
