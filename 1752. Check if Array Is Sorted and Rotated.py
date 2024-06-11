nums = [3,4,5,1,2]
def check(nums):
        """ The code starts here."""
        nums_new = sorted(nums)
        for i in range(len(nums)):
            num = nums_new[i:] + nums_new[:i]
            if num == nums:
                return True
        return False
        """ The code ends here."""
print(check(nums))