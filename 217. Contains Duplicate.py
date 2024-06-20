nums = [1,2,3,1]
def containsDuplicate(nums):
        """ The code starts here."""
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                return True
        return False
        """ The code ends here."""
print(containsDuplicate(nums))