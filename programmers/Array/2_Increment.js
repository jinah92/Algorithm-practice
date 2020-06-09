function solution(x, n) {
  var answer = [];
  for (let i = 0; i < n; i++) {
    answer.push(x + i * x);
  }
  return answer;
}

solution(2, 5);
