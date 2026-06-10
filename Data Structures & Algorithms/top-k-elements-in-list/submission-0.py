class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen={}
        res=[]
        for i in nums:
            seen[i]=seen.get(i,0) +1
        itr = sorted(seen.items(),key=lambda x:x[1],reverse=True)
        for i in range(k):
            res.append(itr[i][0])
        return res
