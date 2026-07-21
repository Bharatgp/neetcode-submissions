class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ht = {}

        for s in strs:
            tmp = [0]*26
            for c in s:
                tmp[ord('a')-ord(c)] += 1
            key = tuple(tmp)                
            if key in ht:
                ht[key].append(s)
            else:
                ht[key] = [s]
        
        return list(ht.values())


