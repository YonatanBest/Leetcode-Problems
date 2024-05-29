nums = [-1,0,3,5,9,12]
target = 9
def search(nums, target):
        """ The code starts here."""
        min = 0
        max = len(nums) - 1
        while min <= max:
            mid = (max + min)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                max = mid - 1
            else:
                min = mid + 1
        return -1
        """ The code ends here."""
print(search(nums, target))