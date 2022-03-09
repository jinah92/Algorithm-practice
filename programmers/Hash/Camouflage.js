const clothes = [
  ["crowmask", "face"],
  ["bluesunglasses", "face"],
  ["smoky_makeup", "face"],
];

solution(clothes);

function solution(clothes) {
  let answer = 1;
  let hash = {};

  clothes.forEach((cloth) => {
    if (!(cloth[1] in hash)) {
      hash[cloth[1]] = 0;
    }
    hash[cloth[1]] += 1;
  });

  Object.keys(hash).forEach((key) => {
    answer *= hash[key] + 1;
  });

  return answer - 1;
}
