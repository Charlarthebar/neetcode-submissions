class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list) # {[charCount], [list of anagrams]

        for string in strs:
            count = [0] * 26
            for ch in string:
                count[ord(ch)-ord('a')] += 1
            hmap[tuple(count)].append(string)
        return list(hmap.values())
