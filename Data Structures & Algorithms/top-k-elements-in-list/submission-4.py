class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dicts = {}
        for i in nums :
            if i not in dicts :
                dicts[i] = 1
            else:
                dicts[i] += 1
        dicts = dict(sorted(dicts.items(), key=lambda x: x[1], reverse=True))

        return list(dicts.keys())[:k]
                