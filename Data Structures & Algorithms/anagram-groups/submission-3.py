class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ht = defaultdict(list)

        for s in strs:
            ht[tuple(sorted(s))].append(s)
        res = []
        for v in ht.values():
            res.append(v)
        return res
        