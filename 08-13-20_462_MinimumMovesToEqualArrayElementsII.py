"""
This problem was all about knowing math. My first approach was using the mean, which didn't work for some test cases.
I then tried median, which didn't work for others. Lastly, I combined the two which worked. 

Stats:
Time: ~19 minutes
Runtime: 84 ms, faster than 58.19% of Python3 online submissions for Minimum Moves to Equal Array Elements II.
Memory Usage: 15 MB, less than 89.55% of Python3 online submissions for Minimum Moves to Equal Array Elements II.
"""

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        # Find median of nums and count difference between every element & median
        m = sorted(nums)
        move1 = 0
        if len(nums)%2 == 0:
            target = round((m[round(len(m)/2-1)] + m[round(len(m)/2)])/2)
        else:
            target = m[round(len(m)/2-1)]
        for num in nums:
            move1 += abs(target - num)
        # Find mean of nums and count difference between every element & mean 
        s = sum(nums)
        target = round(s / len(nums))
        move2 = 0
        for num in nums:
            move2 += abs(target - num)
        # Return the smaller result
        if move1> move2:
            return move2
        else:
            return move1
