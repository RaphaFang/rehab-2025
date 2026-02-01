class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        last_i = len(nums)-1
        switch = False
        temp = 0
        rr = []

        for i, n in enumerate(nums):
            if i != last_i:
                if (n + 1) == nums[i+1]:
                    if switch == False:
                        temp = n
                    switch = True
                else:
                    if switch == True:
                        rr.append(f"{temp}->{n}")
                        switch = False
                    else:
                        rr.append(f"{n}")
            else:
                if switch == True:
                    rr.append(f"{temp}->{n}")
                    switch = False
                else:
                    rr.append(f"{n}")

        return rr
