class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} #各文字の出現頻度を記録
        res = 0
        left = 0
        max_f = 0 #ウィンドウ内での最大頻度

        for right in range(len(s)):
            #右端の文字をcountに追加
            #dictになければdefault_value = 0を返すgetの活用
            count[s[right]] = 1 + count.get(s[right], 0)
            #出現頻度最大を更新
            max_f = max(max_f, count[s[right]])

            #ウィンドウが無効なら左端を動かす
            
            while right - left + 1 - max_f > k:
                count[s[left]] -= 1
                left += 1

            #最大の長さを更新
            res = max(res, right - left + 1)

        return res
