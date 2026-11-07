class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = dict()

        for wrd in strs:

            sorted_wrd = ''.join(sorted(wrd))

            if sorted_wrd in result:
                result[sorted_wrd].append(wrd)
            else:
                result[sorted_wrd] = [wrd]

        return list(result.values())
        