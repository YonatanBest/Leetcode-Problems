nums = [3,1,-2,-5,2,-4]
def rearrangeArray(nums):
        """ The code starts here."""
        new = []*len(nums)
        i = 0
        j = 1
        for num in nums:
            if num > 0:
                new.insert(i, num)
                i+=2
            else:
                new.insert(j, num)
                j+=2
        return new
        """ The code ends here."""
print(rearrangeArray(nums))