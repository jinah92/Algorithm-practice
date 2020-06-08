function solution(n) {
  let answer = 0;
  if (Number.isInteger(Math.sqrt(n))) {
    return Math.pow(Math.sqrt(n) + 1, 2);
  } else {
    return -1;
  }
}

console.log(solution(144));
console.log(solution(13));
