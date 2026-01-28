import heapq
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        ll = len(citations)
        heapq.heapify(citations)
        for i in range(ll):
            temp = heapq.heappop(citations)
            if temp >= ll -i:
                return ll -i
        return 0