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
        left, right = 0, 0

        target = defaultdict(int)
        for i in range(len(t)):
            target[t[i]] = 1 + target.get(t[i], 0)
        
        counter = len(t)
        min_len = float('inf')
        start = 0

        while right < len(s):
            if target[s[right]] > 0:
                counter -= 1
            target[s[right]] -= 1
            right += 1

            while counter == 0:
                # valid window is found
                if right - left < min_len:
                    min_len = right-left
                    start = left
                
                target[s[left]] += 1
                if target[s[left]] > 0:
                    counter += 1
                left+=1
        return "" if min_len == float('inf') else s[start:start+min_len]