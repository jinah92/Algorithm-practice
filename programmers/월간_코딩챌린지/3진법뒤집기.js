function solution(n) {
  let quot = n;
  let result = "";

  while (quot > 0) {
    result += quot % 3;
    quot = parseInt(quot / 3);
  }
  return parseInt(result, 3);
}
