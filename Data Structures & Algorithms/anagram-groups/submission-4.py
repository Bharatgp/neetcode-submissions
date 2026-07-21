class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_map = defaultdict(list)

        for anagram in strs:
            key = tuple(sorted(anagram))

            if key not in anagram_map:
                anagram_map[key]=[]
            anagram_map[key].append(anagram)
        
        return list(anagram_map.values())

        