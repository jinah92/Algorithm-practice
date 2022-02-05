// N : 스테이지 개수, stages : 사용자가 현재 멈춰있는 스테이지의 번호
// 실패율 = 스테이지에 도달하였으나 아직 클리어하지 못한 플레이어 수 / 스테이지에 도달한 플레이어 수
// 실패율이 높은 스테이지부터 내림차순으로 스테이지 번호 배열을 리턴
function solution(N, stages) {
  let answer = [];
  for (let i = 1; i < N + 1; i++) {
    let failedRate = 0;
    let total = stages.filter((user) => user >= i).length;
    if (total) {
      let nonClear = stages.filter((user) => user === i).length;
      failedRate = nonClear / total;
    }
    answer.push({ idx: i, rate: failedRate });
  }
  return answer.sort((a, b) => b.rate - a.rate).map((el) => el.idx);
}

solution(5, [2, 1, 2, 6, 2, 4, 3, 3]);
