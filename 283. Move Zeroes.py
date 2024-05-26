nums = [0,1,0,3,12]
def moveZeroes(nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        """ The code starts here."""
        x = 0
        arr = []
        for i in range(len(nums)):
            if nums[i] == 0:
                x += 1
                nums.insert(len(nums), 0)
        for j in range(0, len(nums)-x):
            if nums[j] == 0:
                arr.append(j)
        m = 0
        for r in arr:
            nums.pop(r-m)
            m +=1
        """ The code ends here."""
        return nums
print(moveZeroes(nums))
