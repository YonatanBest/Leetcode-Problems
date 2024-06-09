nums = [1,2,3,1]
def findPeakElement(nums):
    """ The code starts here."""
    l = 0
    r = len(nums) - 1
    currentMax = 0
    while l <= r:
        if nums[l] >= nums[r]:
            currentMax = l
            r -= 1
        elif nums[l] < nums[r]:
            currentMax = r
            l += 1
    return currentMax
    """ The code ends here."""
print(findPeakElement(nums))