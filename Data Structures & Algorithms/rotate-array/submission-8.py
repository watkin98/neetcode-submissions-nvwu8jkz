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
            current = start

            while True:
                next_i = (current + k) % n
                nums[next_i], prev = prev, nums[next_i]
                current = next_i
                count += 1

                if current == start:
                    break

            start += 1