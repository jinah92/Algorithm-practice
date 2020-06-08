function solution(n) {
  let arr = [];
  for (let i = 0; i < n + 1; i++) {
    arr.push(true);
  }
  console.log(arr);
  for (let i = 2; i * i <= n; i++) {
    if (arr[i]) {
      for (let j = i * i; j <= n; j += i) {
        arr[j] = false;
        console.log("소수가 아님 : " + i + "값 " + arr[j]);
      }
    }
  }
  arr.splice(0, 2, false, false);
  console.log(arr);
  const answer = arr.filter((val) => {
    return val !== false;
  });
  return answer.length;
}

console.log(solution(10));
console.log(solution(5));
