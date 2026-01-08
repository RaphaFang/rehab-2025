class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        holder = []
        time = len(nums) - (k % len(nums))

        if time > 0:
            nums.reverse()

            while time:
                holder.append(nums.pop())
                time -=1
            nums.reverse()
            nums.extend(holder)

# time 0ms 100%, yabe