import heapq
def kth(arr,k):
    heap = arr[:k]
    heapq.heapify(heap)

    for i in arr[k:]:
        if i>heap[0]:
            heapq.heappushpop(heap,i)
    
    return heap[0]

print(kth([3,2,3,1,2,4,5,5,6] , 4))
    
    
