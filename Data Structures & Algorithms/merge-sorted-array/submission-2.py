class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ptr1, ptr2 = 0, 0

        while ptr1 < m and ptr2 < n:
            if nums2[ptr2] <= nums1[ptr1]:
                nums1.insert(ptr1, nums2[ptr2])
                ptr2 += 1
            else:
                ptr1 += 1

        while ptr2 < n:
            nums1[ptr1] = nums2[ptr2]
            ptr1 += 1
            ptr2 += 1

        print(nums1)
        while len(nums1) > m + n:
            del nums1[-1]
        
        print(nums1)