class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashSet = set()
        left = 0
        cur_len = 0

        for right in range(len(s)):
            while s[right] in hashSet:
                hashSet.remove(s[left])
                left+=1
            hashSet.add(s[right])
            cur_len = max(cur_len, right-left+1)
        return cur_len