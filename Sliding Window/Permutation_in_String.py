class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 , n2 = len(s1), len(s2)
        #まず制約条件チェック
        if n1 > n2:
            return False

        count = {}
        #1 s1の文字をプラス
        for char in s1:
            count[char] = count.get(char, 0) + 1

        #2最初のウィンドウ文をカウント
        for i in range(n1):
            count[s2[i]] = count.get(s2[i], 0) -1

        if all(v == 0 for v in count.values()):
            return True

        for right in range(n1, n2):
            left = right - n1

            # 右から入る文字を引く
            count[s2[right]] = count.get(s2[right], 0) - 1
            # 左から出る文字を戻す
            count[s2[left]] = count.get(s2[left], 0) + 1

            if all(v == 0 for v in count.values()):
                return True

        return False