nums = [-1,0,1,2,-1,-4]
def threeSum(nums):
        """ The code starts here."""
        arr = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and  nums[i] == nums[i-1]:
                continue 
            l, r = i+1, len(nums) - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum < 0:
                    l += 1
                elif sum > 0:
                    r -= 1
                else:
                    arr.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return arr
        """ The code starts here."""
print(threeSum(nums))