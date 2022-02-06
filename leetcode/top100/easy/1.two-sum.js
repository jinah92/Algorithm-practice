/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  let hashMap = {};
  for (let i = 0; i < nums.length; i++) {
    if (hashMap.hasOwnProperty(target - nums[i])) {
      return [hashMap[target - nums[i]], i];
    }
    hashMap[nums[i]] = i;
  }
};

let nums = [0, 4, 3, 0];
let target = 0;

const result = twoSum(nums, target);
console.log(result);
