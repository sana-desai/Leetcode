# [1,2,5,9] target= 6

def TwoSum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if j == len(nums) - 1:
                target_sum = nums[i]
            else:
                target_sum = nums[i] + nums[j+1]
                
            if target_sum == target:
                print([nums[i], nums[j+1]])
                return [i, j+1]
num1 =[1,2,3,6]
TwoSum(num1,4)

