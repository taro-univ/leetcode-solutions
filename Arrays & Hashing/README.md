# Arrays & Hashing

LeetCode の Arrays & Hashing カテゴリの解答まとめ。

---

## 問題一覧

| # | 問題名 | 難易度 | アルゴリズム | 計算量 |
|---|--------|--------|-------------|--------|
| 1 | [Two Sum](#1-two-sum) | Easy | ハッシュマップ | O(n) |
| 49 | [Group Anagrams](#49-group-anagrams) | Medium | ソート / 文字カウント | O(n·k log k) / O(n·k) |
| 347 | [Top K Frequent Elements](#347-top-k-frequent-elements) | Medium | ソート / バケットソート | O(n log n) / O(n) |
| 238 | [Product of Array Except Self](#238-product-of-array-except-self) | Medium | 左右積 (ピンサー) | O(n) |
| 271 | [Encode and Decode Strings](#271-encode-and-decode-strings) | Medium | 長さプレフィックス | O(n) |
| 36 | [Valid Sudoku](#36-valid-sudoku) | Medium | ハッシュセット | O(1) |
| 128 | [Longest Consecutive Sequence](#128-longest-consecutive-sequence) | Medium | ハッシュセット | O(n) |

---

## 1. Two Sum

**ファイル:** `Two Sum.py`

### アプローチ
ハッシュマップ (`prevMap`) に「値 → インデックス」を記録しながら1回のループで解く。

```
diff = target - num
if diff in prevMap → 答えが見つかった
else → prevMap[num] = i として記録
```

### 計算量
- 時間: O(n)
- 空間: O(n)

---

## 49. Group Anagrams

**ファイル:** `Group Anagrams.py` / `GroupAnagram2.py`

### アプローチ 1 — ソート (`Group Anagrams.py`)
各単語をソートしてキーにする。`"eat"` → `"aet"` のようにアナグラムは同じキーになる。

### アプローチ 2 — 文字カウント (`GroupAnagram2.py`)
26文字のカウント配列を `tuple` 化してキーにする。ソート不要で O(n·k) に改善。

```python
count = [0] * 26
for c in s:
    count[ord(c) - ord("a")] += 1
res[tuple(count)].append(s)
```

### 計算量
| 手法 | 時間 | 空間 |
|------|------|------|
| ソート | O(n·k log k) | O(n·k) |
| 文字カウント | O(n·k) | O(n·k) |

---

## 347. Top K Frequent Elements

**ファイル:** `topKFrequent.py` / `topKFrequent_optimized.py`

### アプローチ 1 — ソート (`topKFrequent.py`)
出現回数を `defaultdict` でカウントし、降順ソートして上位 k 件を返す。

### アプローチ 2 — バケットソート (`topKFrequent_optimized.py`)
`freq[出現回数]` にその要素を格納し、末尾（高頻度）から k 個集める。ソート不要で O(n)。

```
freq = [[] for _ in range(len(nums) + 1)]
freq[cnt].append(n)
← 末尾から k 個取り出す
```

### 計算量
| 手法 | 時間 | 空間 |
|------|------|------|
| ソート | O(n log n) | O(n) |
| バケットソート | O(n) | O(n) |

---

## 238. Product of Array Except Self

**ファイル:** `ProductsOfArrayExceptSelf.py`

### アプローチ — ピンサー攻撃 (左右積)
除算を使わず、左からの累積積と右からの累積積を別々に計算して合成する。

```
左パス: output[i] = (i より左の積)   ← 後入れで自分を含めない
右パス: output[i] *= (i より右の積)  ← 後入れで自分を含めない
```

### 計算量
- 時間: O(n)
- 空間: O(1) (出力配列を除く)

---

## 271. Encode and Decode Strings

**ファイル:** `EncodeAndDecodeStrings.py`

### アプローチ — 長さプレフィックス
各文字列を `"長さ#文字列"` 形式に変換してエンコード。デコード時は `#` の手前まで読んで長さを取得し、その分だけスライスする。

```
encode: "eat" → "3#eat"
decode: i→j で '#' を探す → length = s[i:j] → s[j+1 : j+1+length]
```

### 計算量
- 時間: O(n)
- 空間: O(n)

---

## 36. Valid Sudoku

**ファイル:** `ValidSudoku.py`

### アプローチ
行・列・3×3ブロックそれぞれに `set` を用意し、重複があれば即 `False`。

```python
index = (r // 3) * 3 + (c // 3)  # 3×3ブロックのインデックス計算
```

### 計算量
- 時間: O(1)（盤面サイズ固定 9×9）
- 空間: O(1)（固定サイズのセット）

---

## 128. Longest Consecutive Sequence

**ファイル:** `longestConsecutive.py`

### アプローチ — ハッシュセット + 連続列の始点探索
全要素を `set` に変換し、「連続列の始点 (n-1 がセットにない要素)」からのみ連続カウントを開始する。始点以外はスキップするため、各要素は最大1回しか処理されない。

```python
num_set = set(nums)
for n in num_set:
    if n - 1 not in num_set:  # 始点の判定
        while current_num + 1 in num_set:
            current_num += 1
            current_streak += 1
```

### 計算量
- 時間: O(n)
- 空間: O(n)
