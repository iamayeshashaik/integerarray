def Pair_of_integer (nums, sum):
     
    for i in range(len(nums) - 1):
 
        for j in range(i + 1, len(nums)):

                if nums[i] + nums[j] == sum:
                    print('Pair of integer is : ', (nums[i], nums[j]))
                    return
    print('pair of integers not found')
 
if __name__ == '__main__':
 
    nums = [5,7,3,9,8,1,2,4]
    sum = 10
Pair_of_integer (nums, sum)