function solution(arr1, arr2) {
  var answer = [[], []];

  for (let i in arr1[0]) {
    for (let j in arr1[1]) {
      answer[i][j] = arr1[i][j] + arr2[i][j];
    }
  }
  return answer;
}

const result = solution([[1], [2]], [[3], [4]]);

console.log(result);
