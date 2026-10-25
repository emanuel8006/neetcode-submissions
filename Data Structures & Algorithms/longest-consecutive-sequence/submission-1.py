from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums) 
        # We convert our initial array into a set for O(1) lookup, O(n) space
        longest = 0

        for num in nums:
            if (num-1) not in numSet: # If not, then we know its the start of a consec
                length = 0
                # Check if we can find the consec num in our set
                while (num + length) in numSet:
                    length += 1
                longest = max(longest, length) # compare curr length to prev recorded longest
        return longest
