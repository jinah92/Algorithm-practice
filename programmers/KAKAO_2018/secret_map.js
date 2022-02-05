function solution(n, arr1, arr2) {
  let answer = [];
  let dec1 = getDecryption(arr1, n);
  let dec2 = getDecryption(arr2, n);

  console.log(dec1, dec2);

  for (let i = 0; i < n; i++) {
    answer.push([]);
    let inputs = "";
    for (let j = 0; j < n; j++) {
      if (dec1[i][j] === "0" && dec2[i][j] === "0") {
        inputs += " ";
      } else {
        inputs += "#";
      }
    }
    answer[i] = inputs;
  }

  return answer;
}

function getDecryption(arr, n) {
  let result = [];
  for (let a of arr) {
    result.push(a.toString(2).padStart(n, "0"));
  }
  return result;
}

const n = 5;
const arr1 = [9, 20, 28, 18, 11];
const arr2 = [30, 1, 21, 17, 28];

solution(n, arr1, arr2);
