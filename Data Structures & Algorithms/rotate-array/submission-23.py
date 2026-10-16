class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n

        start = count = 0
        while count < n:
            prev = nums[start]
            idx = start
            while True:
                nxt_idx = (idx + k) % n
                nums[nxt_idx], prev = prev, nums[nxt_idx]
                idx = nxt_idx
                count += 1

                if nxt_idx == start:
                    break
            start += 1 