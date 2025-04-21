class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Initialize an empty list to store the concatenated array
        ans = []
        
        # Get the length of the input array `nums`
        n = len(nums)
        
        # Create a new list `ans` with twice the length of `nums`, initialized to zeros
        ans = (n * 2) * [0]

        # Iterate through the original `nums` array
        for i, num in enumerate(nums):
            # Place each element of `nums` in the corresponding positions of `ans`
            ans[i] = num
            # Place each element of `nums` again in the positions after the first set in `ans`
            ans[i+n] = num

        # Return the concatenated array `ans`
        return ans
