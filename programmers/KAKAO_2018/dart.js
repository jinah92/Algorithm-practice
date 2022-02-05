function solution(dartResult) {
  const square = { S: 1, D: 2, T: 3 };
  const NUMS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"];
  let answer = 0;

  let targetNum = ["", "", ""];
  let inputIdx = 0;

  for (let result of dartResult) {
    if (NUMS.includes(result)) {
      targetNum[inputIdx] += result;
      continue;
    }

    if (result === "S" || result === "D" || result === "T") {
      targetNum[inputIdx] = Math.pow(
        Number(targetNum[inputIdx]),
        square[result]
      );
      if (targetNum[2] !== "") {
        answer += targetNum.shift();
        targetNum.push("");
      }
    }

    if (result === "*" || result === "#") {
      acceptOptions(result, targetNum, inputIdx - 1);
      if (inputIdx > 1) {
        answer += Number(targetNum[0]) + Number(targetNum[1]);
        targetNum = ["", "", ""];
        inputIdx = 0;
        continue;
      } else {
        inputIdx -= 1;
      }
    }
    inputIdx += 1;
  }
  targetNum.filter((num) => num !== "").map((el) => (answer += el));

  return answer;
}

function acceptOptions(option, targetNum, idx) {
  if (option === "*") {
    let cnt = 0;
    for (let i = 0; i < 3; i++) {
      if (targetNum[i] !== "") {
        cnt += 1;
        targetNum[i] *= 2;
      }
      if (cnt === 2) break;
    }
  } else {
    let targetIdx = 0;
    for (let i = 0; i < 3; i++) {
      if (targetNum[i] !== "") {
        targetIdx = i;
      } else {
        targetNum[targetIdx] *= -1;
        break;
      }
    }
  }
}

solution("1D2S3T*");
