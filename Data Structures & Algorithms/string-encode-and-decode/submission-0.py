class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s)) + "#" + s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        i=0
        decoded=[]
        while i<len(s):
            num=""
            while s[i]!="#":
                num = num+s[i]
                i=i+1
            start = i + 1
            end = start + int(num)
            decoded.append(s[start:end])
            i = start + int(num)
        return decoded
            