class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        #targetの存在が保証されていないのでl <= r
        while l <= r:
            #mの定義に注意
            m = l + ((r - l) // 2)
            if nums[m] == target:
                return m
            #左右どちらが綺麗にsortされているか
            elif nums[m] > nums[r]:
                #左側はソート済み, 右側はどこかに最小値がある状態
                #まず左側の判定。左端の判定を追加するのを忘れないように
                if target < nums[m] and nums[l] <= target:
                    r = m - 1
                else:
                    l = m + 1
            else:
                #右側はソート済み
                if target > nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return -1