// function solution(n, lost, reserve) {
//   let _lost = lost.sort((a, b) => a - b);
//   let _reserve = reserve.sort((a, b) => a - b);
//   let answer = n;

//   let hasShirt = Array.from({ length: n }, () => 0);

//   for (let i = 0; i < n; i++) {
//     if (!hasShirt[i]) {
//         if (_lost[0] === i+1) {

//         }

//     }
//   }

//   return answer;
// }

function solution(n, lost, reserve) {
  let _lost = lost.sort((a, b) => a - b).filter((e) => !reserve.includes(e));
  let _reserve = reserve.sort((a, b) => a - b).filter((e) => !lost.includes(e));

  let answer = n - _lost.length;

  for (let i = 0; i < _reserve.length; i++) {
    if (!_lost.length) break;
    if (_lost.includes(_reserve[i])) {
      _lost.splice(_lost.indexOf(_reserve[i]), 1);
      ++answer;
    } else {
      if (_lost.includes(_reserve[i] - 1)) {
        _lost.splice(_lost.indexOf(_reserve[i] - 1), 1);
        ++answer;
      } else if (_lost.includes(_reserve[i] + 1)) {
        _lost.splice(_lost.indexOf(_reserve[i] + 1), 1);
        ++answer;
      }
    }
  }

  return answer;
}

let n = 5;
let lost = [4, 3];
let reserve = [3, 2];

solution(n, lost, reserve);
