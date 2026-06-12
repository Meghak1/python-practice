nums = [1,2,3,4,5,6]

is_sorted = True

for i in range(len(nums)-1):
    if nums[i] > nums[i+1]:
        is_sorted = False
        break

print(is_sorted)
