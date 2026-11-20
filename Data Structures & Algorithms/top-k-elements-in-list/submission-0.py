import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}

        for n in nums:
            if n in freq_dict:
                freq_dict[n] += 1
            else:
                freq_dict[n] = 1

        my_heap = []

        for n,f in freq_dict.items():

            if len(my_heap) >= k:
                if f > my_heap[0][0]:
                    heapq.heappop(my_heap)
                else:
                    continue
            heapq.heappush(my_heap, (f,n))

        return [my_heap[n][1] for n in range(len(my_heap))]
        