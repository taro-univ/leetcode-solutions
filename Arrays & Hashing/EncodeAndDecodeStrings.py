class Solution:

    def encode(self, strs: List[str]) -> str:
        #Chunked Encoding風のアプローチ
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            # "#" を探す
            j = i
            while s[j] != "#":
                j += 1

            # 次に、長さを取得
            length = int(s[i:j])
            #2ケタ以上の長さの場合を考慮

            #長さの分だけ抽出
            res.append(s[j + 1: j + 1 + length])

            i = j + 1 + length

        return res