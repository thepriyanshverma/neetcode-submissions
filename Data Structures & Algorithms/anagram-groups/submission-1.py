class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen={}
        for i in strs:
            a_key=tuple(sorted(i))
            # a_key="".join(a)
            if a_key in seen:
                seen[a_key].append(i)
            else:
                seen[a_key]=[i]
        return list(seen.values())