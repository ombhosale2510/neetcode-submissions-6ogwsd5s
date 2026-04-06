class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        in s, t: count of chars must be same

        s and t: len(s) != len(t): return False
        Counter(s) Counter(t): each char if their values 
        are not equal return False

        
        
        """

        if len(s) != len(t):
            return False
        
        letters_of_s = Counter(s)

        for char in t:
            if char not in letters_of_s or letters_of_s[char] == 0:
                return False
            else:
                letters_of_s[char]-=1
        return True