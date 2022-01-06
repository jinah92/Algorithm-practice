function solution(board, moves) {
  let cnt = 0;
  const stack = [];
  const size = Math.max.apply(null, moves);

  for (const move of moves) {
    for (let i = 0; i < size; i++) {
      const target = board[i][move - 1];
      if (target) {
        board[i][move - 1] = 0;
        if (stack.length > 0 && stack[stack.length - 1] === target) {
          // 연이든 값이 같은 인형인 경우
          cnt += 2;
          stack.pop();
        } else {
          // 인형 쌓기
          stack.push(target);
        }
        break;
      }
    }
  }
  return cnt;
}
