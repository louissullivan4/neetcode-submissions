class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hs = {}
        for word in strs:
            if str(sorted(word)) in hs.keys():
                hs[str(sorted(word))].append(word)
            else:
                hs[str(sorted(word))] = [word]
        return list(hs.values())

sol = Solution()
print(sol.groupAnagrams(["act","pots","tops","cat","stop","hat"]))