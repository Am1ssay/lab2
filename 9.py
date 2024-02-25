def pown(nums):
    a = list()
    for i in range(0, len(nums)):
        a.append(int(nums[i])**2)
    return a


print("Enter some numbers: ", end="")
numbers = input().split()
print("This are quadz: ", pown(numbers))
