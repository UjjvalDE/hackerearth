def count_pairs(nums, k):
    count = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if (nums[i] + nums[j]) % k == 0:
                count += 1
    return count