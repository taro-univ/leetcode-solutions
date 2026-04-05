from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: 各要素の出現回数をカウント
        count = defaultdict(int)
        for n in nums:
            count[n] += 1

        # Step 2: 頻度バケットを作成
        # インデックス = 出現回数、値 = その回数で出現する要素のリスト
        # 出現回数の最大値は len(nums) なので、サイズは len(nums) + 1
        freq = [[] for _ in range(len(nums) + 1)]
        for n, cnt in count.items():
            freq[cnt].append(n)

        # Step 3: 頻度の高い順（末尾から）にk個集める
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


if __name__ == "__main__":
    sol = Solution()

    # テストケース一覧: (nums, k, 期待される出力の説明)
    test_cases = [
        ([1, 1, 1, 2, 2, 3], 2, "上位2件: [1, 2]"),
        ([1], 1, "要素が1つ: [1]"),
        ([4, 4, 4, 6, 6, 7], 1, "最頻値のみ: [4]"),
        ([1, 2, 3, 4, 5], 3, "全て出現回数1（どれか3つ）"),
        ([-1, -1, 2, 2, 2], 2, "負の数を含む: [2, -1]"),
    ]

    for nums, k, description in test_cases:
        result = sol.topKFrequent(nums, k)
        print(f"nums={nums}, k={k}")
        print(f"  説明    : {description}")
        print(f"  結果    : {result}")
        print()
