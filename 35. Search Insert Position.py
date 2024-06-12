nums = [1,3,5,6]
target = 5
def searchInsert(nums, target):
        """ The code starts here."""
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (r + l)//2
            if nums[mid] < target:
                l = mid +1
            elif nums[mid] > target:
                r = mid -1
            else:
                return mid
        return l
        """ The code ends here."""
print(searchInsert(nums,target))