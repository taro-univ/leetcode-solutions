class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #行、列、ブロックでハッシュセットを用意
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        #盤面のセル(r, c)をループで回る
        r = 0
        while r < 9:
            c = 0 #各行の開始時にcを0にリセット
            while c < 9:
                index = (r//3) * 3 + (c//3)
                val = board[r][c]
                #空欄ならスキップ
                if val == ".":
                    c += 1
                    continue #空欄なら以下の処理を飛ばす
                    
                if (val in rows[r] or
                    val in cols[c] or
                    val in squares[index]):
                    return False
        
                rows[r].add(val)
                cols[c].add(val)
                squares[index].add(val)
                
                c += 1
            
            r += 1

        return True