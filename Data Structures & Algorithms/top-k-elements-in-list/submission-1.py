class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen={}
        res=[]
        for i in nums:
            seen[i]=seen.get(i,0)+1
        itrsort=sorted(seen.items(),key=lambda x:x[1],reverse=True)
        print(itrsort)
        for i in range(k):
            res.append(itrsort[i][0])
        return res
