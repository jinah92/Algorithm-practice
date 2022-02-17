function solution(numbers) {
  let answer = numbers
    .sort((a, b) => b.toString() + a.toString() - (a.toString() + b.toString()))
    .reduce((a, b) => a.toString() + b.toString());

  return answer[0] === "0" ? "0" : answer;
}

const numbers = [6, 10, 2];

solution(numbers);
