class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26    # freq vector by a-z

            for character in s: # go through every character and to update 
                count[ord(character) - ord("a")] += 1

            res[tuple(count)].append(s)

        return list(res.values())