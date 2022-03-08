function solution(citations) {
  let answer = 0;
  const MAX = Math.max.apply(null, citations);
  citations.sort((a, b) => a - b);

  for (let i = 0; i < MAX + 1; i++) {
    let quote = 0,
      no_quote = 0;
    for (let j = 0; j < citations.length; j++) {
      if (citations[j] >= i) {
        quote += 1;
      } else {
        no_quote += 1;
      }
    }
    answer = quote >= i && no_quote <= i ? i : answer;
  }

  return answer;
}
