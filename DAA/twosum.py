def find_two_sum_indices(nums, target):
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return sorted([num_to_index[complement] + 1, i + 1])
        num_to_index[num] = i

n = int(input())
nums = list(map(int, input().split()))
target = int(input())
result = find_two_sum_indices(nums, target)
if result:
    print(result[0], result[1])
else:
    print("No two sum solution found")
