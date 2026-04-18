class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}
        left = 0

        #s1の文字を辞書に格納する
        for i in range(len(s1)):
            count[s1[i]] = 1 + count.get(s1[i], 0)

        for right in range(len(s1), len(s2), 1):
            if right == len(s1):
                for i in range(len(s1)):
                    count[s2[i]] = count.get(s2[i], 0) - 1
                
                if all(v == 0 for v in count.values()):
                    return True
            else:
                count[s2[right]] = count.get(s2[right], 0) - 1
                count[s2[left]]  = count.get(s2[left] , 0) + 1

                if all(v == 0 for v in count.values()):
                    return True
                
                left += 1

        return False