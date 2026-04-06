class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = Counter(t)

        if len(s)!=len(t):
            return False
        for char in s:
            if char not in letters or letters[char]==0:
                return False
            else:
                letters[char]-=1
        return True