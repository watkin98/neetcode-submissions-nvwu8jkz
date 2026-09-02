class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        start = count = 0

        while count < n:
            current_i = start
            prev = nums[current_i]

            while True:
                next_i = (current_i + k) % n
                nums[next_i], prev = prev, nums[next_i]
                current_i = next_i
                count += 1

                if current_i == start:
                    break
            start += 1