class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramsHashMap = defaultdict(list)

        for word in strs:
            count = [0] * 26   #c reate an array that has 26, zero spots

            for char in word:
                count[ord(char) - ord("a")] += 1    # completing through str we will make the freq vector

            anagramsHashMap[tuple(count)].append(word)  # list are mutable so need to convert to tuple
        
        return list(anagramsHashMap.values())