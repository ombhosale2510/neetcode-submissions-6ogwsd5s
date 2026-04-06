class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = defaultdict(list)


        # ["act","pots","tops","cat","stop","hat"]
        for word in strs:
            count = [0]*26
            for char in word:
                count[ord('z')-ord(char)]+=1
            anagram_groups[tuple(count)].append(word)
        return list(anagram_groups.values())