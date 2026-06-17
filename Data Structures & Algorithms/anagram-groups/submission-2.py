class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen={}
        for i in strs:
            new_key=tuple(sorted(i))
            if new_key in seen:
                seen[new_key].append(i)
            else:
                seen[new_key]=[i]
        return list(seen.values())