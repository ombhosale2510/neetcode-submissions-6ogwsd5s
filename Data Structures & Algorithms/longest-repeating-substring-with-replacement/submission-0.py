class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        # 
        given s:string, k:int
        max window len, with same characters
        we are allowed to do k replacements to match most freq characters

        only makes sense to make sure window_size - most_freq <= k
        to make k changes inside window and get max_len



        """

        freq = defaultdict(int)
        left, right = 0, 0
        max_count = 0
        max_len = 0

        while right < len(s):
            freq[s[right]] += 1
            max_count = max(max_count, freq[s[right]])

            if (right-left+1) - max_count > k:
                freq[s[left]] -= 1
                left+=1
            max_len = max(max_len, right-left+1)
            right += 1
        return max_len