class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            curr = numbers[l] + numbers[r]
            # We check for the following cases:
            # CASE 1: the current two indexes sum to be the target -> return this solution
            if (curr == target):
                return [l+1, r+1]
            # CASE 2: if curr < target, we move our l pointer right (+1)
            elif (curr < target):
                l += 1
                continue
            # CASE 3: if curr > target, we move our r pointer left (-1)
            else:
                r -= 1
        return []
            