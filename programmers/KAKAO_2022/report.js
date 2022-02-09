function solution(id_list, report, k) {
  let answer = Array.from({ length: id_list.length }, () => 0);
  let idxObj = Object(id_list); // key: 유저인덱스, value: 유저이름
  const keys = Object.keys(idxObj);
  let reportObj = Object(); // key: 신고대상자, value : [신고당한 횟수: number, 신고한 유저목록: array]

  // 초기화
  id_list.forEach((id) => {
    reportObj[id] = [0, []];
  });

  // 신고한 사람, 신고당한 사람, 횟수 체크
  report.forEach((person, i) => {
    const [user, resportee] = person.split(" ");
    if (!reportObj[resportee][1].includes(user)) {
      // 유저당 다른 유저는 1번만 신고 가능
      reportObj[resportee][1].push(user);
      reportObj[resportee][0] += 1;
    }
  });

  id_list.forEach((item, idx) => {
    if (reportObj[item][0] >= k) {
      // 신고 제한횟수를 초과한 경우
      for (let i = 0; i < keys.length; i++) {
        const value = idxObj[keys[i]];
        if (reportObj[item][1].includes(value)) {
          answer[Number(keys[i])] += 1;
        }
      }
    }
  });

  return answer;
}
