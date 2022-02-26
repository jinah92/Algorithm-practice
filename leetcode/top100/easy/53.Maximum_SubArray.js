/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function (nums) {
  nums.forEach((num, idx) => {
    if (nums[idx - 1] > 0) nums[idx] += nums[idx - 1];
  });
  return Math.max(...nums);
};
