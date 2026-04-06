class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        mark where the split is, plus say how many letters so 
        incase the str alwready has # we wont have an edge case
        """
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            # get the number
            j = i
            while s[j] != '#':
                j+=1
            length = int(s[i:j])
            # skip over the #, get the string of letters
            i = j + 1
            j = i + length
            res.append(s[i:j])
            # reset for the next word
            i = j
        return res