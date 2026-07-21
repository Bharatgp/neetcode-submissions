class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        s3 = s2[::-1]
        return s2 == s3