/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function (nums) {
  let lastNum = -101;
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] === lastNum) {
      nums.splice(i, 1);
      i -= 1;
      continue;
    }
    lastNum = nums[i];
  }
  return nums.length;
};
