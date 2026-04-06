class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #i : fixed, j, k using two pointers
        #sort to nums(to use two pointers)
        nums.sort()
        res = []

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = a + nums[l] + nums[r]

                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    #detection nums[l] == nums[l+1]
                    while nums[l] == nums[l-1] and l < r:# Add boundary check to prevent IndexError
                        l += 1
        return res