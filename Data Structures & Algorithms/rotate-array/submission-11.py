class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        start_cycle = count = 0

        while count < len(nums):
            current_i = start_cycle
            prev_val = nums[current_i]

            while 1:
                next_i = (current_i + k) % len(nums)
                nums[next_i], prev_val = prev_val, nums[next_i]
                current_i = next_i
                count += 1

                if current_i == start_cycle:
                    break
            start_cycle += 1