# Python DSA Practice Problems

Each problem has a matching starter file in its topic folder, named by problem number.

## Lists and strings (easy)

Folder: `01_lists_strings/`

1. Reverse a list without using `reverse()` or slicing.

    Example:
    - Input: `[1, 2, 3, 4]` → Output: `[4, 3, 2, 1]`

2. Find the second largest number in a list.

    Example:
    - Input: `[10, 5, 20, 8]` → Output: `10`

3. Remove duplicates from a list while keeping the original order.

    Example:
    - Input: `[1, 2, 2, 3, 1, 4]` → Output: `[1, 2, 3, 4]`

4. Move all zeros to the end, keeping the order of other elements.

    Example:
    - Input: `[0, 1, 0, 3, 12]` → Output: `[1, 3, 12, 0, 0]`

5. Check if a string is a palindrome (ignore case and spaces).

    Example:
    - Input: `"A man a plan a canal Panama"` → Output: `True`
    - Input: `"hello"` → Output: `False`

6. Reverse the words in a sentence: `"I love AI"` becomes `"AI love I"`.

    Example:
    - Input: `"I love AI"` → Output: `"AI love I"`

7. Find the missing number in a list of 1 to n.

    Example:
    - Input: `[1, 2, 4, 5], n = 5` → Output: `3`

8. Rotate a list by k positions.

    Example:
    - Input: `[1, 2, 3, 4, 5], k = 2` → Output: `[4, 5, 1, 2, 3]`

9. Flatten a nested list one level deep: `[[1,2],[3],[4,5]]`.

    Example:
    - Input: `[[1, 2], [3], [4, 5]]` → Output: `[1, 2, 3, 4, 5]`

10. Find common elements between two lists.

    Example:
    - Input: `[1, 2, 3, 4], [3, 4, 5, 6]` → Output: `[3, 4]`

## Dictionary and Counter (easy to medium)

Folder: `02_dict_counter/`

11. Count the frequency of each character in a string.

    Example:
    - Input: `"banana"` → Output: `{'b': 1, 'a': 3, 'n': 2}`

12. Find the first non-repeating character in a string.

    Example:
    - Input: `"swiss"` → Output: `"w"`
    - Input: `"aabb"` → Output: `None`

13. Check if two strings are anagrams.

    Example:
    - Input: `"listen", "silent"` → Output: `True`
    - Input: `"abc", "abd"` → Output: `False`

14. Two Sum: return indices of two numbers that add up to a target.

    Example:
    - Input: `nums = [2, 7, 11, 15], target = 9` → Output: `[0, 1]`

15. Group anagrams: `["eat","tea","tan","ate","nat"]`.

    Example:
    - Input: `["eat", "tea", "tan", "ate", "nat"]` → Output: `[["eat", "tea", "ate"], ["tan", "nat"]]`

16. Top K frequent elements in a list.

    Example:
    - Input: `[1, 1, 1, 2, 2, 3], k = 2` → Output: `[1, 2]`

17. Find the most frequent word in a paragraph, ignoring punctuation and case.

    Example:
    - Input: `"The cat and the hat. The end!"` → Output: `"the"`

18. Invert a dictionary (values become keys); handle duplicate values by grouping keys in a list.

    Example:
    - Input: `{'a': 1, 'b': 2, 'c': 1}` → Output: `{1: ['a', 'c'], 2: ['b']}`

19. Merge two dicts, summing values for common keys.

    Example:
    - Input: `{'a': 1, 'b': 2}, {'b': 3, 'c': 4}` → Output: `{'a': 1, 'b': 5, 'c': 4}`

20. Given a list of dicts (employees with name, dept, salary), group names by department.

    Example:
    - Input: `[{'name': 'Ann', 'dept': 'IT', 'salary': 50}, {'name': 'Bob', 'dept': 'HR', 'salary': 40}, {'name': 'Cy', 'dept': 'IT', 'salary': 60}]` → Output: `{'IT': ['Ann', 'Cy'], 'HR': ['Bob']}`

## Sorting and lambda (easy to medium)

Folder: `03_sorting_lambda/`

21. Sort a list of tuples by the second element.

    Example:
    - Input: `[(1, 'c'), (2, 'a'), (3, 'b')]` → Output: `[(2, 'a'), (3, 'b'), (1, 'c')]`

22. Sort words by length, then alphabetically.

    Example:
    - Input: `["pear", "fig", "apple", "kiwi"]` → Output: `["fig", "kiwi", "pear", "apple"]`

23. Sort a list of dicts by age descending, then name ascending.

    Example:
    - Input: `[{'name': 'Bob', 'age': 25}, {'name': 'Ann', 'age': 30}, {'name': 'Al', 'age': 25}]` → Output: `[{'name': 'Ann', 'age': 30}, {'name': 'Al', 'age': 25}, {'name': 'Bob', 'age': 25}]`

24. Merge overlapping intervals: `[[1,3],[2,6],[8,10]]`.

    Example:
    - Input: `[[1, 3], [2, 6], [8, 10]]` → Output: `[[1, 6], [8, 10]]`

## Recursion (easy to medium)

Folder: `04_recursion/`

25. Factorial, recursive and iterative.

    Example:
    - Input: `5` → Output: `120`
    - Input: `0` → Output: `1`

26. Fibonacci, plain recursion then with `lru_cache`, and explain the time difference.

    Example:
    - Input: `n = 10` → Output: `55`

27. Fully flatten a deeply nested list: `[1,[2,[3,[4]]]]`.

    Example:
    - Input: `[1, [2, [3, [4]]]]` → Output: `[1, 2, 3, 4]`

28. Sum of digits of a number using recursion.

    Example:
    - Input: `493` → Output: `16`

29. Generate all permutations of a string.

    Example:
    - Input: `"abc"` → Output: `["abc", "acb", "bac", "bca", "cab", "cba"]`

30. Generate all subsets of a list.

    Example:
    - Input: `[1, 2, 3]` → Output: `[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]`

## Stack, sliding window, two pointers (medium)

Folder: `05_stack_window_pointers/`

31. Valid parentheses: `"({[]})"` is valid, `"(]"` is not.

    Example:
    - Input: `"({[]})"` → Output: `True`
    - Input: `"(]"` → Output: `False`

32. Longest substring without repeating characters.

    Example:
    - Input: `"abcabcbb"` → Output: 3  (substring "abc")

33. Maximum sum subarray of size k.

    Example:
    - Input: `[2, 1, 5, 1, 3, 2], k = 3` → Output: `9`

34. Check if a list is sorted, then find a pair summing to a target in a sorted list using two pointers.

    Example:
    - Input: `[1, 2, 5, 9] (is sorted?)` → Output: `True`
    - Input: `[1, 2, 4, 7, 11], target = 9` → Output: (2, 7)  or indices (1, 3)

## Decorators and practical Python (medium, common in GenAI roles)

Folder: `06_decorators_practical/`

35. Write a `@timer` decorator that prints execution time.

    Example:
    - Input: `@timer on a function that sleeps 1 second` → Output: prints something like: slow_func took 1.0012s

36. Write a `@retry(times=3)` decorator for a function that sometimes raises an exception.

    Example:
    - Input: `@retry(times=3) on a function that fails twice, then succeeds` → Output: returns the result on the 3rd attempt
    - Input: `same function failing every time` → Output: raises the last exception after 3 attempts

37. Write a decorator that caches results of a function (your own simple memoize).

    Example:
    - Input: `calling a memoized slow_square(4) twice` → Output: 1st call computes 16, 2nd call returns 16 from the cache

38. Implement an LRU cache class with `get` and `put`.

    Example:
    - Input: `cache = LRUCache(2); put(1, 1); put(2, 2); get(1); put(3, 3); get(2); get(3)` → Output: `get(1) -> 1, get(2) -> -1 (evicted), get(3) -> 3`

39. Read a JSON file of records, filter by a condition, and write the result to a new file with error handling.

    Example:
    - Input: `users.json: [{'name': 'Ann', 'age': 30}, {'name': 'Bob', 'age': 17}], condition age >= 18` → Output: `adults.json: [{'name': 'Ann', 'age': 30}]`
    - Input: `missing or invalid JSON file` → Output: prints a clear error message instead of crashing

40. Call 3 mock async APIs concurrently with `asyncio.gather` and collect the results.

    Example:
    - Input: `3 mock APIs that each sleep 1 second and return 'A', 'B', 'C'` → Output: `['A', 'B', 'C'] in about 1 second total (not 3)`

## Extra practice (easy to medium)

Folder: `07_extra_practice/`

41. Binary search: given a sorted list and a target, return the index of the target or -1. Then modify it to return the *first* occurrence when the target appears multiple times: `[1,2,2,2,3]`, target 2 returns 1.

    Example:
    - Input: `[1, 2, 3, 4, 5], target = 4` → Output: `3`
    - Input: `[1, 2, 3], target = 9` → Output: `-1`
    - Input: `[1, 2, 2, 2, 3], target = 2 (first occurrence)` → Output: `1`

42. Write a `BankAccount` class with `deposit`, `withdraw` and `get_balance`. Reject negative amounts, prevent overdrawing with a clear error, and keep a transaction history. Add a `__repr__` for readable printing.

    Example:
    - Input: `acct = BankAccount(); acct.deposit(100); acct.withdraw(30); acct.get_balance()` → Output: `70`
    - Input: `acct.withdraw(500)` → Output: raises an error: insufficient funds
    - Input: `acct.deposit(-5)` → Output: raises an error: amount must be positive

43. First, transpose a matrix (`[[1,2,3],[4,5,6]]` becomes `[[1,4],[2,5],[3,6]]`). Then count the number of islands in a grid of 0s and 1s, where an island is connected 1s going up, down, left or right.

    Example:
    - Input: `[[1, 2, 3], [4, 5, 6]] (transpose)` → Output: `[[1, 4], [2, 5], [3, 6]]`
    - Input: `[[1, 1, 0, 0], [1, 0, 0, 1], [0, 0, 1, 1]] (islands)` → Output: `2`

