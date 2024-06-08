nums = [2,2,1]
def singleNumber(nums):
        nums.sort()
        i = 0
        while i < len(nums):
                if nums.count(nums[i]) == 1:
                    return nums[i]
                i += nums.count(nums[i])
print(singleNumber(nums))