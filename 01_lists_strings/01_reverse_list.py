"""Problem 1

Reverse a list without using `reverse()`.

Example:
Input:  [1, 2, 3, 4]
Output: [4, 3, 2, 1]
"""


# Write your solution below

#1 reverse()
def reverse_list(lst):
    return list(reversed(lst))


#2 slicing
def reverse_list(lst):
    lst = lst[::-1]
    return lst

#3 brutforce
def reverse_list(lst):
    n = len(lst)-1
    out= []
    for i in range(n,-1,-1):
        out.append(lst[i])
    return out

#4 O(1) extra space
def reverse_list(lst):
    left = 0
    right = len(lst)-1

    while left<right:
        lst[left], lst[right] = lst[right], lst[left]
        left +=1
        right -=1
    return lst

if __name__ == "__main__":
    print(reverse_list([1, 2, 3, 4]))
