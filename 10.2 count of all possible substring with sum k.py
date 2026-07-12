def allSubarrays(arr, k):
    result = []
    count = 0
    for i in range(len(arr)):
        total = 0

        for j in range(i, len(arr)):
            total += arr[j]

            if total == k:
                result.append(arr[i:j+1])
                count+=1

    return result, count


arr = [1, 2, 3, 2, 1]

print(allSubarrays(arr, 3))
