function solution(arr) {
  if (arr.length === 1) {
    return [-1];
  }
  const minVal = Math.min.apply(null, arr);
  arr.splice(arr.indexOf(minVal), 1);
  return arr;
}

let test = solution([4, 3, 2, 1]);
console.log(test);
