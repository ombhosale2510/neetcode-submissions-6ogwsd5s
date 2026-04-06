class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        # given s and t, find window in s such that all t char are in s
        minimize the window, such that return is min_len of possible window

        # 
        sliding window
        counter of t chars: int
        target = Counter(t)
        run through the s string, such that counter -= 1 when char matches t char

        left, right 0
        min_leng = inf

        window:
        keep increasing the window size if cur window does not have all the t chars
        once it does, counter == 0
        calc min lenght, update start index
        shrink the window, until its t char
        
        """

        left, right = 0, 0 # start window from left
        target = defaultdict(int)
        for i in range(len(t)):
            target[t[i]] = 1 + target.get(t[i], 0)
        counter = len(t)
        start = 0 # index
        min_len = float('inf')
        
        while right < len(s):
            # 1. make window contain all t chars
            if target[s[right]] > 0:
                counter -= 1
            target[s[right]] -= 1
            right += 1 #inc window

            while counter == 0:
                # 2. check min length
                if right - left < min_len:
                    min_len = right-left
                    start = left
                
                # shrink window
                target[s[left]] += 1
                if target[s[left]] > 0:
                    counter += 1 # we need this back
                left += 1 
        return "" if min_len == float('inf') else s[start:start+min_len]