function solution(arr) {
  return arr.reduce((a, b) => a + b) / arr.length;
}

const test = solution([1, 2, 3, 4, 5]);
console.log(test);
