nums = [1,6,5,78,456]
target = 461


def two_sum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]


print(two_sum(nums,target))


def two_sum_optimized(nums,target):
    seen = {}
    for idx,num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff],idx]
        seen[num] = idx


print(two_sum_optimized(nums,target))