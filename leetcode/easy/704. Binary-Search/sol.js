/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */

var search = function (nums, target) {
  let start = 0;
  let end = nums.length - 1;
  let middle = 0;

  while (start < end) {
    middle = parseInt((start + end) / 2);

    if (nums[middle] === target) {
      return middle;
    }
    if (nums[middle] > target) {
      end = middle - 1;
    } else {
      start = middle + 1;
    }
  }

  middle = parseInt((start + end) / 2);

  return nums[middle] === target ? middle : -1;
};
