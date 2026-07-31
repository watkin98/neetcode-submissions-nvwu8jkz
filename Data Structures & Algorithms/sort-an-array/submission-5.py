class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums, 0, len(nums) - 1)
        return nums

    def mergeSort(self, nums, l, r):
        if l >= r:
            return

        m = (l + r) // 2
        self.mergeSort(nums, l, m)
        self.mergeSort(nums, m+1, r)
        self.merge(nums, l, m, r)

    def merge(self, nums, l, m, r):
        left = nums[l:m+1]
        right = nums[m+1:r+1]

        i, L, R = l, 0, 0

        while L < len(left) and R < len(right):
            if left[L] <= right[R]:
                nums[i] = left[L]
                L += 1
            else:
                nums[i] = right[R]
                R += 1
            i += 1

        while L < len(left):
            nums[i] = left[L]
            L += 1
            i += 1
        while R < len(right):
            nums[i] = right[R]
            R += 1
            i += 1
