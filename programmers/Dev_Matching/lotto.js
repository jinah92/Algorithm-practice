function solution(lottos, win_nums) {
  const zeros = lottos.filter((x) => x === 0).length; // 모르는 수
  const equals = win_nums.filter((x) => lottos.includes(x)).length; // 일치하는 수

  return [getRate(equals + zeros), getRate(equals)];
}

function getRate(number) {
  return number > 1 ? 7 - number : 6;
}
