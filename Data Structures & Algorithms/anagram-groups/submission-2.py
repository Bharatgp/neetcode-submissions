class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ht = defaultdict(list)

        for s in strs:
            tmp = [0]*26
            for i in s:
                tmp[ord(i)-ord('a')] += 1
            ht[tuple(tmp)].append(s)
        
        return list(ht.values())
