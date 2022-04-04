/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function (nums) {
  let cnt = 0;

  while (nums.includes(0)) {
    nums.forEach((num, i) => {
      if (num === 0) {
        cnt++;
        nums.splice(i, 1);
      }
    });
  }

  for (let i = 0; i < cnt; i++) nums.push(0);
};
