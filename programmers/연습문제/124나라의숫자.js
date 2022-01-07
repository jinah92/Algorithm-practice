function solution(n) {
  let result = [];

  let mok = n;
  let remain = 0;

  while (parseInt(mok / 3) > 0) {
    remain = mok % 3;
    mok = parseInt(mok / 3);

    if (!remain) {
      mok -= 1;
      remain = 4;
    }
    result.push(remain.toString());
    if (mok === 3) {
      mok = 4;
      break;
    }
  }

  result.push(mok.toString());
  result = result.reverse().join("").replace("0", "");

  return result.length > 0 ? result : n.toString();
}
