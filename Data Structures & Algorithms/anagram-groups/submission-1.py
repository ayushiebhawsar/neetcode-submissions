class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)

        for wrd in strs:
            count = [0] * 26

            for c in wrd:
                count[ord(c) - ord('a')] += 1

            res[tuple(count)].append(wrd)

        return list(res.values())
        