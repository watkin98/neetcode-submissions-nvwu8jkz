class MinHeap:
    
    def __init__(self):
        self.heap = []
        self.size = 0

    def push(self, val: int) -> None:
        self.heap.append(val)
        self.size += 1
        
        i = self.size - 1
        while i > 0:
            parent = (i - 1) // 2

            if self.heap[parent] <= self.heap[i]:
                break

            self.heap[parent], self.heap[i] = (
                self.heap[i],
                self.heap[parent],
            )
            i = parent

    def pop(self) -> int:
        if self.size == 0:
            return -1

        res = self.heap[0]
        last = self.heap.pop()
        self.size -= 1

        if self.size > 0:
            self.heap[0] = last
            self.minHeapify(0)

        return res


    def top(self) -> int:
        return self.heap[0] if self.size != 0 else -1

    def heapify(self, nums: List[int]) -> None:
        self.heap = nums.copy()
        self.size = len(nums)

        self.buildMinHeap()
    
    def buildMinHeap(self):
        for i in range(self.size // 2 - 1, - 1, -1):
            self.minHeapify(i)

    def minHeapify(self, i):
        l = (2 * i) + 1
        r = (2 * i) + 2

        smallest = i
        if l < len(self.heap) and self.heap[l] < self.heap[smallest]:
            smallest = l
        if r < len(self.heap) and self.heap[r] < self.heap[smallest]:
            smallest = r

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.minHeapify(smallest)

