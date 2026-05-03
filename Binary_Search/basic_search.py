class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #探索範囲を示す左右のポインタを初期化
        l, r = 0, len(nums) - 1

        while l <= r:
            #中央のインデックスを計算
            m = l + ((r - l) // 2)

            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m

        return -1