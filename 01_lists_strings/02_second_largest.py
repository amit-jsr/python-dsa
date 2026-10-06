"""Problem 2

Find the second largest number in a list.

Example:
Input:  [10, 5, 20, 8]
Output: 10
"""


# Write your solution below

# Built-in sorted()
def second_largest_builtin(nums):
    # nums.sort(reverse = True)
    nums = sorted(nums, reverse=True)
    return nums[1]
    
# O(1) extra space
def second_largest(nums):
    min_1 = min_2 = nums[0]
    for num in nums:
        print(num)
        if num<min_1:
            min_2 = min_1
            min_1 = num
        elif num>min_1 and num<min_2:
            min_2 = num
        else:
            pass
    return min_1,min_2


if __name__ == "__main__":
    nums = [4,1,2,3,-1,-9,6,7]
    print(second_largest(nums))