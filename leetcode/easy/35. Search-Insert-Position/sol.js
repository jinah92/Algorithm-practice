var searchInsert = function (nums, target) {
  let start = 0,
    end = nums.length - 1;
  let middle = 0;
  while (start <= end) {
    middle = parseInt((start + end) / 2);
    if (nums[middle] === target) return middle;

    if (nums[middle] < target) {
      start = middle + 1;
    } else {
      end = middle - 1;
    }
  }
  return nums[middle] > target ? middle : middle + 1;
};
