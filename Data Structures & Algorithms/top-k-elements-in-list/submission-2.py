import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i,0) + 1
        
        top_k = []

        for key, value in freq.items():
            if len(top_k) < k:
                heapq.heappush(top_k,(value,key))
            elif len(top_k) == k and value > top_k[0][0]:
                heapq.heappop(top_k)
                heapq.heappush(top_k,(value,key))
        result = [y for x,y in top_k]
        return result

        
