let max = 0;
let visit;

function solution(k, dungeons) {
  visit = Array.from({ length: dungeons.length }, () => null);
  for (let i = 0; i < dungeons.length; i++) {
    if (k >= dungeons[i][0]) dfs(i, k, 1, dungeons);
  }

  return max;
}

function dfs(curr, tired, depth, dungeons) {
  visit[curr] = true;
  tired -= dungeons[curr][1];
  for (let i = 0; i < dungeons.length; i++) {
    if (!visit[i] && dungeons[i][0] <= tired)
      dfs(i, tired, depth + 1, dungeons);
  }
  max = Math.max(depth, max);
  visit[curr] = false;
}

solution(80, [
  [80, 20],
  [50, 40],
  [30, 10],
]);
