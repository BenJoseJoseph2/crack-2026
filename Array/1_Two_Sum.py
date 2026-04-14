nums = [1,6,5,78,456]
target = 461


def two_sum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]


print(two_sum(nums,target))