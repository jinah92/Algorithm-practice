function solution(numbers, target) {
  let answer = dfs(0, numbers, target);
  return answer;

  function dfs(startIndex, numbers, target) {
    return (function dfsRecursive(num, index) {
      if (index === numbers.length) {
        if (num === target) {
          return 1;
        } else {
          return 0;
        }
      }
      let num1 = num + numbers[index];
      let num2 = num - numbers[index];

      return dfsRecursive(num1, index + 1) + dfsRecursive(num2, index + 1);
    })(0, startIndex);
  }
}

const numbers = [1, 1, 1, 1, 1];
const target = 3;

solution(numbers, target);
