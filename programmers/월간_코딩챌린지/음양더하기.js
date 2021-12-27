function solution(absolutes, signs) {
  let result = 0;
  for (let i in signs) {
    if (!signs[i]) {
      result -= absolutes[i];
    } else {
      result += absolutes[i];
    }
  }
  return result;
}

solution([1, 2, 3], [false, false, true]);
