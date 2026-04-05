class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            #lenが返すのはint → strに変換
            res += str(len(s)) + "#" + s
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            #ifではなくwhileで
            # "#"のギリギリ手前まで行きたいから
            while s[j] != "#":
                j += 1
            #sはstr → intに変換    
            length = int(s[i:j])

            # += すると要素をバラバラにして格納する
            # よってappendを使用する
            res.append(s[j + 1 : j + 1 + length])

            i = j + 1 + length

        return res