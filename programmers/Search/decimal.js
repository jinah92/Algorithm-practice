function solution(numbers) {
  let answer = 0;

  // 순열 함수
  function getPermutaion(arr, selectNumber) {
    const result = [];
    if (selectNumber === 1) return arr.map((val) => [val]);

    arr.forEach((fixed, idx, origin) => {
      const rest = [...origin.slice(0, idx), ...origin.slice(idx + 1)];
      const permutaions = getPermutaion(rest, selectNumber - 1);
      const attached = permutaions.map((permutaion) => [fixed, ...permutaion]);
      result.push(...attached);
    });
    return result;
  }

  // 소수 찾기
  function isPrime(num) {
    if (num < 2) return false;
    for (let i = 2; i < Math.floor(Math.sqrt(num)) + 1; i++) {
      if (num % i === 0) return false;
    }
    return true;
  }

  let candidateNumbers = [];
  const NUMBERS = numbers.split("");
  for (let i = 1; i < NUMBERS.length + 1; i++) {
    candidateNumbers.push(
      ...getPermutaion(NUMBERS, i).map((arr) => Number(arr.join("")))
    );
  }
  candidateNumbers = [...new Set(candidateNumbers)];
  for (candidate of candidateNumbers) {
    if (/^0/g.test(candidate)) continue;
    if (isPrime(candidate)) answer += 1;
  }

  return answer;
}
