class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26 #Create 26 hash maps.

            for c in s:
                count[ord(c) - ord("a")] += 1 #ord : Convert to a numerical value
            res[tuple(count)].append(s) #tuple : Use immutable values ​​as keys

        return list(res.values())