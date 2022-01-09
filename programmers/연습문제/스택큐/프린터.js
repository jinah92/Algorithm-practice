// 1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
// 2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
// 3. 그렇지 않으면 J를 인쇄합니다.
function solution(priorities, location) {
  let needToPrints = [];
  let printOrder = [];

  priorities.forEach((item, key) => {
    needToPrints.push([key, item]);
  });

  while (needToPrints.length) {
    let pushNew = true;
    const print = needToPrints.shift();

    for (let i = 0; i < needToPrints.length; i++) {
      if (needToPrints[i][1] > print[1]) {
        needToPrints.push(print);
        pushNew = false;
        break;
      }
    }
    if (pushNew) printOrder.push(print);
  }
  for (let i = 0; i < printOrder.length; i++) {
    if (printOrder[i][0] === location) return i + 1;
  }
}
