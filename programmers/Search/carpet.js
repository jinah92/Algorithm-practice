function solution(brown, yellow) {
  let total = brown + yellow;
  let init = 3;

  while (true) {
    if (init >= total / init && (init - 2) * (total / init - 2) === yellow) {
      break;
    }
    init += 1;
  }

  return [init, total / init];
}
