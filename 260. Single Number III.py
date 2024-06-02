nums = [1,2,1,3,2,5]
def singleNumber(nums):
    """ The code starts here."""
    nums.sort()
    i = 0
    arr = []
    while i < len(nums):
            if nums.count(nums[i]) == 1:
                arr.append(nums[i])
            i += nums.count(nums[i])
    return arr
    """ The code ends here."""
print(singleNumber(nums))