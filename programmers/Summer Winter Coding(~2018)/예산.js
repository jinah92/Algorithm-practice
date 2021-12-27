function solution(d, budget) {
  let start = 0, end = d.length;
  let targetArray;

  d = d.sort((a, b) => a - b); // 작은 예산 순으로 정렬

  while (end > 0) {
    targetArray = d.slice(start, end)
    if (targetArray.reduce((stack, el)=>(stack+el), 0) <= budget) return targetArray.length;
    end -= 1
  }
  return 0;
}

// 파라미터 : 부서별 신청한 금액, 예산
// 리턴 : 최대 지원할 수 있는 부서의 수
solution([1,3,2,5,4], 9); // return : 3
solution([2,2,3,3], 10); // return : 4
