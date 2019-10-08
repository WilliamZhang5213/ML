'''
二维有序数组：由左向右，由上至下，依次增大
'''
def find(nums,target):
    startrow = 0
    row = len(nums)-1
    col = len(nums[0])-1
    while startrow <= row and col>=0:
        if nums[startrow][col] == target:
            return True
        elif nums[startrow][col] > target:
            col-=1
        elif nums[startrow][col] < target:
            startrow+=1
    return False


nums = [[1,4,7],
        [2,5,8],
        [3,6,9]]
target = 9
print(find(nums,target))