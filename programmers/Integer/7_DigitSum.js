function solution(n) {
  let answer = 0;
  let number = n.toString();
  for (let i = 0; i < number.length; i++) {
    answer += Number(number[i]);
  }
  return answer;
}

solution(10);
