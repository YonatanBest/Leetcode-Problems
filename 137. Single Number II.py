nums = [2,2,3,2]
def singleNumber(nums):
        """ The code starts here."""
        nums.sort()
        i = 0
        while i < len(nums):
                if nums.count(nums[i]) == 1:
                    return nums[i]
                i += nums.count(nums[i])
        """ The code ends here."""
print(singleNumber(nums))