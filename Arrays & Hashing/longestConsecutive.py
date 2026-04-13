class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #まずハッシュマップをsetを使用して作成
        num_set = set(nums)
        longest_streak = 0

        for n in num_set:
            if n-1 not in num_set: # 開始地点の判定
                current_num = n
                current_streak = 1

                # 次の数字がセットにある間、ループを回す
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak