function solution(numbers) {
  let sum = 0;
  const sortedNumbers = numbers.sort((a, b) => a - b);

  for (let i = 0; i < 10; i++) {
    if (sortedNumbers.length === 0 || sortedNumbers[0] !== i) {
      sum += i;
    } else {
      sortedNumbers.shift();
    }
  }
  return sum;
}
