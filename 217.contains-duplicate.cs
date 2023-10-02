/*
 * @lc app=leetcode id=217 lang=csharp
 *
 * [217] Contains Duplicate
 */

// @lc code=start
public class Solution
{
    public bool ContainsDuplicate(int[] nums)
    {
        for (int i = 0; i < nums.Length; i++)
        {
            for (int j = i + 1; j < nums.Length; j++)
            {
                if (nums[i] == nums[j])
                    return true;
            }
        }
        
        return false;
    }
}
// @lc code=end
