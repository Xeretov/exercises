# The Number of Beautiful Subsets: write a function with an array nums of positive integers and a positive integer k given as inputs.
# A subset of nums is beautiful if it does not contain two integers with an absolute difference equal to k.
# Return the number of non-empty beautiful subsets of the array nums.
# A subset of nums is an array that can be obtained by deleting some (possibly none) elements from nums.
# Two subsets are different if and only if the chosen indices to delete are different.

def is_beautiful(nums: list, k: int) -> int:
    def backtrack(start, current_subset):
        nonlocal count
        if current_subset:
            count += 1
        
        for i in range(start, len(nums)):
            can_add = True
            for num in current_subset:
                if abs(num - nums[i]) == k:
                    can_add = False
                    break
                    
            if can_add:
                current_subset.append(nums[i])
                backtrack(i + 1, current_subset)
                current_subset.pop()
    
    nums.sort()
    count = 0
    backtrack(0, [])
    return count

print(is_beautiful([4,2,5,9,10,3],k=1))

# Combinations: given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
#  You may return the answer in any order.

# Example 1:
# Input: n = 4, k = 2
# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

# Example 2:
# Input: n = 1, k = 1
# Output: [[1]]


# Generate Parentheses: Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

# Example 2:
# Input: n = 1
# Output: ["()"]
