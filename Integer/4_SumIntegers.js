function solution(a, b) {
  let answer = 0;
  let start = 0;
  let end = 0;
  if (a < b) {
    start = a;
    end = b;
  } else {
    start = b;
    end = a;
  }
  for (let i = start; i <= end; i++) {
    answer += i;
  }
  return answer;
}

console.log(solution(3, 5));
