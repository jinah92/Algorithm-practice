// progresses : 각 작업의 진도율(%), speeds : 각 작업의 개발 속도
// return값 : 각 배포별 기능 개수
function solution(progresses, speeds) {
  const lastDays = [];
  const lastJobs = progresses.map((a) => 100 - a);
  for (let i = 0; i < speeds.length; i++) {
    lastDays.push(Math.ceil(lastJobs[i] / speeds[i]));
  }

  let acc = 0,
    input = 0;
  let returnData = [];

  lastDays.forEach((item, idx) => {
    if (idx === 0) {
      acc = item;
      input = 1;
    } else {
      if (item > acc) {
        returnData.push(input);
        input = 1;
        acc = item;
      } else {
        input += 1;
      }
    }
  });
  returnData.push(input);

  return returnDat;
}
