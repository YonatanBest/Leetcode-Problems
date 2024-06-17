nums = [4,2,3]
def checkPossibility(nums):
        """ The code starts here."""
        count = 0
        c = 0
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                count += 1
                if len(nums) - 1 >= i + 1 and nums[i - 1] < nums[i + 1] or i == len(nums) - 1:
                    c = i
                else:
                    c = i - 1
        if count > 1:
            return False
        if len(nums) - 1 == c:
            nums[c] = nums[c - 1]
        else:
            nums[c] = nums[c + 1]
        if nums != sorted(nums):
            return False
        return True
        """ The code ends here."""
print(checkPossibility(nums))