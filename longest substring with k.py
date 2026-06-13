def get_longest_substr(arr,k):
    max_len = 0
    new_len = 0
    curr_sum = 0
    start, end = -1, -1
    curr_map={}
    for i in range(len(arr)):
        curr_sum +=arr[i]
        if curr_sum == k:
            max_len = i+1
            start = 0
            end = i
        if curr_sum-k in curr_map:
            new_len = i-curr_map[curr_sum-k]
            if new_len>max_len:
                max_len = new_len
                start = curr_map[curr_sum-k]+1
                end = i
        if curr_sum not in curr_map:
            curr_map[curr_sum]=i
    if start!=-1:
        return arr[start:end+1]
    return []
 
arr = [10, 5, 2, 7, 1, 9]  
k=15    
r = get_longest_substr(arr, k)
print(r)
print(len(r))
