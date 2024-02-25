def uniq_numbs(nums):
    a = list()
    for i in range(0, len(nums)):
        if numbers.count(nums[i]) == 1:
            a.append(nums[i])
    return a


print("Enter some numbers: ", end="")
numbers = input().split()
print("There are uniq numbers: ", uniq_numbs(numbers))
