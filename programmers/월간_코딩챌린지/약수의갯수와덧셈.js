function solution(left, right) {
  let total = 0,
    divNum;
  for (let i = left; i <= right; i++) {
    divNum = 0;
    for (let j = 1; j <= i; j++) {
      if (i % j === 0) divNum += 1;
    }
    if (divNum % 2) {
      total -= i;
      continue;
    }
    total += i;
  }
  return total;
}
