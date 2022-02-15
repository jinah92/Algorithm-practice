function solution(k, dungeons) {
  let answer = 0;
  let obj = {};

  let needs = [];

  dungeons.forEach((hp) => {
    needs.push(hp[0]);
    obj[hp[0]] = [hp[1], 0];
  });

  needs.sort((a, b) => b - a);

  let _k = k;
  let _list = [needs[0]];
  let tmp = [needs[0], needs[0] - obj[needs[0]][0]];
  let i = 0;
  _k = _k - obj[needs[0]][0];
  // 첫번째로 필요 피로도가 높은곳 을 방문
  while (i < needs.length) {
    needs.forEach((el) => {
      if (obj[el][0] - _k && !_list.includes(el)) {
        if (tmp[1] > _k - obj[el][0]) {
          tmp = [el, _k - obj[el][0]];
        }
      }
    });
    _list.push(tmp[0]);
    i += 1;
  }

  // 첫번째로 잔여 피로도가 높은 곳을 방문

  console.log(obj);

  while (k) {
    for (let key in obj) {
      obj[key][1] = k - obj[key][0];
    }
    console.log(obj);
  }

  return answer;
}

solution(80, [
  [80, 20],
  [50, 40],
  [30, 10],
]);
