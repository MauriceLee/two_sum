def twoSum(nums, target):

    complements = {}

    for index, item in enumerate(nums):
        if item in complements:
            return[complements[item], index]
        else:
            complements[target - item] = index

    return[]

nums = [2, 7, 11, 15]
target = 9

solution = twoSum(nums, target)
print(solution)