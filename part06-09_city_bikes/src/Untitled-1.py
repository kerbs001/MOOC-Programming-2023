def twoSum(nums, target):
    output = []

    for i in nums:
        for j in nums:
            if nums.index(i) == nums.index(j):
                continue
            if i - j == target:
                output.append(nums.index(i))
                output.append(nums.index(j))
       
    return(output)
    
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(twoSum(nums, target))