function solution(numbers) {
  let answer = [],
    sum = 0;

  for (let nums of getCombinations(numbers, 2)) {
    sum = nums[0] + nums[1];
    if (!answer.find((v) => v == sum)) answer.push(sum);
  }

  return answer
    .filter((val, idx) => {
      return answer.indexOf(val) === idx;
    })
    .sort((a, b) => a - b);
}

function getCombinations(nums, selectNumber) {
  const results = [];
  if (selectNumber === 1) {
    return nums.map((el) => [el]);
  }

  nums.forEach((fixed, index, array) => {
    const restArray = array.slice(index + 1);
    const combinations = getCombinations(restArray, selectNumber - 1);
    const attachedArray = combinations.map((el) => [fixed, ...el]);

    results.push(...attachedArray);
  });

  return results;
}
